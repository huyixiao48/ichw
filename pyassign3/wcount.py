#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""wcount.py: count words from an Internet file.

__author__ = "胡奕潇"
__pkuid__  = "1700011716"
__email__  = "1700011716@pku.edu.cn"

"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    import string
    tol = {}
    al = []
    trans = []
    lines = lines.lower()
    for p in string.punctuation:
        lines = lines.replace(p , "")
    """Remove all the puctuation in the text. Or one word may be 
    considered as two or more words in the split step. """
    for word in lines.split():
        if word in al:
            tol[word] += 1
        else:
            al.append(word)
            tol[word] = 1
    """Count all the words in the given text."""
    for k in tol:
        trans += [[tol[k],k]]
        trans.sort()
    """Sorted the words."""
    for i in range(topn):
        print('%-10s%-10s' % (trans[-1-i][1],trans[-1-i][0]))
    """Give the output.
    The output is a litte bit different from the teacher's given answer.
    Like for the example alice in wonderland. The word 'alice' and 'was' both
    occour 168 times, but teacher's answer showed 'alice' first while this 
    answer shows 'was' first. 
    And the number of 'she' is also different. For my answer is 238, and 
    the teacher's answer is 237.
    But I think for the first situation above it can't say me wrong.
    And for the second I don't know where it goes wrong."""
    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)