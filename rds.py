#!/usr/bin/env python
# coding: utf-8

# In[92]:


import numpy as np
from PIL import Image, ImageDraw

# Input RDS's size, caring be dividable 
size = 100

# Input the disparity, 
disparity = 4

# The target size is half of RDS’s　size in default 
inner = int(size/ 2)

# Two images prepair
img = Image.new("L", (size, size), 255)
draw = ImageDraw.Draw(img)

img2 = Image.new("L", (size, size), 255)
draw2 = ImageDraw.Draw(img2)

# Drawing the planes of RDS
for i in range(0, size):
    for j in range(1, size + 1):
        x = np.round(np.random.binomial(1, 0.5, 1))*(j)
        draw.point((x, i), fill=(0))
        draw2.point((x, i), fill=(0))

# Filling the targets area
draw.rectangle((int(size/2) - int(inner/2)-1,  int(size/2) + int(inner/2), int(size/2) + int(inner/2)-1, int(size/2) - int(inner/2)), fill=255, outline=None)
draw2.rectangle((int(size/2) - int(inner/2) + disparity -1,  int(size/2) + int(inner/2), int(size/2) + int(inner/2)- 1+ disparity, (size/2) - (inner/2)), fill=255, outline=None)

# Drawing the targets
for i in range(0, inner+1):
    for j in range(0, inner + 1):
        x = np.round(np.random.binomial(1, 0.5, 1))*(1+j)
        if x != 0:
            draw.point((x + ((size/2) - (inner/2)) -2 , i + (size/2) - (inner/2)))
            draw2.point((x + (size/2) - (inner/2) -2 + disparity, i + (size/2) - (inner/2)))

# Write images
img.save('rds.jpg', quality=100)
img2.save('rds2.jpg', quality=100)

