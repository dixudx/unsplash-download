unsplash-download
=================

This little Python script allows you to download the fine public domain images
from http://unsplash.com

This will not download images that already exist locally, thus making it possible to
run this from a cron job.

v1.2.0
------
author - jmorris1501

- Added Threading module, will pull 10 images simultaneously
- Removed BeautifulSoup4 and lxml dependencies
- Updated String constants
- Added methods for printing data separators for command line/terminal viewing
- Created methods for:
	-	Getting command line/terminal arguments
	-	encoding page arguments
	-	constructing page URL
	-	fetching page HTML
	-	creating a directory should it not already exist
	-	retrieve the image names from the HTML
	-	setting up an image for download
	-	downloading an image
	-	populating lists of image names (used with threading to download images simultaneously)
	-	starting an image download thread
	-	joining the threads once a group has been started
	-	main method
	-	methods to print various error messages at the end of the script's execution should any occur
- updated version
- updated dependencies in setup.py
- changed entry_points in setup.py to scripts, changes the script call from unsplash-download to unsplash_download
- added basic command line scripts for windows users for install and running this scripts
- updated .gitignore to include eclipse project files
- updated README.rst

-TODO:
	- For those pages with more than 24 images, the other images are only loaded when the bottom of the page 
	  is reached. This script will pull those images retreived on the initial page load, but at the moment
	  it cannot retrieve the additional images.

Requirements
------------

- Python 3
- docopt

Installation
------------

You can use pip/PyPI, which will automatically resolve all dependencies:

	pip install unsplash-download


To install unsplash-download you can also clone the repo and install it via 
setup.py:

    git clone https://github.com/mkzero/unsplash-download
    python setup.py install

After that you should be able to use the ``unsplash_download`` command from 
your command line.

The featured collections can be retrieved using 

	'unsplash_download [output_location_of_choice] ['collections' by default, this is optional] [starting index, featured collections start at '1'] [end index, currently '126' as of 28 October 2016, this will change over time]'

For example:

	unsplash_download /unsplash_output 1 126

The other collections should be able to be retrieved using minimum index greater than 126, 
and a maximum index of something around 270000.

It should be noted that not every index is used, which is why the script doesn't exit on 
each html error.

Also, 270000 is close to the maximum encountered index, so if a higher index is found, 
use that in your command.

It should be noted that these images are not small when downloaded in large batches 
(the 116 featured collections are 3.14GB altogether), so rather run the index range as 
that of 50 or 100, for example: 

	'unsplash_download <output_location_of_choice> 150 250'
	
This is especially important if you are running on a weaker or intermittant internet connection.