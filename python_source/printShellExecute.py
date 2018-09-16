# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import, unicode_literals

# ref: http://timgolden.me.uk/python/win32_how_do_i/print.html
# ref: http://docs.activestate.com/activepython/2.7/pywin32/win32api__ShellExecute_meth.html

import win32api
import sys


if __name__ == '__main__':
    pdf_file_name = sys.argv[1]
    win32api.ShellExecute(0, "print", pdf_file_name, None, ".", 0)
