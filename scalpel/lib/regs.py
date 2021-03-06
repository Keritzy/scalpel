#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: define regs
  Created: 03/19/17
"""

from . import data

VULNUS_START = data.VULNUS_START
VULNUS_END = data.VULNUS_END

WRAPER_START = data.WRAPER_START
WRAPER_END = data.WRAPER_END

EXTRACT_TAG_PATTERN = "(" + VULNUS_START + '(.*)' + VULNUS_END + ")"
EXTRACT_RSP_PATTERN = "(" + WRAPER_START + '(.*)' + WRAPER_END + ")"

#
# Tag Parser Regs
#
####################################################################################
_PARSE_TAG = "(\(([a-zA-Z0-9_]*)\))"
_PARSE_PARAMS = "(\{(([0-9]+)(,([ ]+)?([0-9]+)?)?)\})"
_SUFFIX = "(\:([a-zA-Z0-9]+))"
####################################################################################

TAG_PATTERN = "(" + '|'.join(data.TAG_LIST) + ")" + _PARSE_TAG + '?' + _PARSE_PARAMS + '?' +\
    _SUFFIX + "?"
TEMPLATE_PATTERN = "((" + VULNUS_START + ")" + TAG_PATTERN + "(" + VULNUS_END + "))"


