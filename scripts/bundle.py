import os
import platform
import shutil
import sys

if len(sys.argv) != 2:
    print('Usage: python bundle.py path/to/bundle')
    exit(1)

bundledir = sys.argv[1]
builddir = bundledir + "/.."

if platform.system() == 'Windows':
    bundlezip = builddir + "/Poco-Win"
else:
    bundlezip = builddir + "/Poco-Mac"

shutil.make_archive(bundlezip, 'zip', bundledir)
