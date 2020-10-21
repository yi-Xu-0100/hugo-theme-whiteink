---
date: '2018-01-08'
tags:
  - python3
  - html
  - csv
title: python实现HTML的表格转csv
---

个人需要整一张网页上的表格，不好的我需要保留网页的表格样式，我试着去提取网页中的内容，写了点代码，做为参考。

<!--more-->

```python
    # -*- coding: utf-8 -*-


    __author__ = 'yi_Xu'


    from bs4 import BeautifulSoup
    import pandas as pd
    import os

    class getPage(object):
        def __init__(self, src = os.path.join(".",'html', 'page1.html'), classname = "", backup_name = "", csv_name = ""):
            self.src = src
            self.classname = classname
            self.filename = os.path.split(src)[1]
            self.backup_name = (backup_name or self.filename[:-5] + '_change.html')
            self.csv_name = (csv_name or self.filename[:-5] + '_modify.csv')
            self.page_html = self._get_page()
            self.page_table = self._get_table()

        def _get_page(self, src = ""):
            with open((src or self.src), mode = "r") as f:
                html_code = f.read()
                return BeautifulSoup(html_code, "html.parser")

        def modify_backup(self, html_code, backup_src = ""):
            with open((backup_src or os.path.join(".", 'result', self.backup_name)), mode = "w", encoding="utf-8") as f:
                f.write(html_code.prettify())

        def modify_table(self, result = ""):
            page_html = self.page_html
            table = page_html.tr
            csv_src = os.path.join(".", 'csv', self.csv_name)
            df= pd.read_csv(csv_src,encoding = "utf-8", header = None)
            count = 0
            tables = []
            while (table != None):
                for column_number, child in enumerate(table.children):
                    child.string = str(df.iloc[count][column_number])
                table = table.find_next_sibling("tr")
                count = count + 1
            self.modify_backup(page_html)

        def _get_table(self, csv_src = ""):
            table = self.page_html.tbody.tr
            csv_src = (csv_src or os.path.join(".", 'csv', self.csv_name))
            count = 0
            tables = []
            while (table != None):
                for column_number, child in enumerate(table.children):
                    tables.append((count, column_number, child.string))
                table = table.find_next_sibling("tr")
                count = count + 1
            data= [['*' for i in range(column_number + 1)] for i in range(count + 1)]
            for key in tables:
                data[key[0]][key[1]] = key[2]
            df = pd.DataFrame(data = data)
            if os.path.exists(csv_src) == False:
                df.to_csv(csv_src,index=False, header = False, encoding = "utf-8")
            return df


    if __name__ == "__main__":
        page = getPage(src = './html/page1.html')
        print(page.page_table)
        #page.modify_table(result = './result/page1.html')

```
