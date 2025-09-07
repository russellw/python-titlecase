#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Vendorable titlecase function - extracted from python-titlecase
Original Perl version by: John Gruber http://daringfireball.net/ 10 May 2008
Python version by Stuart Colville http://muffinresearch.co.uk
License: http://www.opensource.org/licenses/mit-license.php
"""

import string

try:
    import regex
except ImportError:
    import re as regex
    REGEX_AVAILABLE = False
else:
    REGEX_AVAILABLE = True

__version__ = '2.4.1'

SMALL = r'a|an|and|as|at|but|by|en|for|if|in|of|on|or|the|to|v\.?|via|vs\.?'
PUNCT = r"""!""#$%&''()*+,\-–‒—―./:;?@[\\\]_`{|}~"""

SMALL_WORDS = regex.compile(r'^(%s)$' % SMALL, regex.I)

SMALL_FIRST = regex.compile(r'^([%s]*)(%s)\b' % (PUNCT, SMALL), regex.I)
SMALL_LAST = regex.compile(r'\b(%s)[%s]?$' % (SMALL, PUNCT), regex.I)
SUBPHRASE = regex.compile(r'([:.;?!\-–‒—―][ ])(%s)' % SMALL)
MAC_MC = regex.compile(r"^([Mm]c|MC)(\w.+)")
MR_MRS_MS_DR = regex.compile(r"^((m((rs?)|s))|Dr)$", regex.I)

if REGEX_AVAILABLE:
    INLINE_PERIOD = regex.compile(r'[\p{Letter}][.][\p{Letter}]', regex.I)
    UC_ELSEWHERE = regex.compile(r'[%s]*?[\p{Letter}]+[\p{Uppercase_Letter}]+?' % PUNCT)
    CAPFIRST = regex.compile(r"^[%s]*?([\p{Letter}])" % PUNCT)
    APOS_SECOND = regex.compile(r"^[dol]{1}['']{1}[\p{Letter}]+(?:['s]{2})?$", regex.I)
    UC_INITIALS = regex.compile(r"^(?:[\p{Uppercase_Letter}]{1}\.{1}|[\p{Uppercase_Letter}]{1}\.{1}[\p{Uppercase_Letter}]{1})+$")
else:
    INLINE_PERIOD = regex.compile(r'[\w][.][\w]', regex.I)
    UC_ELSEWHERE = regex.compile(r'[%s]*?[a-zA-Z]+[A-Z]+?' % PUNCT)
    CAPFIRST = regex.compile(r"^[%s]*?([\w])" % PUNCT)
    APOS_SECOND = regex.compile(r"^[dol][''][\w]+(?:['s]{2})?$", regex.I)
    UC_INITIALS = regex.compile(r"^(?:[A-Z]\.|[A-Z]\.[A-Z])+$")




def set_small_word_list(small=SMALL):
    global SMALL_WORDS
    global SMALL_FIRST
    global SMALL_LAST
    global SUBPHRASE
    SMALL_WORDS = regex.compile(r'^(%s)$' % small, regex.I)
    SMALL_FIRST = regex.compile(r'^([%s]*)(%s)\b' % (PUNCT, small), regex.I)
    SMALL_LAST = regex.compile(r'\b(%s)[%s]?$' % (small, PUNCT), regex.I)
    SUBPHRASE = regex.compile(r'([:.;?!][ ])(%s)' % small)


def titlecase(text, small_first_last=True, preserve_blank_lines=False, normalise_space_characters=False):
    """
    :param text: Titlecases input text
    :param small_first_last: Capitalize small words (e.g. 'A') at the beginning; disabled when recursing
    :param preserve_blank_lines: Preserve blank lines in the output
    :param normalise_space_characters: Convert all original spaces to normal space characters
    :type text: str
    :type small_first_last: bool
    :type preserve_blank_lines: bool
    :type normalise_space_characters: bool

    This filter changes all words to Title Caps, and attempts to be clever
    about *un*capitalizing SMALL words like a/an/the in the input.

    The list of "SMALL words" which are not capped comes from
    the New York Times Manual of Style, plus 'vs' and 'v'.

    """
    if preserve_blank_lines:
        lines = regex.split('[\r\n]', text)
    else:
        lines = regex.split('[\r\n]+', text)
    processed = []
    for line in lines:
        all_caps = line.upper() == line
        split_line = regex.split(r'(\s)', line)
        words = split_line[::2]
        spaces = split_line[1::2]
        tc_line = []
        for word in words:
            if all_caps:
                if UC_INITIALS.match(word):
                    tc_line.append(word)
                    continue

            if APOS_SECOND.match(word):
                if len(word[0]) == 1 and word[0] not in 'aeiouAEIOU':
                    word = word[0].lower() + word[1] + word[2].upper() + word[3:]
                else:
                    word = word[0].upper() + word[1] + word[2].upper() + word[3:]
                tc_line.append(word)
                continue

            match = MAC_MC.match(word)
            if match:
                tc_line.append("%s%s" % (match.group(1).capitalize(),
                                         titlecase(match.group(2), True)))
                continue

            match = MR_MRS_MS_DR.match(word)
            if match:
                word = word[0].upper() + word[1:]
                tc_line.append(word)
                continue

            if INLINE_PERIOD.search(word) or (not all_caps and UC_ELSEWHERE.match(word)):
                tc_line.append(word)
                continue
            if SMALL_WORDS.match(word):
                tc_line.append(word.lower())
                continue

            if "/" in word and "//" not in word:
                slashed = map(
                    lambda t: titlecase(t, False),
                    word.split('/')
                )
                tc_line.append("/".join(slashed))
                continue

            if '-' in word:
                hyphenated = map(
                    lambda t: titlecase(t, False),
                    word.split('-')
                )
                tc_line.append("-".join(hyphenated))
                continue

            if all_caps:
                word = word.lower()


            CONSONANTS = ''.join(set(string.ascii_lowercase)
                                 - {'a', 'e', 'i', 'o', 'u', 'y'})
            is_all_consonants = regex.search(r'\A[' + CONSONANTS + r']+\Z', word,
                                             flags=regex.IGNORECASE)
            if is_all_consonants and len(word) > 2:
                tc_line.append(word.upper())
                continue

            tc_line.append(CAPFIRST.sub(lambda m: m.group(0).upper(), word))

        if small_first_last and tc_line:
            tc_line[0] = SMALL_FIRST.sub(lambda m: '%s%s' % (
                m.group(1),
                m.group(2).capitalize()
            ), tc_line[0])

            tc_line[-1] = SMALL_LAST.sub(
                lambda m: m.group(0).capitalize(), tc_line[-1]
            )

        if normalise_space_characters:
            result = " ".join(tc_line)
        else:
            line_to_be_joined = tc_line + spaces
            line_to_be_joined[::2] = tc_line
            line_to_be_joined[1::2] = spaces
            result = "".join(line_to_be_joined)

        result = SUBPHRASE.sub(lambda m: '%s%s' % (
            m.group(1),
            m.group(2).capitalize()
        ), result)

        processed.append(result)

    result = "\n".join(processed)
    return result


