#from __future__ import print_function
import os, sys
from excode import getvar
#from RemoveSpacesFunc import delspace

def delspace(myPath):
    import os
    
    paths = (os.path.join(root, filename)
             for root, _, filenames in os.walk(myPath)
             for filename in filenames)
    for path in paths:
        newname = os.path.dirname(path) + '/###%%%' + os.path.basename(path)
        try: os.rename(path, newname)
        except WindowsError, e:
            print e
            print path
            print newname
            pass
        
    paths2 = (os.path.join(root, filename)
             for root, _, filenames in os.walk(myPath)
             for filename in filenames)

    for path in paths2:
        newname = path.replace('###%%% ', '')
        if newname != path:
            try: os.rename(path, newname)
            except WindowsError, e:
                print e
                print path
                print newname
                pass
            else:
                print 'renamed %s' % path
        else:
            newname = path.replace('###%%%', '')
            try: os.rename(path, newname)
            except WindowsError, e:
                print e
                print path
                print newname
                pass


NumChanged = 0
errors = 0
varss = getvar('Remove.cfg')
toRemove = varss['remove']
thepaths = varss['path']
print('This program will remove certian annoying charecter sequences from your file names.')
if not toRemove:
    toRemove = raw_input('Enter the sequence you want to remove from the file beginning\n')
    print('Will remove "%s"' % toRemove)
    toRemove = [toRemove]
print('press ENTER to continue')
raw_input()
for myPath in thepaths:
    for thing in toRemove:
        paths = (os.path.join(root, filename)
            for root, _, filenames in os.walk(myPath)
            for filename in filenames)
        if thing == ' ':
            delspace(myPath)
        else:
            for path in paths:
                fname = os.path.basename(path)
                newname = fname.replace(thing, '')
                newname = os.path.join(os.path.dirname(path), newname)
                if newname != path:
                    try: os.rename(path, newname)
                    except WindowsError, e:
                        print e
                        print path
                        print newname
                        errors += 1
                        print 'press ENTER to contiue'
                        raw_input()
                        pass
                    else:
                        print 'Sucessfully renamed %s' % path
                    #print('removed "%s" from %s' % (thing, path))
                    NumChanged += 1

print('done')
print(str(NumChanged) + ' files changed.')
print('%s errors' % errors)
print('Press any key to exit.')
raw_input()
sys.exit()
