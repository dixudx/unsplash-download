#!/usr/bin/env python

"""
unsplash-download - Downloads images from unsplash.com

Usage:
  unsplash-download <folder> <min_index> 
  unsplash-download <folder> <min_index> <max_index>
  unsplash-download <folder> <col_type> <min_index> <max_index>
  unsplash-download -h | --help
  unsplash-download -v | --version

Options:
  -h --help                 Show this screen
  -v --version              Show version

"""

DEBUG = False
ud_version = '1.2.0'

import urllib.parse
import urllib.request
import re
import os
import sys
from threading import Thread, ThreadError
from docopt import docopt

base_url = 'https://unsplash.com'
link_search = re.compile("/photos/[a-zA-Z0-9-_]+/download")
page_ender = "photos/?"
url_args = {"grid":"multi", "per_page":"300"}
output_path = "%s/%s.jpeg"
tag_href = 'href'
separator = "/"

def printSeperatorError():
    print("Error------------------------------Error------------------------------------Error")

def printSeperatorThick():
    print("================================================================================")
    
def printSeperator(): 
    print("--------------------------------------------------------------------------------")   

def getArguments():
    return docopt(__doc__, help=True, version='unsplash-download ' + ud_version)

def encodeURLArgs(url_args):
    return urllib.parse.urlencode(url_args)

def constructURL(base_url, col_type, index, page_ender, enc_args):
    return base_url + separator + col_type + separator + str(index) + separator + page_ender + enc_args

def getPageHTML(url):
    return urllib.request.urlopen(url).read()

def makeDirIfNotExists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def getImageNamesFromHTML(html):
    image_list = list(set(re.findall(link_search, str(html))))
    print(str(len(image_list)) + " images found.")
    printSeperator() 
    return image_list 

def retrieveImage(download_url, download_path, index, image_id):
    urllib.request.urlretrieve(download_url, output_path % (download_path + separator + str(index), image_id))

def downloadImage(tag, download_path, index):
    download_url = base_url + tag
    image_id = download_url.split(separator)[4]
    if os.path.exists(output_path % (download_path + separator + str(index), image_id)):
        print("Not downloading duplicate %s" % download_url)
    else:
        print("Downloading %s" % download_url)
        retrieveImage(download_url, download_path, index, image_id)
        
def populateImageLists(images):
    imagelists = {}
    idx = 0
    entry = 0
    for image in images:
        imagelists[idx, entry] = image
        entry += 1
        if entry == 10:
            entry = 0
            idx += 1
    return imagelists

def startThread(imagelists, listIndex, listEntry, download_path, index, threads):
    tag = imagelists[listIndex, listEntry]   
    t = Thread(target=downloadImage, args=(tag, download_path, index))
    t.start()
    threads.append(t)   

def joinThreads(threads):
    for t in threads:   
        t.join()  

def main():
    arguments = getArguments()
    
    folder = arguments['<folder>']
    
    col_type = "collections"
    if arguments['<col_type>']:
        col_type = arguments['<col_type>'] 
         
    min_index = arguments['<min_index>']
    
    if arguments['<max_index>']:
        max_index = arguments['<max_index>']
    else:
        max_index = min_index    
        
    download_path = str(folder) + separator + str(col_type)
    
    error_count = 0   
    html_error_count = 0
    thread_error_count = 0
    pages_not_found = 0
    
    index = int(min_index)
    
    while index < int(max_index) + 1 :
        try:
            enc_args = encodeURLArgs(url_args)
            url = constructURL(base_url, col_type, index, page_ender, enc_args)
            
            printSeperatorThick()
            print("Parsing page %s" % url)
            
            html = getPageHTML(url)
            
            printSeperator()
            
            makeDirIfNotExists(download_path + separator + str(index))
            images = getImageNamesFromHTML(html)  

            imagelists = populateImageLists(images)

            totalLength = 0
            listIndex = 0
            listEntry = 0
            
            listLength = len(imagelists)
            threads = []
                    
            while totalLength < listLength:    
                         
                while listEntry < 10 and totalLength < listLength:         
                    
                    startThread(imagelists, listIndex, listEntry, download_path, index, threads)
                    
                    totalLength += 1         
                    listEntry += 1
                    
                listEntry = 0
                listIndex += 1
                     
                joinThreads(threads)
                  
        except urllib.error.URLError as e:
            if e.code == 404:
                print("Skipping URL : " + url + " : 404 Not Found")    
                if DEBUG:
                    print(e, file=sys.stderr)
                pages_not_found += 1
                continue   
        except urllib.error.HTTPError as e:
            if DEBUG:
                print("HTML error. This would be all.")
                print(e, file=sys.stderr)
            html_error_count += 1
        except ThreadError as e:
            if DEBUG:
                print("Thread error. This would be all.")
                print(e, file=sys.stderr)
            thread_error_count += 1    
        except Exception as e:
            printSeperatorError()
            print(e)
            printSeperator()
            error_count += 1
        finally:
            index += 1
            
    printSeperatorThick() 
    printHtmlErrorMessage(html_error_count)
    printThreadErrorMessage(thread_error_count)
    printPagesErrorMessage(pages_not_found)
    printErrorMessage(error_count) 

def printHtmlErrorMessage(html_error_count):
    if html_error_count > 0:        
        print(str(html_error_count) + " HTML error/s occured", file=sys.stderr)
        printSeperatorThick()

def printThreadErrorMessage(thread_error_count):
    if thread_error_count > 0:        
        print(str(thread_error_count) + " Thread error/s occured", file=sys.stderr)
        printSeperatorThick()
        
def printPagesErrorMessage(pages_not_found):
    if pages_not_found > 0:        
        print(str(pages_not_found) + " page/s not found", file=sys.stderr)
        printSeperatorThick()
        
def printErrorMessage(error_count):
    if error_count > 0:        
        print(str(error_count) + " unknown error/s occured", file=sys.stderr)
        printSeperatorThick()
        
if __name__ == '__main__':
    main()        
