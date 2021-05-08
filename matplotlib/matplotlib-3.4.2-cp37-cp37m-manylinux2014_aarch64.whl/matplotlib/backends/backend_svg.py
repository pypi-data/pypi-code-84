from collections import OrderedDict
import base64
import datetime
import gzip
import hashlib
from io import BytesIO, StringIO, TextIOWrapper
import itertools
import logging
import os
import re
import uuid

import numpy as np
from PIL import Image

import matplotlib as mpl
from matplotlib import _api, cbook
from matplotlib.backend_bases import (
     _Backend, _check_savefig_extra_args, FigureCanvasBase, FigureManagerBase,
     RendererBase, _no_output_draw)
from matplotlib.backends.backend_mixed import MixedModeRenderer
from matplotlib.colors import rgb2hex
from matplotlib.dates import UTC
from matplotlib.font_manager import findfont, get_font
from matplotlib.ft2font import LOAD_NO_HINTING
from matplotlib.mathtext import MathTextParser
from matplotlib.path import Path
from matplotlib import _path
from matplotlib.transforms import Affine2D, Affine2DBase

_log = logging.getLogger(__name__)

backend_version = mpl.__version__

# ----------------------------------------------------------------------
# SimpleXMLWriter class
#
# Based on an original by Fredrik Lundh, but modified here to:
#   1. Support modern Python idioms
#   2. Remove encoding support (it's handled by the file writer instead)
#   3. Support proper indentation
#   4. Minify things a little bit

# --------------------------------------------------------------------
# The SimpleXMLWriter module is
#
# Copyright (c) 2001-2004 by Fredrik Lundh
#
# By obtaining, using, and/or copying this software and/or its
# associated documentation, you agree that you have read, understood,
# and will comply with the following terms and conditions:
#
# Permission to use, copy, modify, and distribute this software and
# its associated documentation for any purpose and without fee is
# hereby granted, provided that the above copyright notice appears in
# all copies, and that both that copyright notice and this permission
# notice appear in supporting documentation, and that the name of
# Secret Labs AB or the author not be used in advertising or publicity
# pertaining to distribution of the software without specific, written
# prior permission.
#
# SECRET LABS AB AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD
# TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANT-
# ABILITY AND FITNESS.  IN NO EVENT SHALL SECRET LABS AB OR THE AUTHOR
# BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY
# DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,
# WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
# ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE
# OF THIS SOFTWARE.
# --------------------------------------------------------------------


def escape_cdata(s):
    s = s.replace("&", "&amp;")
    s = s.replace("<", "&lt;")
    s = s.replace(">", "&gt;")
    return s


_escape_xml_comment = re.compile(r'-(?=-)')


def escape_comment(s):
    s = escape_cdata(s)
    return _escape_xml_comment.sub('- ', s)


def escape_attrib(s):
    s = s.replace("&", "&amp;")
    s = s.replace("'", "&apos;")
    s = s.replace('"', "&quot;")
    s = s.replace("<", "&lt;")
    s = s.replace(">", "&gt;")
    return s


def short_float_fmt(x):
    """
    Create a short string representation of a float, which is %f
    formatting with trailing zeros and the decimal point removed.
    """
    return '{0:f}'.format(x).rstrip('0').rstrip('.')


class XMLWriter:
    """
    Parameters
    ----------
    file : writable text file-like object
    """

    def __init__(self, file):
        self.__write = file.write
        if hasattr(file, "flush"):
            self.flush = file.flush
        self.__open = 0  # true if start tag is open
        self.__tags = []
        self.__data = []
        self.__indentation = " " * 64

    def __flush(self, indent=True):
        # flush internal buffers
        if self.__open:
            if indent:
                self.__write(">\n")
            else:
                self.__write(">")
            self.__open = 0
        if self.__data:
            data = ''.join(self.__data)
            self.__write(escape_cdata(data))
            self.__data = []

    def start(self, tag, attrib={}, **extra):
        """
        Open a new element.  Attributes can be given as keyword
        arguments, or as a string/string dictionary. The method returns
        an opaque identifier that can be passed to the :meth:`close`
        method, to close all open elements up to and including this one.

        Parameters
        ----------
        tag
            Element tag.
        attrib
            Attribute dictionary.  Alternatively, attributes can be given as
            keyword arguments.

        Returns
        -------
        An element identifier.
        """
        self.__flush()
        tag = escape_cdata(tag)
        self.__data = []
        self.__tags.append(tag)
        self.__write(self.__indentation[:len(self.__tags) - 1])
        self.__write("<%s" % tag)
        for k, v in sorted({**attrib, **extra}.items()):
            if v:
                k = escape_cdata(k)
                v = escape_attrib(v)
                self.__write(' %s="%s"' % (k, v))
        self.__open = 1
        return len(self.__tags) - 1

    def comment(self, comment):
        """
        Add a comment to the output stream.

        Parameters
        ----------
        comment : str
            Comment text.
        """
        self.__flush()
        self.__write(self.__indentation[:len(self.__tags)])
        self.__write("<!-- %s -->\n" % escape_comment(comment))

    def data(self, text):
        """
        Add character data to the output stream.

        Parameters
        ----------
        text : str
            Character data.
        """
        self.__data.append(text)

    def end(self, tag=None, indent=True):
        """
        Close the current element (opened by the most recent call to
        :meth:`start`).

        Parameters
        ----------
        tag
            Element tag.  If given, the tag must match the start tag.  If
            omitted, the current element is closed.
        """
        if tag:
            assert self.__tags, "unbalanced end(%s)" % tag
            assert escape_cdata(tag) == self.__tags[-1], \
                "expected end(%s), got %s" % (self.__tags[-1], tag)
        else:
            assert self.__tags, "unbalanced end()"
        tag = self.__tags.pop()
        if self.__data:
            self.__flush(indent)
        elif self.__open:
            self.__open = 0
            self.__write("/>\n")
            return
        if indent:
            self.__write(self.__indentation[:len(self.__tags)])
        self.__write("</%s>\n" % tag)

    def close(self, id):
        """
        Close open elements, up to (and including) the element identified
        by the given identifier.

        Parameters
        ----------
        id
            Element identifier, as returned by the :meth:`start` method.
        """
        while len(self.__tags) > id:
            self.end()

    def element(self, tag, text=None, attrib={}, **extra):
        """
        Add an entire element.  This is the same as calling :meth:`start`,
        :meth:`data`, and :meth:`end` in sequence. The *text* argument can be
        omitted.
        """
        self.start(tag, attrib, **extra)
        if text:
            self.data(text)
        self.end(indent=False)

    def flush(self):
        """Flush the output stream."""
        pass  # replaced by the constructor


