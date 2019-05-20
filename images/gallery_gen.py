# Run me to format the files in images/gallery_images/ for the website
# Also initialize image votes

from glob import glob
import json
import os

if os.path.isfile("gallery_votes.json"):
    gallery_votes = json.loads(open("gallery_votes.json").read())
else:
    gallery_votes = {}

file = open('gallery_images.html', 'w+')
filenames = glob('gallery_images/*')
filenames.sort()

removed_imgs = gallery_votes.copy()

for f in filenames:
    name = f.split('/')[-1].split('.')[0]
    nospace_name = name.replace(" ", "")
    removed_imgs.pop(nospace_name)

    if nospace_name not in gallery_votes:
        gallery_votes[nospace_name] = 0

    file.write('<pre>' + name + "</pre>\n")

    file.write('<img src="images/' + f + '" alt="' + f.split('/')[-1] + '">\n')
    #file.write('<button ...') # format the button

    file.write('<br><br>\n\n')

for f in removed_imgs:
    gallery_votes.pop(f)

with open('gallery_votes.json', 'w') as fp:
    json.dump(gallery_votes, fp)

file.close()
