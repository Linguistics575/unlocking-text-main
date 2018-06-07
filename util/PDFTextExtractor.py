#!/bin/python3
import PyPDF2 as pdf
import argparse
import sys

# #######################################################
# Copyright (c) 2018 Jimmy Bruno, Eric Lindberg
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# #######################################################

# Python script to extract embedded text from paged PDF files.
# Files to be extracted can be listed in the command line.
# The resulting text files are output to identically named files, with "_text.txt" appended instead of ".pdf"
# The suffix being appended may be modified with the "-x" command line option.

def text_filename(filename, suffix):
    return '%s%s.txt' % (filename[0:filename.rfind('.pdf')], suffix)

argparser = argparse.ArgumentParser(description='Extract existing text pages from a PDF file')
argparser.add_argument('filename', metavar='F', nargs='+', help='PDF File')
argparser.add_argument('-x', default='_text', help='Suffix to place on *.txt file (Defaults to "_text")')
argparser.add_argument('-p', type=int, default=0, help='Start page number (default is 0)')

args = argparser.parse_args()

for fname in args.filename:
    pdfFile = open(fname, 'rb')
    outFile = open(text_filename(fname, args.x), 'w')
    pdfreader = pdf.PdfFileReader(pdfFile)

    sys.stdout.write('%s ==> %s, %d pages\n' % (fname, text_filename(fname, args.x), pdfreader.numPages))
    for pg in range(pdfreader.numPages):
        pageObj = pdfreader.getPage(pg)

        outFile.write('\n===\npg. %d\n---\n%s\n' % (pg+args.p, pageObj.extractText()))
        sys.stdout.write('%d ' % (pg+args.p))
        sys.stdout.flush()