def generate_transform(transform_list=[]):
    if len(transform_list):
        output = StringIO()
        for type, value in transform_list:
            if (type == 'scale' and (value == (1,) or value == (1, 1))
                    or type == 'translate' and value == (0, 0)
                    or type == 'rotate' and value == (0,)):
                continue
            if type == 'matrix' and isinstance(value, Affine2DBase):
                value = value.to_values()
            output.write('%s(%s)' % (
                type, ' '.join(short_float_fmt(x) for x in value)))
        return output.getvalue()
    return ''


def generate_css(attrib={}):
    if attrib:
        output = StringIO()
        attrib = sorted(attrib.items())
        for k, v in attrib:
            k = escape_attrib(k)
            v = escape_attrib(v)
            output.write("%s:%s;" % (k, v))
        return output.getvalue()
    return ''


_capstyle_d = {'projecting': 'square', 'butt': 'butt', 'round': 'round'}


class RendererSVG(RendererBase):
    def __init__(self, width, height, svgwriter, basename=None, image_dpi=72,
                 *, metadata=None):
        self.width = width
        self.height = height
        self.writer = XMLWriter(svgwriter)
        self.image_dpi = image_dpi  # actual dpi at which we rasterize stuff

        self._groupd = {}
        self.basename = basename
        self._image_counter = itertools.count()
        self._clipd = OrderedDict()
        self._markers = {}
        self._path_collection_id = 0
        self._hatchd = OrderedDict()
        self._has_gouraud = False
        self._n_gradients = 0
        self._fonts = OrderedDict()

        super().__init__()
        self._glyph_map = dict()
        str_height = short_float_fmt(height)
        str_width = short_float_fmt(width)
        svgwriter.write(svgProlog)
        self._start_id = self.writer.start(
            'svg',
            width='%spt' % str_width,
            height='%spt' % str_height,
            viewBox='0 0 %s %s' % (str_width, str_height),
            xmlns="http://www.w3.org/2000/svg",
            version="1.1",
            attrib={'xmlns:xlink': "http://www.w3.org/1999/xlink"})
        self._write_metadata(metadata)
        self._write_default_style()

    @_api.deprecated("3.4")
    @property
    def mathtext_parser(self):
        return MathTextParser('SVG')

    def finalize(self):
        self._write_clips()
        self._write_hatches()
        self.writer.close(self._start_id)
        self.writer.flush()

    def _write_metadata(self, metadata):
        # Add metadata following the Dublin Core Metadata Initiative, and the
        # Creative Commons Rights Expression Language. This is mainly for
        # compatibility with Inkscape.
        if metadata is None:
            metadata = {}
        metadata = {
            'Format': 'image/svg+xml',
            'Type': 'http://purl.org/dc/dcmitype/StillImage',
            'Creator':
                f'Matplotlib v{mpl.__version__}, https://matplotlib.org/',
            **metadata
        }
        writer = self.writer

        if 'Title' in metadata:
            writer.element('title', text=metadata['Title'])

        # Special handling.
        date = metadata.get('Date', None)
        if date is not None:
            if isinstance(date, str):
                dates = [date]
            elif isinstance(date, (datetime.datetime, datetime.date)):
                dates = [date.isoformat()]
            elif np.iterable(date):
                dates = []
                for d in date:
                    if isinstance(d, str):
                        dates.append(d)
                    elif isinstance(d, (datetime.datetime, datetime.date)):
                        dates.append(d.isoformat())
                    else:
                        raise ValueError(
                            'Invalid type for Date metadata. '
                            'Expected iterable of str, date, or datetime, '
                            'not {!r}.'.format(type(d)))
            else:
                raise ValueError('Invalid type for Date metadata. '
                                 'Expected str, date, datetime, or iterable '
                                 'of the same, not {!r}.'.format(type(date)))
            metadata['Date'] = '/'.join(dates)
        elif 'Date' not in metadata:
            # Do not add `Date` if the user explicitly set `Date` to `None`
            # Get source date from SOURCE_DATE_EPOCH, if set.
            # See https://reproducible-builds.org/specs/source-date-epoch/
            date = os.getenv("SOURCE_DATE_EPOCH")
            if date:
                date = datetime.datetime.utcfromtimestamp(int(date))
                metadata['Date'] = date.replace(tzinfo=UTC).isoformat()
            else:
                metadata['Date'] = datetime.datetime.today().isoformat()

        mid = None
        def ensure_metadata(mid):
            if mid is not None:
                return mid
            mid = writer.start('metadata')
            writer.start('rdf:RDF', attrib={
                'xmlns:dc': "http://purl.org/dc/elements/1.1/",
                'xmlns:cc': "http://creativecommons.org/ns#",
                'xmlns:rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
            })
            writer.start('cc:Work')
            return mid

        uri = metadata.pop('Type', None)
        if uri is not None:
            mid = ensure_metadata(mid)
            writer.element('dc:type', attrib={'rdf:resource': uri})

        # Single value only.
        for key in ['title', 'coverage', 'date', 'description', 'format',
                    'identifier', 'language', 'relation', 'source']:
            info = metadata.pop(key.title(), None)
            if info is not None:
                mid = ensure_metadata(mid)
                writer.element(f'dc:{key}', text=info)

        # Multiple Agent values.
        for key in ['creator', 'contributor', 'publisher', 'rights']:
            agents = metadata.pop(key.title(), None)
            if agents is None:
                continue

            if isinstance(agents, str):
                agents = [agents]

            mid = ensure_metadata(mid)
            writer.start(f'dc:{key}')
            for agent in agents:
                writer.start('cc:Agent')
                writer.element('dc:title', text=agent)
                writer.end('cc:Agent')
            writer.end(f'dc:{key}')

        # Multiple values.
        keywords = metadata.pop('Keywords', None)
        if keywords is not None:
            if isinstance(keywords, str):
                keywords = [keywords]

            mid = ensure_metadata(mid)
            writer.start('dc:subject')
            writer.start('rdf:Bag')
            for keyword in keywords:
                writer.element('rdf:li', text=keyword)
            writer.end('rdf:Bag')
            writer.end('dc:subject')

        if mid is not None:
            writer.close(mid)

        if metadata:
            raise ValueError('Unknown metadata key(s) passed to SVG writer: ' +
                             ','.join(metadata))

    def _write_default_style(self):
        writer = self.writer
        default_style = generate_css({
            'stroke-linejoin': 'round',
            'stroke-linecap': 'butt'})
        writer.start('defs')
        writer.element('style', type='text/css', text='*{%s}' % default_style)
        writer.end('defs')

    def _make_id(self, type, content):
        salt = mpl.rcParams['svg.hashsalt']
        if salt is None:
            salt = str(uuid.uuid4())
        m = hashlib.sha256()
        m.update(salt.encode('utf8'))
        m.update(str(content).encode('utf8'))
        return '%s%s' % (type, m.hexdigest()[:10])

    def _make_flip_transform(self, transform):
        return (transform +
                Affine2D()
                .scale(1.0, -1.0)
                .translate(0.0, self.height))

    def _get_font(self, prop):
        fname = findfont(prop)
        font = get_font(fname)
        font.clear()
        size = prop.get_size_in_points()
        font.set_size(size, 72.0)
        return font

    def _get_hatch(self, gc, rgbFace):
        """
        Create a new hatch pattern
        """
        if rgbFace is not None:
            rgbFace = tuple(rgbFace)
        edge = gc.get_hatch_color()
        if edge is not None:
            edge = tuple(edge)
        dictkey = (gc.get_hatch(), rgbFace, edge)
        oid = self._hatchd.get(dictkey)
        if oid is None:
            oid = self._make_id('h', dictkey)
            self._hatchd[dictkey] = ((gc.get_hatch_path(), rgbFace, edge), oid)
        else:
            _, oid = oid
        return oid

    def _write_hatches(self):
        if not len(self._hatchd):
            return
        HATCH_SIZE = 72
        writer = self.writer
        writer.start('defs')
        for (path, face, stroke), oid in self._hatchd.values():
            writer.start(
                'pattern',
                id=oid,
                patternUnits="userSpaceOnUse",
                x="0", y="0", width=str(HATCH_SIZE),
                height=str(HATCH_SIZE))
            path_data = self._convert_path(
                path,
                Affine2D()
                .scale(HATCH_SIZE).scale(1.0, -1.0).translate(0, HATCH_SIZE),
                simplify=False)
            if face is None:
                fill = 'none'
            else:
                fill = rgb2hex(face)
            writer.element(
                'rect',
                x="0", y="0", width=str(HATCH_SIZE+1),
                height=str(HATCH_SIZE+1),
                fill=fill)
            hatch_style = {
                    'fill': rgb2hex(stroke),
                    'stroke': rgb2hex(stroke),
                    'stroke-width': str(mpl.rcParams['hatch.linewidth']),
                    'stroke-linecap': 'butt',
                    'stroke-linejoin': 'miter'
                    }
            if stroke[3] < 1:
                hatch_style['stroke-opacity'] = str(stroke[3])
            writer.element(
                'path',
                d=path_data,
                style=generate_css(hatch_style)
                )
            writer.end('pattern')
        writer.end('defs')

    def _get_style_dict(self, gc, rgbFace):
        """Generate a style string from the GraphicsContext and rgbFace."""
        attrib = {}

        forced_alpha = gc.get_forced_alpha()

        if gc.get_hatch() is not None:
            attrib['fill'] = "url(#%s)" % self._get_hatch(gc, rgbFace)
            if (rgbFace is not None and len(rgbFace) == 4 and rgbFace[3] != 1.0
                    and not forced_alpha):
                attrib['fill-opacity'] = short_float_fmt(rgbFace[3])
        else:
            if rgbFace is None:
                attrib['fill'] = 'none'
            else:
                if tuple(rgbFace[:3]) != (0, 0, 0):
                    attrib['fill'] = rgb2hex(rgbFace)
                if (len(rgbFace) == 4 and rgbFace[3] != 1.0
                        and not forced_alpha):
                    attrib['fill-opacity'] = short_float_fmt(rgbFace[3])

        if forced_alpha and gc.get_alpha() != 1.0:
            attrib['opacity'] = short_float_fmt(gc.get_alpha())

        offset, seq = gc.get_dashes()
        if seq is not None:
            attrib['stroke-dasharray'] = ','.join(
                short_float_fmt(val) for val in seq)
            attrib['stroke-dashoffset'] = short_float_fmt(float(offset))

        linewidth = gc.get_linewidth()
        if linewidth:
            rgb = gc.get_rgb()
            attrib['stroke'] = rgb2hex(rgb)
            if not forced_alpha and rgb[3] != 1.0:
                attrib['stroke-opacity'] = short_float_fmt(rgb[3])
            if linewidth != 1.0:
                attrib['stroke-width'] = short_float_fmt(linewidth)
            if gc.get_joinstyle() != 'round':
                attrib['stroke-linejoin'] = gc.get_joinstyle()
            if gc.get_capstyle() != 'butt':
                attrib['stroke-linecap'] = _capstyle_d[gc.get_capstyle()]

        return attrib

    def _get_style(self, gc, rgbFace):
        return generate_css(self._get_style_dict(gc, rgbFace))

    def _get_clip(self, gc):
        cliprect = gc.get_clip_rectangle()
        clippath, clippath_trans = gc.get_clip_path()
        if clippath is not None:
            clippath_trans = self._make_flip_transform(clippath_trans)
            dictkey = (id(clippath), str(clippath_trans))
        elif cliprect is not None:
            x, y, w, h = cliprect.bounds
            y = self.height-(y+h)
            dictkey = (x, y, w, h)
        else:
            return None

        clip = self._clipd.get(dictkey)
        if clip is None:
            oid = self._make_id('p', dictkey)
            if clippath is not None:
                self._clipd[dictkey] = ((clippath, clippath_trans), oid)
            else:
                self._clipd[dictkey] = (dictkey, oid)
        else:
            clip, oid = clip
        return oid

    def _write_clips(self):
        if not len(self._clipd):
            return
        writer = self.writer
        writer.start('defs')
        for clip, oid in self._clipd.values():
            writer.start('clipPath', id=oid)
            if len(clip) == 2:
                clippath, clippath_trans = clip
                path_data = self._convert_path(
                    clippath, clippath_trans, simplify=False)
                writer.element('path', d=path_data)
            else:
                x, y, w, h = clip
                writer.element(
                    'rect',
                    x=short_float_fmt(x),
                    y=short_float_fmt(y),
                    width=short_float_fmt(w),
                    height=short_float_fmt(h))
            writer.end('clipPath')
        writer.end('defs')

    def open_group(self, s, gid=None):
        # docstring inherited
        if gid:
            self.writer.start('g', id=gid)
        else:
            self._groupd[s] = self._groupd.get(s, 0) + 1
            self.writer.start('g', id="%s_%d" % (s, self._groupd[s]))

    def close_group(self, s):
        # docstring inherited
        self.writer.end('g')

    def option_image_nocomposite(self):
        # docstring inherited
        return not mpl.rcParams['image.composite_image']

    def _convert_path(self, path, transform=None, clip=None, simplify=None,
                      sketch=None):
        if clip:
            clip = (0.0, 0.0, self.width, self.height)
        else:
            clip = None
        return _path.convert_to_string(
            path, transform, clip, simplify, sketch, 6,
            [b'M', b'L', b'Q', b'C', b'z'], False).decode('ascii')

    def draw_path(self, gc, path, transform, rgbFace=None):
        # docstring inherited
        trans_and_flip = self._make_flip_transform(transform)
        clip = (rgbFace is None and gc.get_hatch_path() is None)
        simplify = path.should_simplify and clip
        path_data = self._convert_path(
            path, trans_and_flip, clip=clip, simplify=simplify,
            sketch=gc.get_sketch_params())

        attrib = {}
        attrib['style'] = self._get_style(gc, rgbFace)

        clipid = self._get_clip(gc)
        if clipid is not None:
            attrib['clip-path'] = 'url(#%s)' % clipid

        if gc.get_url() is not None:
            self.writer.start('a', {'xlink:href': gc.get_url()})
        self.writer.element('path', d=path_data, attrib=attrib)
        if gc.get_url() is not None:
            self.writer.end('a')

    def draw_markers(
            self, gc, marker_path, marker_trans, path, trans, rgbFace=None):
        # docstring inherited

        if not len(path.vertices):
            return

        writer = self.writer
        path_data = self._convert_path(
            marker_path,
            marker_trans + Affine2D().scale(1.0, -1.0),
            simplify=False)
        style = self._get_style_dict(gc, rgbFace)
        dictkey = (path_data, generate_css(style))
        oid = self._markers.get(dictkey)
        style = generate_css({k: v for k, v in style.items()
                              if k.startswith('stroke')})

        if oid is None:
            oid = self._make_id('m', dictkey)
            writer.start('defs')
            writer.element('path', id=oid, d=path_data, style=style)
            writer.end('defs')
            self._markers[dictkey] = oid

        attrib = {}
        clipid = self._get_clip(gc)
        if clipid is not None:
            attrib['clip-path'] = 'url(#%s)' % clipid
        writer.start('g', attrib=attrib)

        trans_and_flip = self._make_flip_transform(trans)
        attrib = {'xlink:href': '#%s' % oid}
        clip = (0, 0, self.width*72, self.height*72)
        for vertices, code in path.iter_segments(
                trans_and_flip, clip=clip, simplify=False):
            if len(vertices):
                x, y = vertices[-2:]
                attrib['x'] = short_float_fmt(x)
                attrib['y'] = short_float_fmt(y)
                attrib['style'] = self._get_style(gc, rgbFace)
                writer.element('use', attrib=attrib)
        writer.end('g')

    def draw_path_collection(self, gc, master_transform, paths, all_transforms,
                             offsets, offsetTrans, facecolors, edgecolors,
                             linewidths, linestyles, antialiaseds, urls,
                             offset_position):
        # Is the optimization worth it? Rough calculation:
        # cost of emitting a path in-line is
        #    (len_path + 5) * uses_per_path
        # cost of definition+use is
        #    (len_path + 3) + 9 * uses_per_path
        len_path = len(paths[0].vertices) if len(paths) > 0 else 0
        uses_per_path = self._iter_collection_uses_per_path(
            paths, all_transforms, offsets, facecolors, edgecolors)
        should_do_optimization = \
            len_path + 9 * uses_per_path + 3 < (len_path + 5) * uses_per_path
        if not should_do_optimization:
            return super().draw_path_collection(
                gc, master_transform, paths, all_transforms,
                offsets, offsetTrans, facecolors, edgecolors,
                linewidths, linestyles, antialiaseds, urls,
                offset_position)

        writer = self.writer
        path_codes = []
        writer.start('defs')
        for i, (path, transform) in enumerate(self._iter_collection_raw_paths(
                master_transform, paths, all_transforms)):
            transform = Affine2D(transform.get_matrix()).scale(1.0, -1.0)
            d = self._convert_path(path, transform, simplify=False)
            oid = 'C%x_%x_%s' % (
                self._path_collection_id, i, self._make_id('', d))
            writer.element('path', id=oid, d=d)
            path_codes.append(oid)
        writer.end('defs')

        for xo, yo, path_id, gc0, rgbFace in self._iter_collection(
                gc, master_transform, all_transforms, path_codes, offsets,
                offsetTrans, facecolors, edgecolors, linewidths, linestyles,
                antialiaseds, urls, offset_position):
            clipid = self._get_clip(gc0)
            url = gc0.get_url()
            if url is not None:
                writer.start('a', attrib={'xlink:href': url})
            if clipid is not None:
                writer.start('g', attrib={'clip-path': 'url(#%s)' % clipid})
            attrib = {
                'xlink:href': '#%s' % path_id,
                'x': short_float_fmt(xo),
                'y': short_float_fmt(self.height - yo),
                'style': self._get_style(gc0, rgbFace)
                }
            writer.element('use', attrib=attrib)
            if clipid is not None:
                writer.end('g')
            if url is not None:
                writer.end('a')

        self._path_collection_id += 1

    def draw_gouraud_triangle(self, gc, points, colors, trans):
        # docstring inherited

        # This uses a method described here:
        #
        #   http://www.svgopen.org/2005/papers/Converting3DFaceToSVG/index.html
        #
        # that uses three overlapping linear gradients to simulate a
        # Gouraud triangle.  Each gradient goes from fully opaque in
        # one corner to fully transparent along the opposite edge.
        # The line between the stop points is perpendicular to the
        # opposite edge.  Underlying these three gradients is a solid
        # triangle whose color is the average of all three points.

        writer = self.writer
        if not self._has_gouraud:
            self._has_gouraud = True
            writer.start(
                'filter',
                id='colorAdd')
            writer.element(
                'feComposite',
                attrib={'in': 'SourceGraphic'},
                in2='BackgroundImage',
                operator='arithmetic',
                k2="1", k3="1")
            writer.end('filter')
            # feColorMatrix filter to correct opacity
            writer.start(
                'filter',
                id='colorMat')
            writer.element(
                'feColorMatrix',
                attrib={'type': 'matrix'},
                values='1 0 0 0 0 \n0 1 0 0 0 \n0 0 1 0 0' +
                       ' \n1 1 1 1 0 \n0 0 0 0 1 ')
            writer.end('filter')

        avg_color = np.average(colors, axis=0)
        if avg_color[-1] == 0:
            # Skip fully-transparent triangles
            return

        trans_and_flip = self._make_flip_transform(trans)
        tpoints = trans_and_flip.transform(points)

        writer.start('defs')
        for i in range(3):
            x1, y1 = tpoints[i]
            x2, y2 = tpoints[(i + 1) % 3]
            x3, y3 = tpoints[(i + 2) % 3]
            rgba_color = colors[i]

            if x2 == x3:
                xb = x2
                yb = y1
            elif y2 == y3:
                xb = x1
                yb = y2
            else:
                m1 = (y2 - y3) / (x2 - x3)
                b1 = y2 - (m1 * x2)
                m2 = -(1.0 / m1)
                b2 = y1 - (m2 * x1)
                xb = (-b1 + b2) / (m1 - m2)
                yb = m2 * xb + b2

            writer.start(
                'linearGradient',
                id="GR%x_%d" % (self._n_gradients, i),
                gradientUnits="userSpaceOnUse",
                x1=short_float_fmt(x1), y1=short_float_fmt(y1),
                x2=short_float_fmt(xb), y2=short_float_fmt(yb))
            writer.element(
                'stop',
                offset='1',
                style=generate_css({
                    'stop-color': rgb2hex(avg_color),
                    'stop-opacity': short_float_fmt(rgba_color[-1])}))
            writer.element(
                'stop',
                offset='0',
                style=generate_css({'stop-color': rgb2hex(rgba_color),
                                    'stop-opacity': "0"}))

            writer.end('linearGradient')

        writer.end('defs')

        # triangle formation using "path"
        dpath = "M " + short_float_fmt(x1)+',' + short_float_fmt(y1)
        dpath += " L " + short_float_fmt(x2) + ',' + short_float_fmt(y2)
        dpath += " " + short_float_fmt(x3) + ',' + short_float_fmt(y3) + " Z"

        writer.element(
            'path',
            attrib={'d': dpath,
                    'fill': rgb2hex(avg_color),
                    'fill-opacity': '1',
                    'shape-rendering': "crispEdges"})

        writer.start(
                'g',
                attrib={'stroke': "none",
                        'stroke-width': "0",
                        'shape-rendering': "crispEdges",
                        'filter': "url(#colorMat)"})

        writer.element(
            'path',
            attrib={'d': dpath,
                    'fill': 'url(#GR%x_0)' % self._n_gradients,
                    'shape-rendering': "crispEdges"})

        writer.element(
            'path',
            attrib={'d': dpath,
                    'fill': 'url(#GR%x_1)' % self._n_gradients,
                    'filter': 'url(#colorAdd)',
                    'shape-rendering': "crispEdges"})

        writer.element(
            'path',
            attrib={'d': dpath,
                    'fill': 'url(#GR%x_2)' % self._n_gradients,
                    'filter': 'url(#colorAdd)',
                    'shape-rendering': "crispEdges"})

        writer.end('g')

        self._n_gradients += 1

    def draw_gouraud_triangles(self, gc, triangles_array, colors_array,
                               transform):
        attrib = {}
        clipid = self._get_clip(gc)
        if clipid is not None:
            attrib['clip-path'] = 'url(#%s)' % clipid

        self.writer.start('g', attrib=attrib)

        transform = transform.frozen()
        for tri, col in zip(triangles_array, colors_array):
            self.draw_gouraud_triangle(gc, tri, col, transform)

        self.writer.end('g')

    def option_scale_image(self):
        # docstring inherited
        return True

    def get_image_magnification(self):
        return self.image_dpi / 72.0

    def draw_image(self, gc, x, y, im, transform=None):
        # docstring inherited

        h, w = im.shape[:2]

        if w == 0 or h == 0:
            return

        attrib = {}
        clipid = self._get_clip(gc)
        if clipid is not None:
            # Can't apply clip-path directly to the image because the
            # image has a transformation, which would also be applied
            # to the clip-path
            self.writer.start('g', attrib={'clip-path': 'url(#%s)' % clipid})

        oid = gc.get_gid()
        url = gc.get_url()
        if url is not None:
            self.writer.start('a', attrib={'xlink:href': url})
        if mpl.rcParams['svg.image_inline']:
            buf = BytesIO()
            Image.fromarray(im).save(buf, format="png")
            oid = oid or self._make_id('image', buf.getvalue())
            attrib['xlink:href'] = (
                "data:image/png;base64,\n" +
                base64.b64encode(buf.getvalue()).decode('ascii'))
        else:
            if self.basename is None:
                raise ValueError("Cannot save image data to filesystem when "
                                 "writing SVG to an in-memory buffer")
            filename = '{}.image{}.png'.format(
                self.basename, next(self._image_counter))
            _log.info('Writing image file for inclusion: %s', filename)
            Image.fromarray(im).save(filename)
            oid = oid or 'Im_' + self._make_id('image', filename)
            attrib['xlink:href'] = filename

        attrib['id'] = oid

        if transform is None:
            w = 72.0 * w / self.image_dpi
            h = 72.0 * h / self.image_dpi

            self.writer.element(
                'image',
                transform=generate_transform([
                    ('scale', (1, -1)), ('translate', (0, -h))]),
                x=short_float_fmt(x),
                y=short_float_fmt(-(self.height - y - h)),
                width=short_float_fmt(w), height=short_float_fmt(h),
                attrib=attrib)
        else:
            alpha = gc.get_alpha()
            if alpha != 1.0:
                attrib['opacity'] = short_float_fmt(alpha)

            flipped = (
                Affine2D().scale(1.0 / w, 1.0 / h) +
                transform +
                Affine2D()
                .translate(x, y)
                .scale(1.0, -1.0)
                .translate(0.0, self.height))

            attrib['transform'] = generate_transform(
                [('matrix', flipped.frozen())])
            attrib['style'] = (
                'image-rendering:crisp-edges;'
                'image-rendering:pixelated')
            self.writer.element(
                'image',
                width=short_float_fmt(w), height=short_float_fmt(h),
                attrib=attrib)

        if url is not None:
            self.writer.end('a')
        if clipid is not None:
            self.writer.end('g')

    def _update_glyph_map_defs(self, glyph_map_new):
        """
        Emit definitions for not-yet-defined glyphs, and record them as having
        been defined.
        """
        writer = self.writer
        if glyph_map_new:
            writer.start('defs')
            for char_id, (vertices, codes) in glyph_map_new.items():
                char_id = self._adjust_char_id(char_id)
                # x64 to go back to FreeType's internal (integral) units.
                path_data = self._convert_path(
                    Path(vertices * 64, codes), simplify=False)
                writer.element(
                    'path', id=char_id, d=path_data,
                    transform=generate_transform([('scale', (1 / 64,))]))
            writer.end('defs')
            self._glyph_map.update(glyph_map_new)

    def _adjust_char_id(self, char_id):
        return char_id.replace("%20", "_")

    def _draw_text_as_path(self, gc, x, y, s, prop, angle, ismath, mtext=None):
        """
        Draw the text by converting them to paths using the textpath module.

        Parameters
        ----------
        s : str
            text to be converted
        prop : `matplotlib.font_manager.FontProperties`
            font property
        ismath : bool
            If True, use mathtext parser. If "TeX", use *usetex* mode.
        """
        writer = self.writer

        writer.comment(s)

        glyph_map = self._glyph_map

        text2path = self._text2path
        color = rgb2hex(gc.get_rgb())
        fontsize = prop.get_size_in_points()

        style = {}
        if color != '#000000':
            style['fill'] = color
        alpha = gc.get_alpha() if gc.get_forced_alpha() else gc.get_rgb()[3]
        if alpha != 1:
            style['opacity'] = short_float_fmt(alpha)
        font_scale = fontsize / text2path.FONT_SCALE
        attrib = {
            'style': generate_css(style),
            'transform': generate_transform([
                ('translate', (x, y)),
                ('rotate', (-angle,)),
                ('scale', (font_scale, -font_scale))]),
        }
        writer.start('g', attrib=attrib)

        if not ismath:
            font = text2path._get_font(prop)
            _glyphs = text2path.get_glyphs_with_font(
                font, s, glyph_map=glyph_map, return_new_glyphs_only=True)
            glyph_info, glyph_map_new, rects = _glyphs
            self._update_glyph_map_defs(glyph_map_new)

            for glyph_id, xposition, yposition, scale in glyph_info:
                attrib = {'xlink:href': '#%s' % glyph_id}
                if xposition != 0.0:
                    attrib['x'] = short_float_fmt(xposition)
                if yposition != 0.0:
                    attrib['y'] = short_float_fmt(yposition)
                writer.element('use', attrib=attrib)

        else:
            if ismath == "TeX":
                _glyphs = text2path.get_glyphs_tex(
                    prop, s, glyph_map=glyph_map, return_new_glyphs_only=True)
            else:
                _glyphs = text2path.get_glyphs_mathtext(
                    prop, s, glyph_map=glyph_map, return_new_glyphs_only=True)
            glyph_info, glyph_map_new, rects = _glyphs
            self._update_glyph_map_defs(glyph_map_new)

            for char_id, xposition, yposition, scale in glyph_info:
                char_id = self._adjust_char_id(char_id)
                writer.element(
                    'use',
                    transform=generate_transform([
                        ('translate', (xposition, yposition)),
                        ('scale', (scale,)),
                        ]),
                    attrib={'xlink:href': '#%s' % char_id})

            for verts, codes in rects:
                path = Path(verts, codes)
                path_data = self._convert_path(path, simplify=False)
                writer.element('path', d=path_data)

        writer.end('g')

    def _draw_text_as_text(self, gc, x, y, s, prop, angle, ismath, mtext=None):
        writer = self.writer

        color = rgb2hex(gc.get_rgb())
        style = {}
        if color != '#000000':
            style['fill'] = color

        alpha = gc.get_alpha() if gc.get_forced_alpha() else gc.get_rgb()[3]
        if alpha != 1:
            style['opacity'] = short_float_fmt(alpha)

        if not ismath:
            font = self._get_font(prop)
            font.set_text(s, 0.0, flags=LOAD_NO_HINTING)

            attrib = {}
            style['font-family'] = str(font.family_name)
            style['font-weight'] = str(prop.get_weight()).lower()
            style['font-stretch'] = str(prop.get_stretch()).lower()
            style['font-style'] = prop.get_style().lower()
            # Must add "px" to workaround a Firefox bug
            style['font-size'] = short_float_fmt(prop.get_size()) + 'px'
            attrib['style'] = generate_css(style)

            if mtext and (angle == 0 or mtext.get_rotation_mode() == "anchor"):
                # If text anchoring can be supported, get the original
                # coordinates and add alignment information.

                # Get anchor coordinates.
                transform = mtext.get_transform()
                ax, ay = transform.transform(mtext.get_unitless_position())
                ay = self.height - ay

                # Don't do vertical anchor alignment. Most applications do not
                # support 'alignment-baseline' yet. Apply the vertical layout
                # to the anchor point manually for now.
                angle_rad = np.deg2rad(angle)
                dir_vert = np.array([np.sin(angle_rad), np.cos(angle_rad)])
                v_offset = np.dot(dir_vert, [(x - ax), (y - ay)])
                ax = ax + v_offset * dir_vert[0]
                ay = ay + v_offset * dir_vert[1]

                ha_mpl_to_svg = {'left': 'start', 'right': 'end',
                                 'center': 'middle'}
                style['text-anchor'] = ha_mpl_to_svg[mtext.get_ha()]

                attrib['x'] = short_float_fmt(ax)
                attrib['y'] = short_float_fmt(ay)
                attrib['style'] = generate_css(style)
                attrib['transform'] = "rotate(%s, %s, %s)" % (
                    short_float_fmt(-angle),
                    short_float_fmt(ax),
                    short_float_fmt(ay))
                writer.element('text', s, attrib=attrib)
            else:
                attrib['transform'] = generate_transform([
                    ('translate', (x, y)),
                    ('rotate', (-angle,))])

                writer.element('text', s, attrib=attrib)

        else:
            writer.comment(s)

            width, height, descent, glyphs, rects = \
                self._text2path.mathtext_parser.parse(s, 72, prop)

            # Apply attributes to 'g', not 'text', because we likely have some
            # rectangles as well with the same style and transformation.
            writer.start('g',
                         style=generate_css(style),
                         transform=generate_transform([
                             ('translate', (x, y)),
                             ('rotate', (-angle,))]),
                         )

            writer.start('text')

            # Sort the characters by font, and output one tspan for each.
            spans = OrderedDict()
            for font, fontsize, thetext, new_x, new_y in glyphs:
                style = generate_css({
                    'font-size': short_float_fmt(fontsize) + 'px',
                    'font-family': font.family_name,
                    'font-style': font.style_name.lower(),
                    'font-weight': font.style_name.lower()})
                if thetext == 32:
                    thetext = 0xa0  # non-breaking space
                spans.setdefault(style, []).append((new_x, -new_y, thetext))

            for style, chars in spans.items():
                chars.sort()

                if len({y for x, y, t in chars}) == 1:  # Are all y's the same?
                    ys = str(chars[0][1])
                else:
                    ys = ' '.join(str(c[1]) for c in chars)

                attrib = {
                    'style': style,
                    'x': ' '.join(short_float_fmt(c[0]) for c in chars),
                    'y': ys
                    }

                writer.element(
                    'tspan',
                    ''.join(chr(c[2]) for c in chars),
                    attrib=attrib)

            writer.end('text')

            for x, y, width, height in rects:
                writer.element(
                    'rect',
                    x=short_float_fmt(x),
                    y=short_float_fmt(-y-1),
                    width=short_float_fmt(width),
                    height=short_float_fmt(height)
                    )

            writer.end('g')

    @_api.delete_parameter("3.3", "ismath")
    def draw_tex(self, gc, x, y, s, prop, angle, ismath='TeX!', mtext=None):
        # docstring inherited
        self._draw_text_as_path(gc, x, y, s, prop, angle, ismath="TeX")

    def draw_text(self, gc, x, y, s, prop, angle, ismath=False, mtext=None):
        # docstring inherited

        clipid = self._get_clip(gc)
        if clipid is not None:
            # Cannot apply clip-path directly to the text, because
            # is has a transformation
            self.writer.start(
                'g', attrib={'clip-path': 'url(#%s)' % clipid})

        if gc.get_url() is not None:
            self.writer.start('a', {'xlink:href': gc.get_url()})

        if mpl.rcParams['svg.fonttype'] == 'path':
            self._draw_text_as_path(gc, x, y, s, prop, angle, ismath, mtext)
        else:
            self._draw_text_as_text(gc, x, y, s, prop, angle, ismath, mtext)

        if gc.get_url() is not None:
            self.writer.end('a')

        if clipid is not None:
            self.writer.end('g')

    def flipy(self):
        # docstring inherited
        return True

    def get_canvas_width_height(self):
        # docstring inherited
        return self.width, self.height

    def get_text_width_height_descent(self, s, prop, ismath):
        # docstring inherited
        return self._text2path.get_text_width_height_descent(s, prop, ismath)


