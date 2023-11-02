from PIL import Image, ImageEnhance, ImageFilter
import os
from datetime import datetime

path='./input'
pathOut = './output'

print('''
    This script will convert your images to black and white.
    Chose the contrast to apply to the images or ignore for 30% contrast.
      Example:
        Lower Contrast: 0.1 (-90%)
        Higher Contrast: 1.9 (+90%)
''')

try:
    contrast_factor = float(input('How much contrast do you want: '))
except:
    contrast_factor = 1.3  #Default contrast is 30%:

start_time = datetime.now()

print(f'{(contrast_factor -1)*100:.0f}%')

for filename in os.listdir(path):
    print(f'Processing: {filename}')
    img = Image.open(f'{path}/{filename}')

    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    # contrast
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(contrast_factor)

    #get file name without extension
    #example:
    #IMG_19862.jpg  ==> ('IMG_19862', '.jpg')
    clean_name = os.path.splitext(filename)[0]

    edit.save(f'{pathOut}/{clean_name}_BW.jpg')

# Print the formatted duration
print(f"Script execution took {datetime.now() - start_time}")