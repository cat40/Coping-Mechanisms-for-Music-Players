from __future__ import print_function
import os
import cat
from os.path import abspath
if isinstance(3/2, float):
    def raw_input(string=''):
        return input(string)

config = cat.getvar('EveryFolderAPlaylist.cfg')
subfolders = config['subfolders']
rootdir = config['rootDir']
playdir = config['playDir']
ftype = config['ftype']
playlistdir = config['playlistDir']

def writefromdir(d):
##    for name in os.listdir(d):
##        print(os.path.join(d, name), os.path.isfile(os.path.join(d, name)))
    files = [os.path.join(d, f) for f in os.listdir(d) if os.path.isfile(os.path.join(d, f))]
    dirs = [os.path.join(d, dirname) for dirname in os.listdir(d) if os.path.isdir(os.path.join(d, dirname))]
##    print(files, dirs)
    if files:
        with open(os.path.join(playlistdir,os.path.basename(d))+ftype, 'w') as playlist: #os.path.join(playlistdir, dirname)+
##            print('playlist')
            plist = []
            for f in files:
                plist.append(os.path.abspath(f).lstrip(playdir).lstrip('\\').lstrip('/'))
                plist.append('\n')
            (playlist.write(p) for p in plist[:-1])
    if dirs:
        for d in dirs:
            writefromdir(d)

#note: might not handle files in the main directory (would get ignored and not added to a playlist)
if subfolders == 1:
    for dirname in (os.path.join(rootdir, folder) for folder in os.listdir(rootdir)):
        plist = []
        for path in (os.path.join(root, fname) for root, _, fnames in os.walk(dirname) for fname in fnames):
            plist.append(os.path.abspath(path).lstrip(playdir).lstrip('\\').lstrip('/'))
            plist.append('\n')
        with open(os.path.join(playlistdir,os.path.basename(dirname)+ftype), 'w') as playlist:
            print(os.path.join(playlistdir,os.path.basename(dirname)+ftype))
            for p in plist[:-1]:
                playlist.write(p)

elif subfolders == 2:
    for dirname in (abspath(os.path.join(rootdir, folder)) for folder in os.listdir(rootdir)):
##        print(dirname)
        writefromdir(dirname)

else:
    for dirname in (abspath(os.path.join(rootdir, folder)) for folder in os.listdir(rootdir)):
        files = [os.path.join(d, f) for f in os.listdir(d) if os.path.isfile(os.path.join(d, f))]
        with open(os.path.join(playlistdir,os.path.basename(dirname))+ftype, 'w') as playlist: #os.path.join(playlistdir, dirname)+
            plist = []
            for f in files:
                plist.append(os.path.abspath(f).lstrip(playdir).lstrip('\\').lstrip('/'))
                plist.append('\n')
            (playlist.write(p) for p in plist[:-1])

print('done. press ENTER to exit.')
raw_input()
