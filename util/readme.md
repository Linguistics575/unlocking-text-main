# Python utilities to Scan From PDF

These Python scripts will operate against PDF documents containing text to be scanned. They both rely on the PyPDF Python library, which is currently not installed on Patas. They will run on your own system after installing the PyPDF library:

```sudo apt-get install python-pypdf```
 

## PDF Text Extractor
Many PDF documents in the collection include existing text from the first time that the document was scanned. This is particuarly true of the documents scanned by the Internet Archives, and in a few of the Google scanned documents. The quality of this text varies, but provides a handy benchmark against further scans.

In general, if a PDF file includes scanned text already, you will be able to select the text when displaying the contents of the file. In any case, the program will detect if there is no text in the file when run.

To run the Text Extractor, you will need to invoke the python script:
```python PDFTextExtractor.py [PDF File Name]```

This will create a new text file with the same name as the PDF file, adding "_text.txt" to the end. It will contain a list of pages in which in finds text and the text itself.

It is possible to change the text added to the name with the -x option. Also, by default the script starts the pages at 0. You can change this with the -p option. Therefore,
```python PDFTextExtractor.py -x _archives_text -p 1 MyPDFFile.pdf```

will create a file "MyPDFFile_archives_text.txt" containing any text found, with the first page numbered 1, and continuing from there.

## PDF JPEG Extractor
In general, all PDF documents based on images of books or the like will contain one image per page. This script assumes this to be the case, and generates separate JPEG files for each page. These images will be easier to feed into OCR systems such as Tesseract.

To run the script against the PDF file:
```python PDFJpegExtractor.py [PDF File Name]```

This will store a separate JPEG file for each page of the document in a directory in the same location as the PDF file.  Additional controls are:

```-r [Resolution]```, which will set the resolution of the output file to the desired size, in pixels per inch. The default is 250. Depending on the relative size of the text in the original images, you might want to raise this as high as 800 PPI, though doing so will increase the size of each image. Setting resolution too large could create problems with the scan. It may be useful to experiment with different resolutions on a few pages before committing to scan the entire document.

```-p [Page Number]```, sets the start page number when outputting the page filenames. This could be useful if you know that a certain number of pages of the input PDF are devoted to the cover and preface, letting the page numbers match the numbering of the document. This number may be negative.

For example, calling the script as:

```python PDFJpegExtractor.py -r 600 -p '-10' MyPDFFile.pdf```

will result in all pages of the PDF file being stored in a directory called "MyPDFFile", numbered starting at -10, presumably because there is a 10 page prefact before page 1 of the actual document.
