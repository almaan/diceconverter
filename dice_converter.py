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
import sys
from typing import Optional,Callable,Dict

global FACEPATH

FACEPATH = osp.join( osp.dirname(osp.realpath(__file__)),'faces')

def sample_face(d: Dict[int,Image.Image])->Callable:
    def fun(k):
        if len(d[k]) > 1:
            idx = np.random.choice(len(d[k]),size = 1)
            return d[k][int(idx)]
        else:
            return d[k][0]
    return fun

def make_dice_image(img: Image.Image,
                    n: int,
                    design_file: Optional[str] = None
                    ):
    """
    Takes an PIL.Image object, converts it to a dice-represenation
    and gives as output the rendered image as an PIL.image object

    Arguments:
        - img : PIL.Imgae object (to be transformed)
        - n : pixel size to be used for each die

    Returns:
        out : PIL.Image object (rendered dice-representation)

    """

    #dice size
    size = (n,n) 
    #dict holding image for each die
    if design_file is None:
        dice_dict = {x:Image.open(osp.join(FACEPATH,
                                           ''.join(["00",str(x),'.png']))).resize(size)
                     for x in range(1,7)}
        get_face = lambda x: dice_dict[x]
    else:
        import yaml
        with open(design_file) as f:
            dice_dict = yaml.load(f,Loader=yaml.FullLoader)
        for k in dice_dict.keys():
            for ii in range(len(dice_dict[k])):
                dice_dict[k][ii] = Image.open(dice_dict[k][ii]).resize(size)
        get_face = sample_face(dice_dict)

    img = img.convert('L')
    #image new output size
    newsize = (n*img.size[0],n*img.size[1])
    #cast to numpy.array for binning
    #transposition to reverse automatic transposition by conversion
    img = np.array(img).T
    #binning into six bins in interval [0,256]
    digitized = 7 - np.digitize(img,np.linspace(0,257,7))
    #create new image object (grayscale)
    out = Image.new('L', newsize)
    #insert die-pictures to represent pixels
    for x in range(0,newsize[0],n):
        for y in range(0,newsize[1],n):
            face_id = digitized[int(x/n),int(y/n)]
            face = get_face(face_id)
            out.paste(face,(x,y))

    return out

prs = arp.ArgumentParser()

prs.add_argument('-i','--image_file',
                 required = True,
                 help = ' '.join(['name of image file',
                                 'to be converted',
                                 ]))
    

prs.add_argument("-o","--output_file",
                 required = False,
                 default = 'dice_picture.png',
                 help = ' '.join(["name of file to which picture should",
                                 'be saved. if non given, default will',
                                 'be used',
                                 ]))

    
prs.add_argument('-ds','--die_size',
                 required = False,
                 type = int,
                 default = 10,
                 help = ' '.join(['size of each die faces',
                                 'one die will represent'
                                 ' one pixel. Meaning that',
                                 'pictures will be scaled by',
                                 'this the same factor',
                                 ]))
    
prs.add_argument("-r","--resize_factor",
                 required = False,
                 type = float,
                 default = 1.0,
                 help = ' '.join(['ratio by which original picture should',
                                 'be rescaled. Recommended to use for', 
                                 'pictures larger than 1000x1000px',
                                 ]))

prs.add_argument("-k","--keep_size",
                 required = False,
                 action = 'store_true',
                 default = False,
                 help = ' '.join(['keep current size of image',
                                 'and scale die images accordingly',
                                 ]))

prs.add_argument("-df",
                 "--design_file",
                 required = False,
                 default = None,
                 help = ' '.join(["YAML design file that contains",
                                  "paths to die images.",
                                  ])
                 )

    
args = prs.parse_args()

if __name__ == '__main__':
    print(f'Initating conversion of file {args.image_file:s}')
    
    #test if proper image file is provided, if not exit
    try:
        img = Image.open(args.image_file)
    except OSError:
        print(f"Enter proper image file")
        sys.exit(0)

    if args.keep_size:
        #allows user to keep size of the image using specied die size
        scaledsize = (int(1./args.die_size*img.size[0]),
                      int(1./args.die_size*img.size[1]))
    else:
        #resize image according to scaling factor provided
        scaledsize = (int(args.resize_factor*img.size[0]),
                      int(args.resize_factor*img.size[1]))
    
    img = img.resize(scaledsize)
    
    img = make_dice_image(img, n = args.die_size,design_file =args.design_file)
    
    #check that proper output name is provided, change to .png otherwise
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
