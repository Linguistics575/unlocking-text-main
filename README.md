# Unlocking Text from its Image
holds tools and code for the _Unlocking Text from its Image_ project.
See [575_OCR](https://github.com/Linguistics575/575_OCR) for a git repository containing related data and output files.  This repository contains code only.
---
The purpose of the tools in this repository is to reliably "unlock" the text from image data, thus making electronic text available to technologies such as Named Entity Recognition, automated TEI markup, and other automated means for processing text.  We provide tools to extract textual portions from images by means of optical character recognition (OCR) on typewritten texts, and handwriting recognition on handwritten texts.  These tools were originally intended for use in The Emma Andrews Diary project, but they may be used on virtually any image containing textual data (albeit with varying degrees of success.  See [our wiki](https://github.com/Linguistics575/unlocking-text-main/wiki/Guidelines-for-Image-Conditions-that-Affect-Handwriting-Recognition-Performance) for guidelines for use.) 

This repository contains 4 principal tools, each with its own User Guide and Technical Documentation in its own directory:
- `azure/`: contains a script to run an image through the MS Azure Handwriting Recognition API and related resources.  [User Guide](https://github.com/Linguistics575/unlocking-text-main/tree/master/azure)  [Technical Documentation](https://github.com/Linguistics575/unlocking-text-main/tree/master/azure#technical-documentation)
- `evaluation/`: contains a script to calculate the Word Error Rate (WER) of an OCRed text by comparing it to a human transcription. [User Guide](https://github.com/Linguistics575/unlocking-text-main/tree/master/evaluation/WER) [Technical Documentation](https://github.com/Linguistics575/unlocking-text-main/tree/master/evaluation/WER#technical-documentation)
- `image_processing/`: contains an admittedly rough _jupyter notebook_ based utility to binarize an image. [User Guide](https://github.com/Linguistics575/unlocking-text-main/tree/master/image_processing#user-guide) [Technical Documentation](https://github.com/Linguistics575/unlocking-text-main/tree/master/image_processing#technical-documentation)
- `util/`: contains two Python scripts designed to extract text or images from PDF files of books or similar documents. [User Guide](https://github.com/Linguistics575/unlocking-text-main/tree/master/util#user-guide) [Technical Documentation](https://github.com/Linguistics575/unlocking-text-main/tree/master/util#technical-documentation). Under this directory, in `util/scripts/` are the scripts for Automated OCR Scanning.  [User Guide](https://github.com/Linguistics575/unlocking-text-main/tree/master/util/scripts#user-guide) [Technical Documentation](https://github.com/Linguistics575/unlocking-text-main/tree/master/util/scripts#technical-documentation). 

See the READMEs/User Guides in the corresponding directories for more information.

See also [our wiki](https://github.com/Linguistics575/unlocking-text-main/wiki/Guidelines-for-Image-Conditions-that-Affect-Handwriting-Recognition-Performance) for information with respect to the image conditions we have discovered to affect recognition performance.

Note: Each tool is provided with its own individual license, which you will find in the readme of its respective directory.

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
