## Python utilities to Scan From PDF
The Python scripts contained directly under this directory are designed to work against PDF files containing document images, such as the travel journals and Thomas Cook travel guides in the data repository.

Some of these files already have an initial text embedded in the PDF. This is particularly true of any file scanned by the [Internet Archives](https://archive.org/). The PDF Text Extractor script will create a transcript of the text from the PDF.

All of the PDF files in the repository consist of one image per page. The PDF JPEG Extractor script will create a directory containing a single JPEG image per page of the PDF document. This is useful for running the OCR Scanning process. (See the [/scripts](https://github.com/Linguistics575/unlocking-text-main/tree/master/util/scripts) directory under this one).

### User Guide
#### PDF Text Extractor
Intended to extract existing text transcripts of OCR scans already in the PDF document. Not all documents will contain text transcripts, and those that do may not be of the best quality, but where they exist they provide a good benchmark for scanned text.

To run the Text Extractor, you will need to invoke the python script:

```$ python PDFTextExtractor.py [PDF File Name]```

This will create a new text file with the same name as the PDF file, adding "_text.txt" to the end. It will contain a list of pages in which in finds text and the text itself.

It is possible to change the text added to the name with the -x option. Also, by default the script starts the pages at 0. You can change this with the -p option. Therefore,

```$ python PDFTextExtractor.py -x _archives_text -p 1 MyPDFFile.pdf```

will create a file "MyPDFFile_archives_text.txt" containing any text found, with the first page numbered 1, and continuing from there.

#### PDF JPEG Extractor
In general, all PDF documents based on images of books or the like will contain one image per page.

To run the script against the PDF file:

```$ python PDFJpegExtractor.py [PDF File Name]```

This will store a separate JPEG file for each page of the document in a directory in the same location as the PDF file.  Additional controls are:

```-r [Resolution]```, which will set the resolution of the output file to the desired size, in pixels per inch.

The default resolution is 250. Depending on the relative size of the text in the original images, you might want to raise this as high as 800 PPI, though doing so will increase the size of each image. Setting resolution too large could create problems with the scan. It may be useful to experiment with different resolutions on a few pages before committing to scan the entire document.

```-p [Page Number]```, sets the start page number of the first page.

This could be useful if you know that a certain number of pages of the input PDF are devoted to the cover and preface, letting the page numbers match the numbering of the document. This number may be negative.

For example, calling the script as:

```python PDFJpegExtractor.py -r 600 -p '-10' MyPDFFile.pdf```

will result in all pages of the PDF file being stored in a directory called "MyPDFFile", numbered starting at -10, presumably because there is a 10 page prefact before page 1 of the actual document.

Because resolution can be tricky to determine, it is helpful to experiment with a few pages to find the best resolution values. To extract only a few pages of the text, there are two command line arguments that specify the start and stop pages of a range to be extracted:

```-s [Start Page]```

```-z [End Page]```

These page numbers are adjusted for the -p value set for pagination.

For example, if you think that the first two pages of the preface, at pages -3 to -2, (in a document starting at page -7 for the cover) are good examples of images on which to test resolution, you could try the following:

```python PDFJpegExtractor.py -p -7 -s -3 -z -2 -r 300 MyPDFFile.pdf```

Will create two pages at a 300 Pixel Per Inch resolution.

### Technical Documentation
These scripts were created to wrap the handy ability of PyPDF2 to iterate over pages of a PDF file and extract its components parts. These are kept separate from the OCR Scanning scripts because they are chiefly designed to be run on ones own machine, and are not easily run on the UW Linguistics Department's server (Patas).

The Python scripts were written using Pyhon3, but should work with either version of Python. Note that the PyPDF2 library will have to be installed for the version of Python used.

To install PyPDF2 on your machine:

On Windows: Download the [PyPDF Installer, pyPdf-1.13.win32.exe ](http://pybrary.net/pyPdf/pyPdf-1.13.win32.exe) for Windows and run it.

On Macintosh, in a terminal window:
```sudo pip install pypdf2```
 
On Linux, in a terminal window:
```sudo apt-get install python-pypdf```

#### PDF Text Extractor
It is not always obvious whether a PDF file already contains embedded text transcripts. In general, if a PDF file includes scanned text already, you will be able to select the text when displaying the contents of the file. In any case, the program will detect if there is no text in the file when run.

#### PDF JPEG Extractor
As with the Text Extractor, the JPEG Extractor makes use of PyPDF2 to iterate over pages and extract the images. The ability to experimentally generate only a few pages makes it easier to experiment with different resolution settings and to see how easily the document might be scanned in general.

The script will generate a directory in the same location as the PDF document, and with the same name, excluding the "*.pdf" extension. It will also generate a log file, listing each file extracted, confirming each page and the size of the image, and noting any errors or warnings encountered.