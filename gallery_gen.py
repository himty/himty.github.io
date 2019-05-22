# Run me to format the files in images/gallery_images/ for the website
# Also initialize image votes

from glob import glob
import json
import os

file = open('gallery_images.html', 'w+')
filenames = glob('images/gallery_images/*')
filenames.sort()

for f in filenames:
    name = f.split('/')[-1].split('.')[0]
    nospace_name = name.replace(" ", "")

    file.write('' + name + "\n")
    file.write('<button id=' + nospace_name + ' onclick="toggleColor(\'' + nospace_name + '\')" \
        type="button" style="color: black; font-size: 20px;">♥</button><br>')
    file.write('<img src="' + f + '" alt="' + f.split('/')[-1] + '">\n')

    file.write('<br><br>\n\n')

file.close()
