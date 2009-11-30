import sys
import shutil
import os

    
def h(o, b):
    if 'win' in sys.platform:
        dest = o['location']
        lib = os.path.join(dest, 'lib')
        bin = os.path.join(dest, 'bin')
        for d in bin, lib:
            if not os.path.exists(d):
                os.makedirs(d)
        for dll in ['sqlite3.dll', 'sqlite3.def']:
            dests = [os.path.join(bin, dll), os.path.join(lib, dll)]
            orig = os.path.join(o['compile-directory'], dll)
            for ldest in dests:
                if os.path.exists(ldest):
                    os.remove(ldest)
                shutil.copy2(orig, ldest)
                if dll == 'sqlite3.dll':
                     shutil.copy2(orig, os.path.join(bin, 'cygsqlite3.dll'))
                     shutil.copy2(orig, os.path.join(lib, 'cygsqlite3.dll'))

    
# vim:set ts=4 sts=4 et  :