from __future__ import print_function
import os
import cat
if type(3/2) is float:
    def raw_input(string=''):
        return input(string)
cfg = cat.getvar('playlistsearch.cfg')
if cfg['usecfg']:
    pname = cfg['pname']
    drivename = cfg['drivename']
    remname = cfg['remname']
else:
    pname = raw_input('Please enter the playlist file name\n')
    drivename = raw_input('Please enter the folder contianing the files to be searched\n')
    remname = raw_input('Please enter file path portion to be removed from playlist entries.\n')
with open(pname, 'a') as playlist:
    while True:
        search = raw_input('input file name to search\n').lower()
        if search == 'done':
            break
        else:
            found = [None]#None is filler for indexing
            i=1
            print(0, 'none of these')
            files = (os.path.join(root, fname) for root, _, fnames in os.walk(drivename) for fname in fnames)
            for f in files:
                if search in f.lower():
                    found.append(f)
                    print(i, f)
                    i += 1
            nums = raw_input('input the number(s) of the files. Seperate entires with commas (,). Hyphens (-) may be used for ranges.\n')
            nums = nums.replace(' ', '').split(',')
            for num in nums:
                if num == '0':
                    break
                elif '-' in num:
                    num = num.split('-')
                    for i in range(int(num[0]), int(num[1])+1):
                        playlist.write(found[i].lstrip(remname).lstrip('/').lstrip('\\')+'\n')
                else:
                    playlist.write(found[int(num)].lstrip(remname).lstrip('/').lstrip('\\')+'\n')
