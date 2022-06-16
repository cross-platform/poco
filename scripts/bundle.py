import os
import platform
import shutil
import sys
import glob

if len(sys.argv) < 3:
    print('Usage: python bundle.py os config')
    exit(1)

opsys = sys.argv[1]
config = sys.argv[2]

curdir = os.path.dirname(os.path.realpath(__file__))
srcdir = curdir + '/..'
bundledir = curdir + '/bundle'
configdir = bundledir + '/poco/' + opsys + '/' + config

# bundle openssl includes

if os.path.exists(bundledir + '/poco/' + opsys + '/include'):
    shutil.rmtree(bundledir + '/poco/' + opsys + '/include')

shutil.copytree(srcdir + '/openssl/subprojects/openssl-3.0.2/include', bundledir + '/poco/' + opsys + '/include')

# bundle poco includes

shutil.copytree(srcdir + '/builddir/bundle/include/Poco', bundledir + '/poco/' + opsys + '/include/Poco')

# bundle openssl objects

if os.path.exists(configdir):
    shutil.rmtree(configdir)

os.makedirs(configdir + '/libcrypto')

if platform.system() == 'Windows':
    files = glob.iglob(os.path.join(srcdir + '/openssl/builddir/subprojects/openssl-3.0.2/libcrypto.a.p/*.obj'))
else:
    files = glob.iglob(os.path.join(srcdir + '/openssl/builddir/subprojects/openssl-3.0.2/libcrypto.a.p/*.o'))

for file in files:
    if os.path.isfile(file):
        shutil.copy2(file, configdir + '/libcrypto')

os.makedirs(configdir + '/libssl')

if platform.system() == 'Windows':
    files = glob.iglob(os.path.join(srcdir + '/openssl/builddir/subprojects/openssl-3.0.2/libssl.a.p/*.obj'))
else:
    files = glob.iglob(os.path.join(srcdir + '/openssl/builddir/subprojects/openssl-3.0.2/libssl.a.p/*.o'))

for file in files:
    if os.path.isfile(file):
        shutil.copy2(file, configdir + '/libssl')

# bundle poco objects

components = ['ActiveRecord', 'Crypto', 'Data', 'Encodings', 'Foundation', 'JSON', 'JWT', 'MongoDB',
              'Net', 'NetSSL_OpenSSL', 'PageCompiler', 'Redis', 'Util', 'XML', 'Zip']

for component in components:
    component_base = component.split('_')[0]

    os.makedirs(configdir + '/Poco/' + component_base)

    if platform.system() == 'Windows':
        if 'release' in config:
            files = glob.iglob(os.path.join(srcdir + '/builddir/' + component + '/' + component_base + '.dir/Release/*.obj'))
        else:
            files = glob.iglob(os.path.join(srcdir + '/builddir/' + component + '/' + component_base + '.dir/Debug/*.obj'))
    else:
        files = glob.iglob(os.path.join(srcdir + '/builddir/' + component + '/CMakeFiles/' + component_base + '.dir/src/*.o'))

    for file in files:
        if os.path.isfile(file):
            shutil.copy2(file, configdir + '/Poco/' + component_base)

# patch

shutil.copy2(curdir + '/patch/globo', bundledir + '/poco/globo')
shutil.copy2(curdir + '/patch/meson.build', bundledir + '/poco/meson.build')

# zip

if platform.system() == 'Windows':
    bundlezip = curdir + '/poco-win'
else:
    bundlezip = curdir + '/poco-mac'

if len(sys.argv) > 3:
    shutil.make_archive(bundlezip, 'zip', bundledir)
