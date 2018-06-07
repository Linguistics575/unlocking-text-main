#!/bin/bash

./get_page_images_as_tiff.sh $1 $2
./scan_tiff_pages.sh $2 $2
rm $2/*.tiff
