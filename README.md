md5crack
===========

This tools can crack md5 hash over http://hashkiller.co.uk

Installation
============
1. Install OCR:

    For linux user:
    `sudo apt-get install python-imaging tesseract-ocr`

    For Mac user:
    `brew install tesseract`

2. Install requirements

    `pip install -r requirements.txt`


###Command

You can use this tool with this command `./md5crack [hash]`

example: `./md5crack.py 4dd39f49f898c062283963c187532af8`

If you want to input captcha manually, you can pass `-m` argument

example: `./md5crack.py -m 4dd39f49f898c062283963c187532af8`
