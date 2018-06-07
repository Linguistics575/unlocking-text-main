## ABBYY FineReader Support

ABBYY FineReader is a commercial OCR system available either for [Windows](https://www.abbyy.com/en-us/finereader/) or for [Macintosh](https://www.abbyy.com/en-us/finereader/pro-for-mac/). It has proven extremely effective at scanning print documents. The main downsides to the product are:

* It is a commercial product, and needs to be licensed (at cost) from the manufacturer ([ABBYY](https://www.abbyy.com))
* It is not easily automated, making most scanning operations time-consuming.
* It is only available on Windows or Macintosh. A development toolkit, [FineReader Engine](https://www.abbyy.com/en-us/ocr-sdk/) is available on Linux, as well as Windows and Macintosh, but would require development in C++.

Apart from those concerns, it is a good tool for extracting text from files. Anyone using it should consult the downloadable [documentation](http://spt.abbyy.com/fr12guide_en.pdf), but the following features are worth mentioning.

* It can scan PDF documents directly. Unlike Tesseract, which needs to work on image files, FineReader can process a PDF file. Be forewarned that scanning a 500 page document will still take a long time to process and will strain most systems.
* It provides a number of tools to preprocess images, letting you deskew a file (i.e. make the lines less slanted) or adjust the distortion caused by an image being photographed at an angle.
* It is possible to create document templates, directing the scanning software to scan columns or only to ignore parts of the page that typically contain images or decoration. While handy, this will only work on a page-by-page basis or for pages with standard layouts.

Some sample layouts are available in the [`util/finereader/eg_gazette/`](https://github.com/Linguistics575/unlocking-text-main/tree/master/util/finereader/eg_gazette) directory.

```
FineReader (c) ABBYY
```