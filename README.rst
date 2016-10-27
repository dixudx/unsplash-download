unsplash-download
=================

This little Python script allows you to download the fine public domain images
from http://unsplash.com

This will not download images that already exist locally, thus making it possible to
run this from a cron job.

v1.2.0
------
author - jmorris1501

- Updated to working state.
- Command changed after setup script changed to use Scripts instead of entry_points, this changed the command call to 'unsplash_download'.
  The command did run successfully using entry points, but after every run would throw an AttributeError: 'module' has no attribute 'main'.
- Minor Bug and code fixes.
- Updated imports.

Requirements
------------

- Python 3
- beautifulsoup4
- lxml
- docopt

	Notes
	-----
	
	- lxml has issues when installed by pip/PyPI so it is better to 
	  download and install it separately

Installation
------------

You can use pip/PyPI, which will automatically resolve all dependencies:

::

    pip install unsplash-download
	
	Notes
	-----
	
	- this will install v1.1.1, v1.2.0 has not been uploaded yet


To install unsplash-download you can also clone the repo and install it via 
setup.py:

::

    git clone https://github.com/mkzero/unsplash-download
    python setup.py install

After that you should be able to use the ``unsplash_download`` command from 
your command line.

The featured collections can be retrieved using 

	'unsplash_download <output_location_of_choice> <collections by default, this is optional> 1 <currently 116 as of 22  July 2016, this will likely change in the future>'

The other collections should be able to be retrieved using minimum index greater than 116, 
and a maximum index of something around 270000.

It should be noted that not every index is used, which is why the script doesn't exit on 
each html error.

Also, 270000 is close to the maximum encountered index, so if a higher index is found, 
use that in your command.

It should be noted that these images are not small when downloaded in large batches 
(the 116 featured collections are 3.14GB altogether), so rather run the index range as 
that of 50 or 100, for example: 

	'unsplash_download <output_location_of_choice> 150 250'
	
This is especially important if you are running on a weaker or intermittant internet connection