class FigureCanvasSVG(FigureCanvasBase):
    filetypes = {'svg': 'Scalable Vector Graphics',
                 'svgz': 'Scalable Vector Graphics'}

    fixed_dpi = 72

    def print_svg(self, filename, *args, **kwargs):
        """
        Parameters
        ----------
        filename : str or path-like or file-like
            Output target; if a string, a file will be opened for writing.

        metadata : dict[str, Any], optional
            Metadata in the SVG file defined as key-value pairs of strings,
            datetimes, or lists of strings, e.g., ``{'Creator': 'My software',
            'Contributor': ['Me', 'My Friend'], 'Title': 'Awesome'}``.

            The standard keys and their value types are:

            * *str*: ``'Coverage'``, ``'Description'``, ``'Format'``,
              ``'Identifier'``, ``'Language'``, ``'Relation'``, ``'Source'``,
              ``'Title'``, and ``'Type'``.
            * *str* or *list of str*: ``'Contributor'``, ``'Creator'``,
              ``'Keywords'``, ``'Publisher'``, and ``'Rights'``.
            * *str*, *date*, *datetime*, or *tuple* of same: ``'Date'``. If a
              non-*str*, then it will be formatted as ISO 8601.

            Values have been predefined for ``'Creator'``, ``'Date'``,
            ``'Format'``, and ``'Type'``. They can be removed by setting them
            to `None`.

            Information is encoded as `Dublin Core Metadata`__.

            .. _DC: https://www.dublincore.org/specifications/dublin-core/

            __ DC_
        """
        with cbook.open_file_cm(filename, "w", encoding="utf-8") as fh:

            filename = getattr(fh, 'name', '')
            if not isinstance(filename, str):
                filename = ''

            if cbook.file_requires_unicode(fh):
                detach = False
            else:
                fh = TextIOWrapper(fh, 'utf-8')
                detach = True

            self._print_svg(filename, fh, **kwargs)

            # Detach underlying stream from wrapper so that it remains open in
            # the caller.
            if detach:
                fh.detach()

    def print_svgz(self, filename, *args, **kwargs):
        with cbook.open_file_cm(filename, "wb") as fh, \
                gzip.GzipFile(mode='w', fileobj=fh) as gzipwriter:
            return self.print_svg(gzipwriter)

    @_check_savefig_extra_args
    @_api.delete_parameter("3.4", "dpi")
    def _print_svg(self, filename, fh, *, dpi=None, bbox_inches_restore=None,
                   metadata=None):
        if dpi is None:  # always use this branch after deprecation elapses.
            dpi = self.figure.get_dpi()
        self.figure.set_dpi(72)
        width, height = self.figure.get_size_inches()
        w, h = width * 72, height * 72

        renderer = MixedModeRenderer(
            self.figure, width, height, dpi,
            RendererSVG(w, h, fh, filename, dpi, metadata=metadata),
            bbox_inches_restore=bbox_inches_restore)

        self.figure.draw(renderer)
        renderer.finalize()

    def get_default_filetype(self):
        return 'svg'

    def draw(self):
        _no_output_draw(self.figure)
        return super().draw()


FigureManagerSVG = FigureManagerBase


svgProlog = """\
<?xml version="1.0" encoding="utf-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
"""


@_Backend.export
class _BackendSVG(_Backend):
    FigureCanvas = FigureCanvasSVG
