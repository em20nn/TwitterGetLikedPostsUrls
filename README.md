# Twitter Get Liked Posts Urls

A python script to help you get your liked posts urls and write them into a file.


## Requirements

This script has been written in Windows 10 and only works on Windows PCs.

- [hashlib]
- [selenium]
- [time]
- [os]
- [keyboard]
- [warnings]
- [argparse]
- [getpass]

They can be installed by running:

````
pip install hashlib selenium time os keyboard warnings argparse getpass
````


## Usage

"py twitter_liked_urls.py" inside the folder in Windows Powershell

### Arguments

```
ALL ARGUMENTS ARE OPTIONAL
```
```
py twitter_liked_urls.py -a "account_name_to_capture" (default your own) -t "new_lines or spaces"(default new_lines) --until "https://www.twitter.com/anyuser/status/post_id" (stops when reached the url)(default none) -o "output_file.txt"(default "final.txt") -f "10" (choose between 1 and 10, 10 being the fastest, default=2) -e (choose between 1 and 20 as maximum errors tolarenced, default = 8)
```
