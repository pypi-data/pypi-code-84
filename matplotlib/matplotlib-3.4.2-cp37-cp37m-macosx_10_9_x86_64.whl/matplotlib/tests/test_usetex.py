import numpy as np
import pytest

import matplotlib as mpl
from matplotlib.testing import _has_tex_package
from matplotlib.testing.decorators import check_figures_equal, image_comparison
import matplotlib.pyplot as plt


if not mpl.checkdep_usetex(True):
    pytestmark = pytest.mark.skip('Missing TeX of Ghostscript or dvipng')


@image_comparison(
    baseline_images=['test_usetex'],
    extensions=['pdf', 'png'],
    style="mpl20")
def test_usetex():
    mpl.rcParams['text.usetex'] = True
    fig, ax = plt.subplots()
    kwargs = {"verticalalignment": "baseline", "size": 24,
              "bbox": dict(pad=0, edgecolor="k", facecolor="none")}
    ax.text(0.2, 0.7,
            # the \LaTeX macro exercises character sizing and placement,
            # \left[ ... \right\} draw some variable-height characters,
            # \sqrt and \frac draw horizontal rules, \mathrm changes the font
            r'\LaTeX\ $\left[\int\limits_e^{2e}'
            r'\sqrt\frac{\log^3 x}{x}\,\mathrm{d}x \right\}$',
            **kwargs)
    ax.text(0.2, 0.3, "lg", **kwargs)
    ax.text(0.4, 0.3, r"$\frac{1}{2}\pi$", **kwargs)
    ax.text(0.6, 0.3, "$p^{3^A}$", **kwargs)
    ax.text(0.8, 0.3, "$p_{3_2}$", **kwargs)
    for x in {t.get_position()[0] for t in ax.texts}:
        ax.axvline(x)
    for y in {t.get_position()[1] for t in ax.texts}:
        ax.axhline(y)
    ax.set_axis_off()


@check_figures_equal()
def test_empty(fig_test, fig_ref):
    mpl.rcParams['text.usetex'] = True
    fig_test.text(.5, .5, "% a comment")


@check_figures_equal()
def test_unicode_minus(fig_test, fig_ref):
    mpl.rcParams['text.usetex'] = True
    fig_test.text(.5, .5, "$-$")
    fig_ref.text(.5, .5, "\N{MINUS SIGN}")


def test_mathdefault():
    plt.rcParams["axes.formatter.use_mathtext"] = True
    fig = plt.figure()
    fig.add_subplot().set_xlim(-1, 1)
    # Check that \mathdefault commands generated by tickers don't cause
    # problems when later switching usetex on.
    mpl.rcParams['text.usetex'] = True
    fig.canvas.draw()


@pytest.mark.parametrize("fontsize", [8, 10, 12])
def test_minus_no_descent(fontsize):
    # Test special-casing of minus descent in DviFont._height_depth_of, by
    # checking that overdrawing a 1 and a -1 results in an overall height
    # equivalent to drawing either of them separately.
    mpl.style.use("mpl20")
    mpl.rcParams['font.size'] = fontsize
    heights = {}
    fig = plt.figure()
    for vals in [(1,), (-1,), (-1, 1)]:
        fig.clf()
        for x in vals:
            fig.text(.5, .5, f"${x}$", usetex=True)
        fig.canvas.draw()
        # The following counts the number of non-fully-blank pixel rows.
        heights[vals] = ((np.array(fig.canvas.buffer_rgba())[..., 0] != 255)
                         .any(axis=1).sum())
    assert len({*heights.values()}) == 1


@pytest.mark.skipif(not _has_tex_package('xcolor'),
                    reason='xcolor is not available')
def test_usetex_xcolor():
    mpl.rcParams['text.usetex'] = True

    fig = plt.figure()
    text = fig.text(0.5, 0.5, "Some text 0123456789")
    fig.canvas.draw()

    mpl.rcParams['text.latex.preamble'] = r'\usepackage[dvipsnames]{xcolor}'
    fig = plt.figure()
    text2 = fig.text(0.5, 0.5, "Some text 0123456789")
    fig.canvas.draw()
    np.testing.assert_array_equal(text2.get_window_extent(),
                                  text.get_window_extent())


def test_textcomp_full():
    plt.rcParams["text.latex.preamble"] = r"\usepackage[full]{textcomp}"
    fig = plt.figure()
    fig.text(.5, .5, "hello, world", usetex=True)
    fig.canvas.draw()
