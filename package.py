#!/usr/bin/python
# -*- coding: UTF-8 -*-

import subprocess
import urllib2
import os
import sys


def download_apk(apk_url):
    print 'please wait, downloading apk...'
    f = urllib2.urlopen(apk_url)
    data = f.read()
    file_name = os.path.basename(apk_url)
    file_name_without_ext, ext = os.path.splitext(file_name)

    if ext != '.apk' and f.headers.getsubtype() == 'vnd.android.package-archive':
        ext = '.apk'

    count = 0
    while os.path.exists(file_name):
        count += 1
        file_name = file_name_without_ext + '(' + str(count) + ')' + ext

    with open(file_name, "wb") as apk:
        apk.write(data)
    return file_name


def main(apk, save_apk=False):
    downloaded = False
    if not os.path.isfile(apk):
        apk = download_apk(apk)
        downloaded = True
    subprocess.call(['chmod', '777', 'aapt'])
    sub = subprocess.Popen(['./aapt', 'd', 'badging', apk], stdout=subprocess.PIPE)
    result = sub.stdout.readlines()[0].split()[1:-1]
    result[0] = result[0].replace('name=', 'packageName=')
    print ''
    for r in result:
        print r
    print ''
    if downloaded and not save_apk:
        os.remove(apk)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print '''
        Usage:
            python package.py apk_url
                      or 
            python package.py xxx.apk
        '''
        sys.exit(0)

    # main('/Users/liuzhenhua/Workspace/apk/1.6.8/xianyougame-offical-release-1.6.8-40.apk')
    # main('http://shouji.360tpcdn.com/170316/4b4094bdbf42b275ce190446aa06c524/com.goplaycn.googleinstall_15.apk')
    main(sys.argv[1], save_apk=len(sys.argv) > 2 and sys.argv[2] == 'save')
