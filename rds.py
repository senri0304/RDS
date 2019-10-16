#!/usr/bin/env python
# coding: utf-8

import os
import numpy as np
from PIL import Image, ImageDraw

to_dir = 'material' 
os.makedirs(to_dir, exist_ok=True)

# Input RDS's size, caring be dividable 
size = 100

# Input the disparity at pixel units
disparity = 18

# Input target size, which is half of RDS’s　size in default 
inner = int(size/ 2)

# Input the quantity you need
q = 5

# Input a number you like to initiate
s = 11

# Generate RDSs
for k in range(s, s + q):

    # Two images prepair
    img = Image.new("L", (size, size), 255)
    draw = ImageDraw.Draw(img)
    
    img2 = Image.new("L", (size, size), 255)
    draw2 = ImageDraw.Draw(img2)
    
    # Draw the planes of RDSs
    for i in range(0, size):
        for j in range(1, size + 1):
            x = np.round(np.random.binomial(1, 0.5, 1))*(j)
            draw.point((x, i), fill=(0))
            draw2.point((x, i), fill=(0))
    
    # Fill the targets area
    draw.rectangle((int(size/2) - int(inner/2) - disparity/2 - 1,  int(size/2) + int(inner/2), int(size/2) + int(inner/2) - 1 - disparity/2, int(size/2) - int(inner/2)), fill=255, outline=None)
    draw2.rectangle((int(size/2) - int(inner/2) + disparity/2 - 1,  int(size/2) + int(inner/2), int(size/2) + int(inner/2) - 1 + disparity/2, int(size/2) - int(inner/2)), fill=255, outline=None)
    
    # Drawing the targets
    for i in range(0, inner+1):
        for j in range(0, inner + 1):
            x = np.round(np.random.binomial(1, 0.5, 1))*(1+j)
            if x != 0:
                draw.point((x + ((size/2) - (inner/2)) -2 - disparity/2, i + (size/2) - (inner/2)))
                draw2.point((x + (size/2) - (inner/2) -2 + disparity/2, i + (size/2) - (inner/2)))
    
    # Write images
    basenameR = os.path.basename('rds' + str(k) + 'R.jpg')
    basenameL = os.path.basename('rds' + str(k) + 'L.jpg')
    img.save(os.path.join(to_dir, basenameR), quality=100)
    img2.save(os.path.join(to_dir, basenameL), quality=100)
