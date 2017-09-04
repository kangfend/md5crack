#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright © 2016 Sutrisno Efendi <kangfend@gmail.com>
# Crack md5 hash via http://hashkiller.co.uk

import argparse
import cfscrape
import os
import requests
import StringIO

from ocr import image_to_string
from PIL import Image
from pyquery import PyQuery


HOST = 'https://www.hashkiller.co.uk'


def crack(md5, auto=True):
    scraper = cfscrape.create_scraper()
    response = scraper.get(HOST + '/md5-decrypter.aspx')

    # Save headers and cookies, to be used in next request
    session = requests.session()
    session.headers = response.headers
    session.cookies = response.cookies

    query = PyQuery(response.content)
    image_path = query("#content1_imgCaptcha").attr("src")
    image_content = scraper.get(HOST + image_path).content

    # Trying to decaptcha image
    captcha_image = Image.open(StringIO.StringIO(image_content))

    if auto:
        img = captcha_image.load()
        pix = captcha_image.size

        for x in xrange(pix[0]):
            for y in xrange(pix[1]):
                if img[x, y][0] < 107 or img[x, y][1] < 4:
                    img[x, y] = (0, 0, 0, 255)
                if img[x, y][2] > 0:
                    img[x, y] = (255, 255, 255, 0)

        captcha = image_to_string(captcha_image)
        captcha = filter(str.isalnum, captcha).upper()
    else:
        captcha_image.show()
        captcha = raw_input("[+] Input captcha: ")

    if len(captcha) != 6:
        return False

    scraper = cfscrape.create_scraper(sess=scraper)
    response = scraper.post(HOST + '/md5-decrypter.aspx', data={
        'ctl00$ScriptMan1': 'ctl00$content1$updDecrypt|ctl00$content1$btnSubmit',
        'ctl00$content1$txtInput': md5,
        'ctl00$content1$txtCaptcha': captcha,
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': query("#__VIEWSTATE").attr("value"),
        '__EVENTVALIDATION': query("#__EVENTVALIDATION").attr("value"),
        '__ASYNCPOST': 'true',
        'ctl00$content1$btnSubmit': 'Submit',
        query('#content1_pnlStatus input').attr('name'): query('#content1_pnlStatus input').attr('value')
    })
    response = PyQuery(response.content)
    status = response('#content1_lblStatus').text()
    result = response('#content1_lblResults .text-green').text()

    return status, result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Crack md5hash over https://hashkiller.co.uk')
    parser.add_argument('md5', nargs='+', help='md5 hash')
    parser.add_argument('-m', '--manual-captcha', default=False,
                        help='Manual captcha image. (GUI only)',
                        action='store_true')
    args = parser.parse_args()
    if args.md5:
        md5hash = args.md5[0]
        if len(md5hash) != 32:
            print "[!] Your hash is not md5!"
            exit()
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")
        print "[+] Trying to crack your hash..."

        while True:
            try:
                auto = False if args.manual_captcha else True
                cracking = crack(md5hash, auto=auto)
                if cracking:
                    if 'CAPTCHA' in cracking[0]:
                        continue
                    elif 'Failed' in cracking[0]:
                        print "[-] Result: Hash not found!"
                    else:
                        print "[+] Result: %s" % cracking[1]
                    exit()
                else:
                    continue
            except KeyboardInterrupt:
                print "\b\b[!] Thanks for using this tool."
                exit()
            except Exception as error:
                print "\b\b[-] %s" % error.message
                exit()
    else:
        parser.print_help()
