## _Jupyter Notebook_ based Image Binarizer.
This is a utility to binarize an image using [adaptive thresholding](http://scikit-image.org/docs/0.12.x/auto_examples/segmentation/plot_threshold_adaptive.html).  The idea is to find small local darkness thresholds over which everything is foreground (text) in our case, and under which everything is background.

The utility uses a [Jupyter Notebook](http://jupyter.org/), an "open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text."

### User Guide
1.  Activate the azure envrionment on a command line terminal (see [installation instructions](https://github.com/Linguistics575/unlocking-text-main/tree/master/azure#installation-instructions) for the Azure Wrapper for a refresher on this.)
2.  cd into the `image processing` directory.  For example, if you're still in the `azure` directory, you would type `cd ../image_processing/` and hit `enter`
3.  Type `jupyter notebook binarizer.ipynb` and hit `enter`.  You should now see the jupyter notebook open in your default web browser.
4.  The remainder of the instructions appear within the notebook itself.  Whenever instructions say to "run a cell," this can be accomplished by clicking within the cell and hitting `ctrl+enter`, or by clicking "cell" on the menubar and then "run cells" on the dropdown.  This is a rough-and-ready utility that lacks of a beautiful front end.  
5.  When you are finished, hit `ctrl+C` from the terminal window to shut down the notebook.

### Technical Documentation
Not much to it, really.  It calls `filters.threshold_sauvola` from `scikit-image` and passes in the parameters set by the widget.