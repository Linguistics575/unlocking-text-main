# Unlocking Text from its Image
holds tools and code for the _Unlocking Text from its Image_ project.
See [575_OCR](https://github.com/Linguistics575/575_OCR) for a git respository containing related data and ouput files.  This repository contains code only.
---
The purpose of the tools in this repository us to relibably "unlock" the text from image data, thus making electronic text availble to technologies such as Named Entity Recognition, automated TEI markup, and other automated means for processing text.  We provide tools to extract textual portions from images by means of optical character regognition (OCR) on typewritten texts, and handwriting recognition on handwritten texts.  These tools were originally intended for use in The Emma Andrews Diary project, but they may be used on virtually any image containing textual data (abeit with varying degrees of success.  See XXXX for guidelines for use.) 

This repository contains 4 principal tools, each with its own User Guide and Technical Documentation, in its own direcotry:
- `azure/`: contains a script to run an image through the MS Azure Handwriting Recognition API and related resources.  [User Guide](https://github.com/Linguistics575/unlocking-text-main/tree/master/azure)  [Technical Documentation](https://github.com/Linguistics575/unlocking-text-main/tree/master/azure#technical-documentation)
- `evaluation/`: contains a script to calcualte the Word Error Rate (WER) of an OCRed text by compariing it to a human transcription. [User Guide](https://github.com/Linguistics575/unlocking-text-main/tree/master/evaluation/WER) [Technical Documentation](https://github.com/Linguistics575/unlocking-text-main/tree/master/evaluation/WER#technical-documentation)
- `image_processing/`: contains an admittedly rough _jupyter notebook_ based utility to binarize an image.
- `ERIC's Utilities HERE`: contains stuff that Eric will write a sentene about here.

See the READMEs/User Guides in the corresponding directories for more information.


