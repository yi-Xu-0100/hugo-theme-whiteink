#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
def deploy():
    try:
        os.system('hugo')
        os.chdir('public/')
        os.system('git init')
        os.system('git ')
        
    except Exception as e:
        print(e)
    
if __name__ = "__main__":
    