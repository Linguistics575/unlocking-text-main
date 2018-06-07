## FineReader Templates for the Egyptian Gazette
This directory contains sample layout files. The Egyptian Gazette scans we have available for the period roughly from 1900 to 1907 have the same general layout. 
* The first and second pages consist of advertisements and shipping schedules in a three-column layout. 
* The third page contains news and advertisements in a six-column layout.
* The fourth page contains advertisements and notices in a combined three and six-column layout. This is the most difficult to read using layout templates.
* The fifth and sixth pages are similar to the page three news page, in a six-column layout, with the added complication of including some content in French and trade and commodities tables in tabular form.

The only templates created so far are
* FrontPage.blk - created for the first and second advertising and shipping pages at the standard image size provided by Wil Hanley of Florida State University. [These copies](https://github.com/dig-eg-gaz/page-images) cover the years 1905-1907, and tend to be of better quality than the 1900-1901 copies we have.
* NewsPage.blk - created for the page three content from the smaller-resolution images in our repository.
* LargeNewsPage.blk - another page three layout template for the larger images from Wil Hanley's repository.

To apply any of these templates,

* Start FineReader and load the copy of the Egyptian Gazette desired.
* Select the page you want to scan.
* Click on the "Image Editor" icon near the upper right-hand corner.
* Select and run "Deskew" and "Correct Perspective"
* Close the Image Editor (click on the icon again)
* Select "Area->Load Layout" from the menu
* Select the appropriate layout for the page.
* Verify that the layout properly fits the page.
* Run the scan!