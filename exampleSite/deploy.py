#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import datetime
def onerror(func, path, exc_info):
    """
    Error handler for ``shutil.rmtree``.

    If the error is due to an access error (read only file)
    it attempts to add write permission and then retries.

    If the error is for another reason it re-raises the error.

    Usage : ``shutil.rmtree(path, onerror=onerror)``
    """
    import stat
    if not os.access(path, os.W_OK):
        # Is the error an access error ?
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        rais

def message(words):
    return "\n*****************************************************************\n\t\t {words}\n*****************************************************************\n".format(words=words)

def deploy(repo):
    if os.path.exists('./public/'):
        print(message('清空 public 目录！'))
        shutil.rmtree('./public/', onerror=onerror)
    else:
        try:
            print(message('执行 hugo 生成站点！'))
            os.system('hugo')
            os.chdir('./public/')
            print(message('初始化 git ！'))
            os.system('git init')
            os.system('git checkout -b gh-pages')
            os.system('git add --all')
            os.system('git commit -m "Rebuild site at {now}"'.format(now=datetime.datetime.now()))
            print(message('向远程库（{repo}）推送！'.format(repo=repo))
            os.system('git remote add origin {repo}'.format(repo=repo)
            os.system('git push -f origin gh-pages:gh-pages')
        except Exception as e:
            print(e)
    
if __name__ == "__main__":
    deploy('git@github.com:yi-Xu-0100/hugo-theme-whiteink.git')