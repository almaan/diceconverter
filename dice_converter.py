#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 22:23:25 2018

@author: A Andersson

"""

import numpy as np
from PIL import Image
import os.path as osp
import argparse as arp

global FACEPATH

FACEPATH = osp.join( osp.dirname(osp.realpath(__file__)),'faces')

def make_dice_image(img, n):
    size = (n,n)
    dice_dict = {x:Image.open(osp.join(FACEPATH,''.join(["00",str(x),'.png']))).resize(size) 
                for x in range(1,7)}
    
    img = img.convert('L')
    newsize = (n*img.size[0],n*img.size[1])
    img = np.array(img).T
    digitized = 7 - np.digitize(img, bins = np.linspace(0,255,6))
    out = Image.new('L', newsize)
    
    for x in range(0,newsize[0],n):
        for y in range(0,newsize[1],n):
            out.paste(dice_dict[digitized[int(x/n),int(y/n)]],(x,y))
        
    return out

prs = arp.ArgumentParser()

prs.add_argument('-i','--image_file',
                 required = True,
                 help = ''.join(['name of image file',
                                 'to be converted',
                                 ]))
    

prs.add_argument("-o","--output_file",
                 required = False,
                 default = 'dice_picture.png',
                 help = ''.join(["name of to which picture shoul",
                                 'be save. if non given, default will',
                                 'be used',
                                 ]))

    
prs.add_argument('-ds','--die_size',
                 required = False,
                 type = int,
                 default = 10,
                 help = ''.join(['size of each die that',
                                 'will represent each pixel',
                                 'picture will be scaled by',
                                 'this amount unless rescaled',
                                 ]))
    
prs.add_argument("-r","--resize_factor",
                 required = False,
                 type = float,
                 default = 1.0,
                 help = ''.join(['ratio by which original picture should',
                                 'be rescaled. Recommended to use for', 
                                 'picture larger than 1000x1000px',
                                 ]))
    
args = prs.parse_args()

if __name__ == '__main__':
    print(f'Initating conversion of file {args.image_file:s}')
    img = Image.open(args.image_file)
    scaledsize = (int(args.resize_factor*img.size[0]),
                  int(args.resize_factor*img.size[1]))
    
    img = img.resize(scaledsize)
    img = make_dice_image(img, n = args.die_size)
    
    
    try:
        img.save(args.output_file)
        out_name = args.output_file
        
    except ValueError:
        splitted_name = args.output_file.split('.')
        if len(splitted_name) > 1:
            out_name = '.'.join([''.join(splitted_name[0:-1]),'png'])
        else:
            out_name = ''.join([splitted_name[0], '.png'])
        
        img.save(out_name)
    
    print(f'Successfully saved genrated image')