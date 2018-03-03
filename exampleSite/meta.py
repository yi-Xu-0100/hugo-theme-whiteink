# -*- coding: utf-8 -*-


__author__ = 'yi_Xu'


import os
import chardet
import yaml

def get_files_name(dir='./content'):
    content = os.walk(dir)
    for path,dir_list,file_list in content:
        for file_name in file_list:
            yield(os.path.join(path, file_name))

def get_charset(dir):
    with open(dir, "rb") as f:
        data = f.read()
    return chardet.detect(data)

def get_meta_data(dir='./content/'):
    for file in get_files_name(dir=dir):
        meta_data = ''
        with open(file, 'r', encoding=get_charset(file)['encoding']) as f:
            start = False
            for line in f:
                if start == False:
                    if ((line == '---\n') or (line == '---\r\n')):
                        start = True
                else:
                    if ((line == '---\n') or (line == '---\r\n')):
                        break
                    else:
                        meta_data += line
        yield file, yaml.load(meta_data)

def change_meta_data(file, change_meta_data=''):
    meta_data = ''
    data = ''
    with open(file, 'rU', encoding=get_charset(file)['encoding']) as f:
        start = False
        content = False
        for line in f:
            if content == True:
                data += line
            if start == False:
                if ((line == '---\n') or (line == '---\r\n')):
                    start = True
            else:
                if ((line == '---\n') or (line == '---\r\n')):
                    content = True
                    start = False
                else:
                    meta_data += line
    if change_meta_data != '':
        try:
            os.remove(file)
        except Exception:
            print("remove {file} fail ".format(file=file))
            raise
        with open(file, 'w', encoding='utf-8') as f:
            f.write('---\n')
            f.write('{meta_data}'.format(meta_data=change_meta_data))
            f.write('---\n\n')
            f.write('{content}'.format(content=data))

def delete_meta_key(key, meta):
    try:
        meta.pop(key)
    except KeyError:
        pass
    finally:
        return meta

if __name__ == "__main__":
    for data in get_meta_data():
        print(data[0])
        fix_meta = data[1]

        # delete categories, fancebox, toc, donate, type, comments
        fix_meta = delete_meta_key('categories',fix_meta)
        fix_meta = delete_meta_key('fancebox',fix_meta)
        fix_meta = delete_meta_key('toc',fix_meta)
        fix_meta = delete_meta_key('donate',fix_meta)
        fix_meta = delete_meta_key('type',fix_meta)
        fix_meta = delete_meta_key('comments',fix_meta)

        # change tags to []
        try:
            if type(fix_meta['tags']) != str:
                fix_meta['tags'] = ','.join(fix_meta['tags'])
        except KeyError:
            fix_meta['tags'] = ''
        finally:
            fix_meta['tags'] = fix_meta['tags'].lower()
            fix_meta['tags'] = fix_meta['tags'].split(',')
            if fix_meta['tags'] == ['']:
                fix_meta.pop('tags')
        meta_data = yaml.dump(fix_meta, allow_unicode=True, \
                              indent=2, default_flow_style=False)

        # write change to md
        change_meta_data(data[0], change_meta_data=meta_data)
        print(fix_meta)