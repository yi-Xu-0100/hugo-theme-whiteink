+++
categories = ["其他分享", "学习思考"]
date = "2017-07-23 14:22:28"
tags = ["Python3", "Python2", "Print", "Input"]
title = "Python 中的 Print"

+++

编程语言学习之旅总是从各种 Print 和 Input 语句中开始， Python 也不例外，那你能看出什么问题呢？没有？那我提几个吧……
<!--more-->

## Python 中的一般 Print 的语法
### 对单引号('')和双引号("")的显示问题
 print 需要用引号来标记输出信息，但如果输出中含有单引号或者双引号时，有时需要转义。
``` python
 >>> print "I don't like Tony's dog."
 I don't like Tony's dog.
 >>> print 'I don"t like Tony"s dog.'
 I don"t like Tony"s dog.
```
上述例子可以看出，对于两边的引号， Python 会将其默认为标记符，只要句子中的引号和标记符不同，可以不使用转义。
``` python
>>> print "I don't like Tony's dog, But Tony said that I don't care you."
I don't like Tony's dog, But Tony said that I don't care you.
>>> print "I don't like Tony's dog, But Tony said : I don't care you."
I don't like Tony's dog, But Tony said : I don't care you.
>>> print "I don't like Tony's dog, But Tony said: "I don't care you.""
  File "<stdin>", line 1
    print "I don't like Tony's dog, But Tony said: "I don't care you.""
                                                    ^
SyntaxError: invalid syntax
>>> print "I don't like Tony's dog, But Tony said: \"I don't care you.\""
I don't like Tony's dog, But Tony said: "I don't care you."
```
上述例子看出，如何两边默认的标记符中出现相同的标记符，需要加上转义符号(\\)。当然要显示(\\)，需要使用(\\\\)。

|     转义字符     |    描述    |
|:---------------:|:----------:|
|\\(在行尾时)|续行符|
|\\\\	|反斜杠符号|
|\\'	|单引号|
|\\"	|双引号|
|\\a	|响铃|
|\\b	|退格 (Backspace)|
|\\e	|转义|
|\\000	|空|
|\\n	|换行|
|\\v	|纵向制表符|
|\\t	|横向制表符|
|\\r	|回车|
|\\f	|换页|
|\\oyy	|八进制数 yy 代表的字符，例如：\\o12 代表换行|
|\\xyy	|十进制数 yy 代表的字符，例如：\\x0a 代表换行|
|\\other	|其它的字符以普通格式输出|

### Print 中 %s 和 %r 的区别
``` python
>>> print "Good %s!" % 'luck'
Good luck!
>>> print "Good %r!" % 'luck'
Good 'luck'!
>>> print "Good %r!" % "luck"
Good 'luck'!
>>> print "Hi,%s!" % "Tom's son"
Hi,Tom's son!
>>> print "Hi,%r!" % "Tom's son"
Hi,"Tom's son"!
```
可以看出， %s 输出为你想要输出的内容，而 %r 输出为原始内容。

### input() 和 raw_input() 的区别

``` python
input(...)
    input([prompt]) -> value

    Equivalent to eval(raw_input(prompt)).
(END)
raw_input(...)
    raw_input([prompt]) -> string

    Read a string from standard input.  The trailing newline is stripped.
    If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
    On Unix, GNU readline is used if enabled.  The prompt string, if given,
    is printed without a trailing newline before reading.
(END)
```
上述由 pydoc 得到。

``` python
>>> input()
2
2
>>> raw_input()
2
'2'
>>> input(),2
2
(2, 2)
>>> raw_input(),2
2
('2', 2)
>>> [input(),2]
2
[2, 2]
>>> [raw_input(),2]
2
['2', 2]
```

不知道你发现了什么没有，希望你能够理解。比较不同哦。

### 相关说明

- 上述代码在 Python2.7.12环境下测试
- 【2017-08-16 19:09:15】更新： python3+ 仅支持input()
