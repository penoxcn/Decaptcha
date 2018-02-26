#!/usr/bin/env python
# coding=utf-8


import sys
import StringIO
from PIL import Image
from decaptcha import Decaptcha

gTessDataPath = '/usr/local/share/tessdata'
class captcha:
    @staticmethod
    def loadfile(fpath):
        with open(fpath,'rb') as f:
            return f.read()
    
    @staticmethod
    def decaptch(imgdata, extract):
        ostr = ''
        try:
            imgbuf =  StringIO.StringIO(imgdata)
            img = Image.open(imgbuf)
            img = img.convert("RGBA")
            pixdata = img.load()
            (width,height) = img.size
            bitmap = extract.extract(pixdata, width, height)
            dc = Decaptcha(gTessDataPath,'eng')
            dc.SetCharList(extract.charlist)
            ostr = dc.Recognize(bitmap, 1, width, extract.x1, extract.y1, extract.x2, extract.y2)
            ostr = ostr.replace(' ','').replace('\n','')
            print '.captcha=%s' % (ostr)
        except Exception as e:
            print '!>error: %s' % (str(e))
        return ostr.strip()
    
class Examples:
    ''' demo aa '''
    def faa(self, fpath):
        class extract:
            def __init__(self):
                self.x1,self.y1,self.x2,self.y2 = 1,1,43,18
                self.charlist = '0123456789'
                
            def extract(self, pixdata, width, height):
                bitmap = ''
                for y in xrange(height):
                    sys.stdout.write('\n')
                    sys.stdout.write('%02x:' % (y))
                    for x in xrange(width):
                        (r,g,b,a) = pixdata[x, y]
                        if r+g+b>=480:
                            bitmap+='\1'
                            sys.stdout.write('#')
                        else:
                            bitmap+='\0'
                            sys.stdout.write(' ')
                sys.stdout.write('\n')
                return bitmap
        #do Recognize    
        imgdata = captcha.loadfile(fpath)
        ostr = captcha.decaptch(imgdata, extract())

    ''' demo bb '''
    def fbb(self, fpath):
        class extract:
            def __init__(self):
                self.x1,self.y1,self.x2,self.y2 = 1,1,91,33
                self.charlist = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
                
            def extract(self, pixdata, width, height):
                bitmap = ''
                for y in xrange(height):
                    sys.stdout.write('\n')
                    sys.stdout.write('%02x:' % (y))
                    for x in xrange(width):
                        (r,g,b,a) = pixdata[x, y]
                        if int(r/240)+int(g/240)+int(b/240)<=1:
                            bitmap+='\1'
                            sys.stdout.write('#')
                        else:
                            bitmap+='\0'
                            sys.stdout.write(' ')
                sys.stdout.write('\n')
                return bitmap
        #do Recognize
        imgdata = captcha.loadfile(fpath)
        ostr = captcha.decaptch(imgdata, extract())
        
    ''' demo cc '''        
    def fcc(self, fpath):
        class extract:
            def __init__(self):
                self.x1,self.y1,self.x2,self.y2 = 20,0,88,26
                self.charlist = '0123456789'
                
            def extract(self, pixdata, width, height):
                bitmap = ''
                for y in xrange(height):
                    sys.stdout.write('\n')
                    sys.stdout.write('%02x:' % (y))
                    for x in xrange(width):
                        if x<=20 or x>88 or y==0 or y>=26 or pixdata[x,y]==(0xff,0xff,0xff,0xff):
                            bitmap+='\0'
                            sys.stdout.write(' ')
                            continue
                        if pixdata[x+1, y]==(0xff,0xff,0xff,0xff) and pixdata[x, y+1]==(0xff,0xff,0xff,0xff):
                            bitmap+='\0'
                            sys.stdout.write(' ')
                        else:
                            bitmap+='\1'
                            sys.stdout.write('#')
                sys.stdout.write('\n')
                return bitmap
        #do Recognize
        imgdata = captcha.loadfile(fpath)
        ostr = captcha.decaptch(imgdata, extract())

    ''' demo dd '''        
    def fdd(self, fpath):
        class extract:
            def __init__(self):
                self.x1,self.y1,self.x2,self.y2 = 12,5,64,25
                self.charlist = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                
            def extract(self, pixdata, width, height):
                bitmap = ''
                for y in xrange(height):
                    sys.stdout.write('\n')
                    sys.stdout.write('%02x:' % (y))
                    for x in xrange(width):
                        (r,g,b,a) = pixdata[x, y]
                        if g==0:
                            bitmap+='\1'
                            sys.stdout.write('#')
                        else:
                            bitmap+='\0'
                            sys.stdout.write(' ')
                sys.stdout.write('\n')
                return bitmap
        #do Recognize
        imgdata = captcha.loadfile(fpath)
        ostr = captcha.decaptch(imgdata, extract())

    ''' demo ee '''        
    def fee(self, fpath):
        class extract:
            def __init__(self):
                self.x1,self.y1,self.x2,self.y2 = 6,4,156,56
                self.charlist = '0123456789'
                
            def extract(self, pixdata, width, height):
                bitmap = ''
                colors = dict()
                cords = ( (0,0),(0,1),(1,0),(1,1),
                (width-2,0),(width-2,1),(width-1,0),(width-1,1),
                (0,height-2),(1,height-2),(0,height-1),(1,height-1),
                (width-2,height-2),(width-2,height-1),(width-1,height-2),(width-1,height-1) )
                for x,y in cords:
                    (r,g,b,a) = pixdata[x, y]
                    cc = (r<<16)|(g<<8)|b
                    if cc in colors:
                        colors[cc]+=1
                    else:
                        colors[cc]=1
                cc = sorted(colors.items(), key=lambda x:x[1], reverse=True)
                backcolor = (cc[0][0]>>16, (cc[0][0]>>8)&0xff, cc[0][0]&0xff)
                ######
                colors = dict()
                thrsold = 50
                for y in xrange(27,30):
                    #sys.stdout.write('\n')
                    #sys.stdout.write('%02x:' % (y))
                    for x in xrange(40,120):
                        (r,g,b,a) = pixdata[x, y]
                        delta = (r-backcolor[0])*(r-backcolor[0])+(g-backcolor[1])*(g-backcolor[1])+(b-backcolor[2])*(b-backcolor[2])
                        if delta>thrsold:
                            cc = (r<<16)|(g<<8)|b
                            if cc in colors:
                                colors[cc]+=1
                            else:
                                colors[cc]=1
                        else:
                            #sys.stdout.write(' ')
                            pass
                        
                cc = sorted(colors.items(), key=lambda x:x[1], reverse=True)
                charcolor = (cc[0][0]>>16, (cc[0][0]>>8)&0xff, cc[0][0]&0xff)
                distcolor = (cc[1][0]>>16, (cc[1][0]>>8)&0xff, cc[1][0]&0xff)

                print 'backcolor:%s charcolor:%s distcolor:%s' % (str(backcolor),str(charcolor),str(distcolor))
                bitmap = ''
                for y in xrange(height):
                    sys.stdout.write('\n')
                    sys.stdout.write('%02x:' % (y))
                    for x in xrange(width):
                        (r,g,b,a) = pixdata[x, y]
                        delta = (r-backcolor[0])*(r-backcolor[0])+(g-backcolor[1])*(g-backcolor[1])+(b-backcolor[2])*(b-backcolor[2])
                        if delta<thrsold:#background
                            bitmap+='\0'
                            sys.stdout.write(' ')
                        else:
                            delta1 = (r-distcolor[0])*(r-distcolor[0])+(g-distcolor[1])*(g-distcolor[1])+(b-distcolor[2])*(b-distcolor[2])
                            delta2 = (r-charcolor[0])*(r-charcolor[0])+(g-charcolor[1])*(g-charcolor[1])+(b-charcolor[2])*(b-charcolor[2])
                            if delta2<thrsold:#characters
                                bitmap+='\1'
                                sys.stdout.write('#')
                            elif delta1<thrsold: #lines
                                bitmap+='\0'
                                sys.stdout.write(' ')
                            else: #others,balabala
                                #if x>20 and x<140 and y>15 and y<49:
                                #    (r,g,b,a) = pixdata[x+1, y]
                                #    delta3 = (r-charcolor[0])*(r-charcolor[0])+(g-charcolor[1])*(g-charcolor[1])+(b-charcolor[2])*(b-charcolor[2])
                                    #(r,g,b,a) = pixdata[x, y+1]
                                    #delta4 = (r-charcolor[0])*(r-charcolor[0])+(g-charcolor[1])*(g-charcolor[1])+(b-charcolor[2])*(b-charcolor[2])
                                #    if delta3<thrsold: #or delta4<thrsold:
                                #        bitmap+='\1'
                                #        sys.stdout.write(' ')
                                #        continue
                                bitmap+='\0'
                                sys.stdout.write(' ')
                #print
                sys.stdout.write('\n')
                return bitmap
        #do Recognize
        imgdata = captcha.loadfile(fpath)
        ostr = captcha.decaptch(imgdata, extract())        
        
def main():
    if len(sys.argv)<=1:
        print 'Usage: python %s ftype fpath'
        print '       ftypes: faa,fbb,fcc,fdd'
        return
    
    ftype = sys.argv[1]
    fpath = sys.argv[2]
    
    example = Examples()
    if ftype=='aa':
        example.faa(fpath)
    elif ftype=='bb':
        example.fbb(fpath)
    elif ftype=='cc':
        example.fcc(fpath)
    elif ftype=='dd':
        example.fdd(fpath)
    elif ftype=='ee':
        example.fee(fpath)
    
if __name__=='__main__':
    main()
