## Scan From PDF utility

### User Guide
The intent of the `scripts/` directory is to set up automated processes for scanning a large number of documents at once.

In general, these are intended to be run on large servers. Running these scripts on your personal machine could run out of memory or disk space if run against too many documents at once.

##### Intended Audience
In general, it is assumed that you have an account on a University of Washington server and have a passing acquaintance with Unix.

#### Running the Scripts Alone
There are some scripts that support quick scanning of documents, mainly as a means of testing the quality of scans or for running scans on a small amount of data. These scripts will require you to have python3 and tesseract installed in your environment. (see the [Technical Documentation]())
 
If you have a relatively small collection of JPEG or TIFF images (i.e. no more than a few hundred), you should be able to scan them at the command prompt with the `scan_jpg_pages.sh` or `scan_tiff_pages.sh` scripts. To invoke either of these scripts, you need to identify the directory you are going to put the resulting transcript text files in and the source directory for the images. Then, while in the `util/scripts/` directory, invoke:

```$ ./scan_jpg_pages.sh [Source Directory] [Text Directory]```

or 

```$ ./scan_tiff_pages.sh [Source Directory] [Text Directory]```

Replace `[Source Directory]` with the directory path to the directory containing the image files and `[Text Directory]` with the directory path to the place where you want to store the text file results of the scan.

###### An Example
If you have a collection of TIFF images for the pages of a document in the dorectory `/project/ling575/smith-notes`, and you have set aside a directory `/home/my_account/ling575/smith-notes-text` to store the text results, then while in the `util/script/` directory, you need to enter the command:

```$ ./scan_diff_pages.sh /projects/ling575/smith-notes /home/my_account/ling575/smith-notes-text```

##### Condor Script
These instructions assume that you have an account on a server machine with the Condor Job Scheduler (aka HTCondor) installed. An example of such a machine is the University of Washington Linguistic Department's server, Patas. Most servers in the University of Washington will have Condor available. Check with Computer Support for your department if you're not sure.

In the `scripts/` directory, there are two command files, `BATCH_SCAN_PDF.cmd` and `SCAN_JPG_DIR.cmd`. These contain the instructions for Condor to scan the specified files and to generate the text transcriptions.

It is assumed that you have a set of source documents, either in the form of PDF files or a collection of JPEG images in the form of a JPEG image for each page of the text. `BATCH_SCAN_PDF.cmd` will operate on a list of PDF files or on all PDF files in a directory, and `SCAN_JPEG_DIR.cmd` operates on all JPEG images in a single directory.

##### Running Condor to Scan PDF Files
If you have a collection of PDF files to scan, the easiest thing to do is to organize them in one directory on the server. Then set aside a directory where all of the output text files will be stored. This output will be in the form of directories with the source PDF name, with each page stored in its own text file.

Copy the `BATCH_SCAN_PDF.cmd` file to your own file in `util/scripts` which will run your command. The text of this file will look like this:

```
#------------------------------------------------------------------------
# Run the scan_from_pdf script on
# a the list of *.pdf files provided
# 
# script command description (see scan_from_pdf.py -h)
# usage: scan_from_pdf.py [-h] [-r R] [-i I] [-o O] [-p P] [-l L] [-f F [F ...]]
 [-g]
#
# Scan PDF images and place pages into directory
#
# optional arguments:
#   -h, --help  show this help message and exit
#   -r R        Image resolution (at least 100, 600+ recommended)
#   -i I        Input Directory containing PDF files
#   -o O        Output Directory to which collections of text files are written
#   -p P        Start page number (default is 0)
#   -l L        Language being read (default is "eng")
#   -f F [F ...] PDF image files to be scanned (default is all)
#   -d          Turn on debug messages
#------------------------------------------------------------------------
universe	= vanilla
executable 	= batch_scan_pdf.sh
getenv		= true
output		= scan.out
error		= scan.err
log		= scan.log
arguments	= "-i /directory/path/to/pdf-files -o /directory/path/to/text-files -r 600 -d"
transfer_executable = false
queue
```

