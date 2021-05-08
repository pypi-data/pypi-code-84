# Process ![image](<src> "title")

from typing import List

from .state_inline import StateInline
from ..token import Token
from ..common.utils import isSpace, normalizeReference


def image(state: StateInline, silent: bool):

    label = None
    href = ""
    oldPos = state.pos
    max = state.posMax

    # /* ! */
    if state.srcCharCode[state.pos] != 0x21:
        return False
    # /* [ */
    if state.pos + 1 < state.posMax and state.srcCharCode[state.pos + 1] != 0x5B:
        return False

    labelStart = state.pos + 2
    labelEnd = state.md.helpers.parseLinkLabel(state, state.pos + 1, False)

    # parser failed to find ']', so it's not a valid link
    if labelEnd < 0:
        return False

    pos = labelEnd + 1
    # /* ( */
    if pos < max and state.srcCharCode[pos] == 0x28:
        #
        # Inline link
        #

        # [link](  <href>  "title"  )
        #        ^^ skipping these spaces
        pos += 1
        while pos < max:
            code = state.srcCharCode[pos]
            if not isSpace(code) and code != 0x0A:
                break
            pos += 1

        if pos >= max:
            return False

        # [link](  <href>  "title"  )
        #          ^^^^^^ parsing link destination
        start = pos
        res = state.md.helpers.parseLinkDestination(state.src, pos, state.posMax)
        if res.ok:
            href = state.md.normalizeLink(res.str)
            if state.md.validateLink(href):
                pos = res.pos
            else:
                href = ""

        # [link](  <href>  "title"  )
        #                ^^ skipping these spaces
        start = pos
        while pos < max:
            code = state.srcCharCode[pos]
            if not isSpace(code) and code != 0x0A:
                break
            pos += 1

        # [link](  <href>  "title"  )
        #                  ^^^^^^^ parsing link title
        res = state.md.helpers.parseLinkTitle(state.src, pos, state.posMax)
        if pos < max and start != pos and res.ok:
            title = res.str
            pos = res.pos

            # [link](  <href>  "title"  )
            #                         ^^ skipping these spaces
            while pos < max:
                code = state.srcCharCode[pos]
                if not isSpace(code) and code != 0x0A:
                    break
                pos += 1
        else:
            title = ""

        # /* ) */
        if pos >= max or state.srcCharCode[pos] != 0x29:
            state.pos = oldPos
            return False

        pos += 1

    else:
        #
        # Link reference
        #
        if "references" not in state.env:
            return False

        # /* [ */
        if pos < max and state.srcCharCode[pos] == 0x5B:
            start = pos + 1
            pos = state.md.helpers.parseLinkLabel(state, pos)
            if pos >= 0:
                label = state.src[start:pos]
                pos += 1
            else:
                pos = labelEnd + 1
        else:
            pos = labelEnd + 1

        # covers label == '' and label == undefined
        # (collapsed reference link and shortcut reference link respectively)
        if not label:
            label = state.src[labelStart:labelEnd]

        label = normalizeReference(label)

        ref = state.env["references"].get(label, None)
        if not ref:
            state.pos = oldPos
            return False

        href = ref["href"]
        title = ref["title"]

    #
    # We found the end of the link, and know for a fact it's a valid link
    # so all that's left to do is to call tokenizer.
    #
    if not silent:
        content = state.src[labelStart:labelEnd]

        tokens: List[Token] = []
        state.md.inline.parse(content, state.md, state.env, tokens)

        token = state.push("image", "img", 0)
        token.attrs = {"src": href, "alt": ""}
        token.children = tokens or None
        token.content = content

        if title:
            token.attrSet("title", title)

        # note, this is not part of markdown-it JS, but is useful for renderers
        if label and state.md.options.get("store_labels", False):
            token.meta["label"] = label

    state.pos = pos
    state.posMax = max
    return True
