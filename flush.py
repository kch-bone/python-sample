#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
created by keiichi 
"""

from PIL import Image
from PIL import ImageOps
import os

import sys, time

def ascii(pmatrix, sx, sy, columns):

    tab = ""
    tablen = 0

    if columns <= sx:
        sx = columns
        columns = 0
    else:
        tablen = columns - sx*2
        for i in xrange(tablen):
            tab = tab + " "

    line = ""
    for y in xrange(sy):
        sentence = ""
        for x in xrange(sx*2):

            gray = pmatrix.getpixel((x,y))

            """            
            if gray > 250:
                character = " "
            elif gray > 230:
                character = "."
            elif gray > 200:
                character = ":"
            elif gray > 175:
                character = "+"
            elif gray > 150:
                character = "*"
            elif gray > 125:
                character = "#"
            elif gray > 50:
                character = "@"
            
           
            if gray > 250:
                character = " "
            elif gray > 230:
                character = "."
            elif gray > 210:
                character = ":"
            elif gray > 190:
                character = "|"
            elif gray > 170:
                character = "/"
            elif gray > 150:
                character = "+"
            elif gray > 130:
                character = "*"
            elif gray > 110:
                character = "¥"
            elif gray > 90:
                character = "&"
            elif gray > 70:
                character = "$"
            elif gray > 50:
                character = "@"
            """

            if gray > 250:
                character = "@"
            elif gray > 230:
                character = "$"
            elif gray > 210:
                character = "&"
            elif gray > 190:
                character = "¥"
            elif gray > 170:
                character = "*"
            elif gray > 150:
                character = "+"
            elif gray > 130:
                character = "/"
            elif gray > 110:
                character = "|"
            elif gray > 90:
                character = ":"
            elif gray > 70:
                character = "."
            elif gray > 50:
                character = " "


            sentence = sentence + character
        line = line + sentence + tab
        
    return line


if __name__ == '__main__':

    try:


        param = sys.argv

        filename = 'logo.gif'

        if param[1] != None:
            
            filename = param[1]
            
        try:
            src = Image.open(filename)
            
        except IOError:
            print "Cant load", filename
            sys.exit(1)

        rows, columns = os.popen('stty size', 'r').read().split()

        size = 60
        sx =  src.size[0]
        sy =  src.size[1]
    
        if param[2] != None:
            size  = int(param[2])

        gif = []

        if (src.format == 'GIF'):
            try:
                while 1:
                    
                    try :
                            image = src.resize((size*2, size), Image.ANTIALIAS)
                            output_image = ImageOps.grayscale(image)
                            gif.append(ascii(output_image, int(size) , int(size), int(columns)))
    
                    except ValueError,UnboundLocalError:
                        pass
                    src.seek(src.tell()+1)
                    # 各フレーム毎の処理をする
    
            except EOFError:
                pass

            print len(gif)
            count = 2
            for i in xrange(count):
                for tgif in gif:
                    #sys.stdout.write("\r"+tgif)
                    os.system("clear")
                    sys.stdout.write('\r%s' % str(tgif))
                    sys.stdout.flush()
                    time.sleep(0.1)
        else:

            image = src.resize((size*2, size), Image.ANTIALIAS)
            #image.show()
            output_image = ImageOps.grayscale(image)
            print ascii(output_image, int(size), int(size), int(columns))
        

    except Exception as e:
        print '=== エラー内容 ==='
        print 'type:' + str(type(e))
        print 'args:' + str(e.args)
        print 'message:' + e.message
        print 'e自身:' + str(e)
    