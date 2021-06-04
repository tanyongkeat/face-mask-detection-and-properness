import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import shutil
from tqdm import tqdm
import os

urls = [
    'https://drive.google.com/uc?id=17-FCstm8Fz3bDzFgTmOWHa_c39lTR_1P', 
    'https://drive.google.com/uc?id=1XClQlP9_V6UmmnwTyzjF28vlrVHNSw2H', 
    'https://drive.google.com/uc?id=1gjltyD_MnNWcnd56NnjUOizdi39CUEPF', 
    'https://drive.google.com/uc?id=1qvbcuTHSLBTxQd3wXNAUIYVXBBJCa2WF'
]

for n, url in enumerate(urls):
    i = n//2 + 1
    j = n%2 + 1
    output = f'cabani{i}{j}.zip'
    gdown.download(url, output, quite=True)

os.mkdir('cabani')

import random
random.seed(69)

n = 0

# undersampling data for correctly masked class
root = '../input/'
a = os.listdir('cabani11')
a = [os.path.join('cabani11/', tmp) for tmp in a]
b = os.listdir('cabani12')
a = [os.path.join('cabani12/', tmp) for tmp in b]
folder_l1 = a + b
random.shuffle(folder_l1)

for f in tqdm(folder_l1):
    if os.path.isdir(f):
        if n >= 10000:
                break
        for image in os.listdir(f):
            if n >= 10000:
                break
            if '.jpg' in image:
                shutil.copy(f + '/' + image, 'cabani/correct/')
                n += 1


# getting classes of incorrectly masked images
categories = set()

incorrectly_masked = ['cabani21', 'cabani22']
for folder in os.listdir(root):
    root1 = os.path.join(root, folder)
    for folder_l1 in os.listdir(root1):
        root2 = os.path.join(root1, folder_l1)
        if os.path.isdir(root2):
            for image in os.listdir(root2):
                if '.jpg' in image:
                    cat = image[6:-4]
                    categories.add(cat)

for cat in categories:
    os.mkdir(os.path.join('cabani', cat))

import random
random.seed(69)

n = 0

# undersampling 'Mask_Mouth_Chin' class
a = os.listdir('cabani21')
a = [os.path.join('cabani21', tmp) for tmp in a]
b = os.listdir('cabani22')
b = [os.path.join('cabani22', tmp) for tmp in b]
folder_l1 = a + b
random.shuffle(folder_l1)

for f in tqdm(folder_l1):
    if os.path.isdir(f):
        for image in os.listdir(f):
            if '.jpg' in image:
                cat = image[6:-4]
                if cat == 'Mask_Mouth_Chin':
                    if n >= 10000:
                        continue
                    n += 1
                shutil.copy(os.path.join(f, image), os.path.join('cabani', cat))