You should only need to edit the "`arguments`" setting of your new file. First, replace `/directory/path/to/pdf-files` with the directory path to the directory containing the PDF files you want to scan. Then replace `/directory/path/to/text-files` with the directory path to the directory where you want to store the output text files.

If you know the optimal resolution, you can replace the `600` value here with the pixels-per-inch value you want. (see [`util/` User Guide](https://github.com/Linguistics575/unlocking-text-main/tree/master/util#user-guide) for instructions on finding the optimal resolution.) If you don't know the optimal resolution, leaving it at 600 should be fine for most documents.

Once you have edited your new file, in the `util/scripts` directory, type the following:

```$ condor_submit <BATCH_FILE_CMD_COPY>```

where `<BATCH_FILE_CMD_COPY>` is replaced by the name of the file you have created.

Exect the process to take as much as 20 to 30 seconds per page. It might take slightly more for large pages or densely-packed text, such as newspapers, slightly less for large-print or small documents.

This could take a while if you are scanning dozens of books with several hundred pages apiece. For example, scanning 20 documents, each with 500 pages, will take somewhere between 60 and 80 hours to run. While this will take some time, it shouldn't overly strain the server.

###### An Example
Imagine you have a series of PDF files stored in the directory `/projects/ling575/itineraries`. You might want to output the text files to your own personal directory at `/home/my_account/ling575/itin_text`. First copy the .cmd file:

```$ cp BATCH_SCAN_PDF.cmd BATCH_SCAN_PDF.itin.cmd```

and then edit the `arguments` entry in `BATCH_SCAN_PDF.itin.cmd` to be:

```
arguments   = "-i /projects/ling575/itineraris -o /home/my_accout/ling575/itin_text -r 600 -d
```

Then run the condor command.

```$ condor_submit BATCH_SCAN_PDF.itin.cmd```

This will create a background process that attempts to scan and transcribe each PDF file in the directory. To verify that the process is running, you can type:

```$ condor_q```

and should see a process with your user name in the resulting list. If you can't find your process, check the file `scan.err` in the directory where you ran the process (i.e. in `util/scripts`). It should contain any explanation for errors it encountered.

##### Running Condor to Scan JPEG files
A `SCAN_JPG_DIR.cmd` file also exists to run the scan process on a directory of page images. (see [`util/` User Guide](https://github.com/Linguistics575/unlocking-text-main/tree/master/util#user-guide) for instructions on extracting JPEG images from a PDF.)

As with the PDF Scan, you want to copy the `SCAN_JPG_DIR.cmd` file and edit the `arguments` line. In this file, the arguments consist of the directory path to the JPEG files and the directory path to the output for the text files for that document. The process will create one transcript text file for each page that was scanned.

Scanning the JPEG images will take much less time than scanning from a PDF file. The main downside is that extracting the image files from the PDF is time-consuming and will use up disk space if the document is particularly large. The main reasons to use this option is either because the source documents were in JPEG and not PDF format, or because the PDF Scan process ran into issues extracting the images for the specific PDF. (See [issues](https://github.com/Linguistics575/unlocking-text-main/tree/master/util/scripts#technical-documentation) in the Technical Documentation.)
###### An Example
Imagine you have a collection of JPEG images for the pages of one document at `/project/ling575/journal-1889`. Create a location to output the text transcripts in your own account, say at `/home/my_account/ling575/journal-1889-text`. Now create a new copy of the command file.

```$ cp SCAN_JPG_DIR.cmd SCAN_JPG_DIR_journal-1889.cmd```

Edit the `arguments` line of the new file:

```
arguments   = "/projects/ling575/journal-1889 /home/my_accounts/ling575/journal-1889-text"
```

Then run the process:

```$ condor_submit SCAN_JPG_DIR_journal-1889.cmd```

### Technical Documentation
The `scan_jpg_pages.sh` and `scan_tiff_pages.sh` shell scripts are written for a Linux environment, such as that on any of the UW servers or on your own Linux box. It is possible to run these scripts on a Windows or Mac environment, though with varying degrees of effort.

The scripts as written should run in a Mac environment so long as the necessary software is installed. In windows, you can run Unix shell scripts on Windows using [MobaXTerm](https://mobaxterm.mobatek.net/).
#### Installing Required Software
To run the scan scripts, you will need to install Tesseract.

On Windows, download and run the latest Windows Tesseract installer from the [UB-Mannheim site](https://github.com/UB-Mannheim/tesseract/wiki). The latest supported version is [v3.05.01](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-3.05.01.exe).

On Macintosh, I'm assuming you have _brew_ set up for development. You can then install Tesseract by going to a terminal window and entering:
```
$ brew install imagemagick
```
followed by
```
$ brew install tesseract
```

Alternatively, if you are using _MacPorts_ for your development tools,
```
$ sudo port install tesseract
```

On Linux, in a terminal window, enter:
```
$ sudo apt-install tesseract-ocr
```
followed by
```
$ sudo apt-install libtesseract-dev
```

##### Tesseract Language Support
By default, Tesseract will be installed to support English language scanning. When run, it is possible to instruct Tesseract to scan the text expecting some other language (see the -l option in the Python app documented below).

To support other languages, you will need to install the appropriate language support. In each of the following examples, replace `[lang]` with the three-letter language code for the language you wish to support. It is possible to specify the language as `all` to install support for all languages, but be aware that this could take up a great deal of disk space and take a long time to complete installation.

On Windows, the languages supported should be requested when you run the installer script (see above).

On Macintosh, you need to do the following in a terminal window:
```
$ brew install tesseract-[lang]
```
or using _MacPorts_
```
$ sudo port install tesseract-[lang]
```

In Linux, in a terminal window, enter:
```
$ sudo apt-get install tesseract-ocr-[lang]
```

##### Python
You should be able to achieve what you want with the scripts above and shouldn't need Python for normal activity. However, if you want to run the Python scanning script on your machine, or any of the Python scripts in the `util/` directory, you will need to make sure you have Python installed. It is likely you already have python on your machine. The scripts here were designed specifically for Python 3. They should run with Python2, but have not been fully tested for it.

###### WARNING
In general, you should only be trying to install Python if you are comfortable managing software development tools on your machines. This is particularly true of trying to install Python 3 on a Macintosh environment.

To find out if Python is installed on your machine, and what version it is, go to a terminal window and type:
```
$ python --version
```
If you get a response such as "Python 2.7.12", then you may still have Python 3 installed. Next try typing:
```
$ python3 --version
```

If you do not have Python on your machine, or you want to install Python 3:

On Windows, a good and up to date set of instructions are on the [Open Book Project](http://www.openbookproject.net/courses/webappdev/units/softwaredesign/resources/install_python_win7.html). You need to download and run the latest Windows installer from the [Python download site](http://python.org/download/).

As mentioned above, only install Python 3 on your Macintosh if you are comfortable managing development tools. See the full instructions [here](http://docs.python-guide.org/en/latest/starting/install3/osx/).
The good news is that Mac OS X comes with Python 2 already installed.
 
On Linux, installing Python 3 is a bit simpler, but will still probably involve some development tool tweaking. In a terminal window:
```
$ sudo apt-get install python3.6
```
#### The Python Script
The python script will extract pages from a PDF file as images and run the Tesseract scanner against each page, generating a series of page_####.txt files as output. The process typically takes between twenty to thirty seconds per page, depending on the size of the page and density of text.

The controls for the script are:
```
scan_from_pdf.py
All command line arguments are optional:

  -h, --help        show this help message and exit

  -f <PDF-file> [<PDF-file> ...]  PDF Filenames
        This specifies the files to be scanned. If left empty, it will attempt scan all documents with a *.pdf file type in the target input diretory. Filenames may specify a directory path. If the -i Input Directory option is also used, then this path specification is appended to the input directory.

  -i <Input Directory>  Input Directory containing input PDF files
        The directory from which all PDF files to be scanned will be read. By default, it will either use the current directory or the path specified in the -f file specification.

  -o <Output Directory> Output Directory for collections of text files
        The directory to which all scanned results will be output. If not specified, they will be written to the current directory. The results of PDF scan operation 

  -r <resolution>   Image resolution in dpi (at least 100, 600+ recommended)
        The resolution of the output image, in dpi (dots per inch). Note that a high DPI does not improve the quality of the image if it already has a low resolution. In general, a resolution of at least 600 dpi is recommended.

  -l <language code>  Language being scanned
       The language of the document(s) being scanned, in three-character ISO-639-2 code. Default is "eng" (English).

  -p <page number>  Start page number (default is 0)
       Page number used in the output files. This could be useful if you know that all of your documents start on page 1, for example. The default is 0, meaning the first page will be stored in "page_0000.txt".

  -d                Turn on Debug messages
       If this is specified, then debugging messages are written to the screen, tracking the operations.
```
##### Running the Script From Condor
###### The Condor Command File
Much of this has already been covered above in the User Guide. Further details are added here for anyone who would like to customize the scanning automation process further.

Since scanning a 500-page document could possibly take as much as four hours to complete, it is best to run the scanning utility on Condor so that it runs in the background. This cuts down on overuse of the server and lets you do other work while the scan is taking place. 

In the directory, you can see a sample BATCH_SCAN_PDF.sample.cmd file. This provides the instructions to Condor to let it know what to do. To scan the documents you are interseted in, you need to modify the "arguments" setting in the file. An example looks like this:


```
arguments	= "-i sample -o tmp -r 800 -f sample_journal.pdf"
```

This will read the file in "sample/sample_journal.pdf" and output the results to the directory "tmp/sample_journal", creating the sample_journal directory if necessary. To read your files, change the Input directory (-i value) and Files (-f values). For example, to read the files "file1.pdf" and "file2.pdf" from a directory called "myRepsitory" on your account, the arguments would look something like this:

```
arguments	= "-i /home/myAccount/myRepository -o /home/myAccount/myScannedFiles -r 800 -f file1.pdf file2.pdf"
```

If you want to read all of the PDF files in one directory, set the -i value to that directory, and leave out the -f value, like this:

```
arguments      = "-i /home/myAccount/myRepository -o/home/myAccount/myScannedFiles -r 800"
```

###### Running the Condor Process
Once you have set the arguments as you want them, type the command:

    $ condor_submit BATCH_SCAN_PDF.cmd

This will start the process in the background.

To see the status of the process, type the command:

    $ condor_q

and look for your account ID in the list of processes. The entry should look something like this:

```
OWNER    BATCH_NAME      SUBMITTED   DONE   RUN    IDLE   HOLD  TOTAL JOB_IDS
. . .
lindbe2  CMD: scan_al   5/17 11:21      _      1      _      _      1 103814.0
```

You will usually see a "1" under "IDLE" early on. To make sure it is working correctly, it is a good idea to wait until the condor_q command shows this under "RUN", telling you the process has started.

If the process ends early, the errors will be listed in the file "scan.err".


#### Issues
##### Tesseract Warning Messages
Some warnings will be reported by the scanner ("Tesseract") which are ignorable, but unfortunately cannot be prevented from being written to the scan.err file. These can look something like this:

```
Warning in pixReadFromTiffStream: bpp = 48; stripping 16 bit rgb samples down to
 8
Page 1
Warning in pixReadMemTiff: tiff page 1 not found
```

##### ImageMagick GhostScript incompatibilities
Due to some issues with the image extraction code, which calls the ImageMagick application, and the current version of GhostScript on Patas, some PDF files cannot be read on Patas. If this happens, the error will be reported in the log file in the document output directory.

```
Could not create image files from "tmp/sample_journal/page_0000.tiff"
    Abandonining text extraction.
```
If this happens, it is possible to extract the image files outside of patas and then move them to the server to be scanned. This could take up a lot of memory for each document, depending on the number of pages being read and the desired resolution, so it is recommended to extract one document at a time this way.