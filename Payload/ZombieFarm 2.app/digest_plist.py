import hashlib
import os
import plistlib
import xml

def md5(string):
    return hashlib.md5(string).hexdigest()

def zfhash(data):
    return md5(md5(data) + 'ZombieFarmMagic')

env_vars = os.environ

plist_path = os.path.join(
    env_vars['BUILT_PRODUCTS_DIR'],
    env_vars['EXECUTABLE_FOLDER_PATH']
)

digest_path = os.path.join(
    env_vars['PROJECT_DIR'],
    'Resources/digest.plist'
)

new_digest = {}

with open(digest_path, 'rb') as f:
    try:
        digest = plistlib.readPlist(f)
    except xml.parsers.expat.ExpatError as e:
        print digest_path
        digest = {}

for file_path, hash in digest.iteritems():
    with open(os.path.join(plist_path, file_path), 'rb') as f2:
        new_hash = zfhash(f2.read())

    new_digest[file_path] = new_hash

    print file_path
    print hash, '->', new_hash
    print '\n'

if new_digest:
    new_digest_path = os.path.join(
        plist_path,
        'digest.plist'
    )
    plistlib.writePlist(new_digest, new_digest_path)
    print 'new digest written'
    print new_digest_path
