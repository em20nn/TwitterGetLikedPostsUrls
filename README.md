# ONLY FOR WINDOWS OPERATING SYSTEM
# Twitter Get Liked Posts Urls

A python script to get all liked posts urls and write them into a file.

## Requirements

This script has been written for and only Windows.

- [chrome]
- [python]
- [hashlib]
- [selenium]
- [time]
- [os]
- [keyboard]
- [warnings]
- [argparse]
- [getpass]

# Install

Install Google Chrome --> download the latest version from google.com
Install Python --> download the latest version from python.org

OPEN A CMD COMMAND LINE

````
py -m pip install selenium
py -m pip install keyboard
py -m pip install wget
````

## Usage

in Windows Powershell
```
~\TwitterGetLiked> py .\twitter_liked_urls.py 
```
in CMD
```
~\TwitterGetLiked> py twitter_liked_urls.py 
```

### Arguments

ALL ARGUMENTS ARE OPTIONAL

```
-a "account_username_to_capture" (default=your own twitter account) 
-t "new_lines or spaces" (default=new_lines, eg. new_line=url1 \n url2 ... * spaces=url1 url2 ...)
--until "https://www.twitter.com/*anyuser*/status/*post_id*" (stops when or if reached the url, default=none) 
-o "output_file.txt" (default=final.txt) 
-f "number between 1 and 10" (10 being the fastest, default=2, using at high speed may cause errors) 
-e "number between 1 and 20" (maximum tolerated errors, default = 8)
```
