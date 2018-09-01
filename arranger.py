import os
from datetime import datetime
import shutil
import re
now = datetime.now()
basepath = os.path.abspath('cool.txt')
print(basepath)
desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

imgs = []
docs = []
vids = []
all_dirs = []
whitelisted = ['.command']

for item in os.listdir(desktop):
    path = desktop+'/'+item
    #if any([word not in item for word in whitelisted]):
    if re.compile('|'.join(whitelisted),re.IGNORECASE).search(item): #re.IGNORECASE is used to ignore case
        print('do nothing')
    else:
        if os.path.isfile(path):
            file = open(path)
            fileName,fileExtension = os.path.splitext(item)
            #print('It is a file whose extension is ' + fileExtension + ' and full name is ' + fileName + '. Size is ' + str(os.path.getsize(path)/1000))
            if fileExtension.endswith(('.png','.jpeg', '.jpg', '.gif')):
                imgs.append( {'path':path, 'name':fileName+fileExtension} )
            if fileExtension.endswith(('.txt', '.docx', '.doc', '.pdf')):
                docs.append( {'path':path, 'name':fileName+fileExtension} )
            if fileExtension.endswith(('.mp4','.mkv','.avi','.3gp', '.mov', '.vls')):
                vids.append( {'path':path, 'name':fileName+fileExtension} )
        if os.path.isdir(path):
            all_dirs.append(path)
            print('This is a directory', item, os.path.getsize(path)/1000)

if len(imgs) > 0:
    print('at least one image exists')
    directory = desktop+'/images-'+str(now.strftime("%d-%m-%y"))
    today_dir = desktop+'/images-'+str(now.strftime("%d-%m-%y"))
    if (today_dir in all_dirs) or (os.path.exists(today_dir)):
        print('This path exists')
        print(today_dir)
        for img in imgs:
            shutil.move(img['path'], today_dir+'/'+img['name'])
            print(img['path'])
            print('copied one')
    else:
        os.mkdir(today_dir)
        print('made directory')
        for img in imgs:
            shutil.move(img['path'], today_dir+'/'+img['name'])
            print(img['path'])
            print('copied one')

if len(docs) > 0:
    print('at least one text exists')
    directory = desktop+'/docs-'+str(now.strftime("%d-%m-%y"))
    today_dir = desktop+'/docs-'+str(now.strftime("%d-%m-%y"))
    if (today_dir in all_dirs) or (os.path.exists(today_dir)):
        print('This path exists')
        print(today_dir)
        for doc in docs:
            shutil.move(doc['path'], today_dir+'/'+doc['name'])
            print(doc['path'])
            print('copied one text')
    else:
        os.mkdir(today_dir)
        print('made directory')
        for doc in docs:
            shutil.move(doc['path'], today_dir+'/'+doc['name'])
            print(doc['path'])
            print('copied one text')

if len(vids) > 0:
    print('at least one text exists')
    directory = desktop+'/vids-'+str(now.strftime("%d-%m-%y"))
    today_dir = desktop+'/vids-'+str(now.strftime("%d-%m-%y"))
    if (today_dir in all_dirs) or (os.path.exists(today_dir)):
        print('This path exists')
        print(today_dir)
        for vid in vids:
            shutil.move(vid['path'], today_dir+'/'+vid['name'])
            print(vid['path'])
            print('copied one video')
    else:
        os.mkdir(today_dir)
        print('made directory')
        for vid in vids:
            shutil.move(vid['path'], today_dir+'/'+vid['name'])
            print(vid['path'])
            print('copied one video')
