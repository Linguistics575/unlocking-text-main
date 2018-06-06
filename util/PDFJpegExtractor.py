#!/bin/python3
import PyPDF2 as pdf
import os
import argparse
import sys
import datetime

from wand.image import Image

# Extract each page of the JPG files entered as a directory of JPG image files
# The files to be extracted can be entered as a list. The output will appear
# in directories identically named to the file (minus the ".pdf" extension.
#
# Resolution defaults to 250 and may be modified with the "-r" command line option.
# In general, resolution below 100 will not be useful. Of course, the JPG file sizes
# will increase with the resolution. In general, a resolution of 250 to 400 seems to
# be readable for most of the PDF files in the system. Some continue to have problems,
# particularly the Egyptian Gazettes and some of the Baedeckers.

argparser = argparse.ArgumentParser(description='Convert PDF pages to JPG files')
argparser.add_argument('filename', metavar='F', nargs='+', help='PDF File')
argparser.add_argument('-r', type=int, default=250, help='Image resolution (at least 100, 250+ recommended)')
argparser.add_argument('-p', type=int, default=0, help='Start page number (default is 0)')
argparser.add_argument('-s', type=int, help='Start page of range')
argparser.add_argument('-z', type=int, help='End page of range')

args = argparser.parse_args()

if args.s:
    start_pg = args.s - args.p
else:
    start_pg = 0

for fname in args.filename:
    pdfFile = open(fname, 'rb')
    pdfreader = pdf.PdfFileReader(pdfFile)

    endidx = fname.rfind('.pdf')
    dirname = fname[0:endidx]

    if not os.path.exists(dirname):
        os.makedirs(dirname)

    logFile = open(dirname + '.log', 'w')

    sys.stdout.write('%s, %d pages\n' % (fname, pdfreader.numPages))
    logFile.write('Reading file "%s", %d pages, resolution:%d,  %s\n' % (fname, pdfreader.numPages, args.r, datetime.datetime.now().strftime("%I:%M%p, %B %d, %Y")))

    if args.z:
        end_pg = min(args.z-args.p, pdfreader.numPages-1)
    else:
        end_pg = pdfreader.numPages-1

    if start_pg > end_pg:
        sys.stderr.write('ERROR: range %d to %d not in file "%s"\n' % (args.s, args.z, fname))
        logFile.write('ERROR: range %d to %d not in file "%s"\n' % (args.s, args.z, fname))
        logFile.flush()
        break

    for pg in range(start_pg, end_pg+1):
        with Image(filename='%s[%d]' % (fname, pg), resolution=args.r) as img:
            img.save(filename='%s/page%d.jpg' % (dirname, (pg+args.p)))
            logFile.write('page %d - w:%d, h:%d\n' % (pg+args.p, img.width, img.height))
        sys.stdout.write('%d ' % (pg + args.p))
        sys.stdout.flush()
    logFile.flush()
