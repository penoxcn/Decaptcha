#!/usr/bin/env python
# coding=gbk

import os,sys
from PIL import Image
from decaptcha import Decaptcha

def captcha(inputPic):  
    img = Image.open(inputPic) # Your image here!   
    img = img.convert("RGBA")  
    pixdata = img.load()  
    width,height = img.size
    print 'imgsize: %d x %d' % (width, height)
    bitmap = ''
    for y in xrange(height):
        sys.stdout.write('\n')
        sys.stdout.write('%02x:' % (y))
        for x in xrange(width):
            if pixdata[x, y] == (0xD3,0xD3,0xD3,0xFF):
                bitmap+='\0'
                sys.stdout.write(' ')
            else:
                sys.stdout.write('#')
                bitmap+='\1'
    ####
    dc = Decaptcha('/usr/local/tesseract/tessdata','eng')
    dc.SetCharList('0123456789')
    ostr = dc.Recognize(bitmap, 1, width, 5, 4, 50, 16)
    print 'ostr=' + ostr

if __name__ == '__main__':
    captcha(sys.argv[1])
    print
