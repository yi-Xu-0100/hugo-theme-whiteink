---
date: '2017-08-17 13:19:48'
tags:
- python3
- log
- yaml
title: Python3 中的 log 文件配置方法
---


Python 中有好用的 logging 模块，方便我们为程序添加 log 输出，我一直希望能够写个小程序，现在的现在有个小的关于数据提取的小程序，我希望能够提取相关数据，但是用 print 的方式来观察输出实在是忧伤，所以我试着配置了 log ，问题出现了，我希望同时输出到控制台和文件中保存，恩，怎么配置呢?
<!--more-->

### 问题描述

根据 `logconfig.yaml` 文件，配置log，测试模块文件。

### 问题背景
>此处引用输出级别描述：
>
>作者：好吃的野菜
>
>链接：http://www.jianshu.com/p/feb86c06c4f4
>
>來源：简书
>
>著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

 |     输出级别     |    描述    |
 |:---------------:|:----------:|
 |级别|何时使用|
 |DEBUG|详细信息，典型地调试问题时会感兴趣。|
 |INFO|证明事情按预期工作。|
 |WARNING|表明发生了一些意外，或者不久的将来会发生问题（如‘磁盘满了’）。软件还是在正常工作。|
 |ERROR|由于更严重的问题，软件已不能执行一些功能了。|
 |CRITICAL|严重错误，表明软件已不能继续运行了。|

从上往下，信息级别依次升高！

可采用的 `format` 格式关键词：

|关键词|描述|
|:---------------:|:----------:|
|%(levelno)s|打印日志级别的数值|
|%(levelname)s|打印日志级别名称|
|%(pathname)s|打印当前执行程序的路径|
|%(filename)s|打印当前执行程序名称|
|%(funcName)s|打印日志的当前函数|
|%(lineno)d|打印日志的当前行号|
|%(asctime)s|打印日志的时间|
|%(thread)d|打印线程 id|
|%(threadName)s|打印线程名称|
|%(process)d|打印进程 ID|
|%(message)s|打印日志信息|

### 配置文件

``` yaml
version: 1
```

`version` 键值为 1 ，表示启用这个配置。

``` yaml
formatters:
    simple:
        format: '%(asctime)s - %(filename)s - %(lineno)d - [%(levelname)s] %(message)s'
```

`formatters` 键值中需要有对应的 `format` 设置，可自定义 `format` 。
`datefmt` 格式采用 `time.strftime` 标准模式，此处不设置，自动启用默认。

``` yaml
handlers:
    console:
        class: logging.StreamHandler
        level: WARNING
        formatter: simple
        stream: ext://sys.stdout
    logfile:
        class: logging.handlers.RotatingFileHandler
        level: DEBUG
        formatter: simple
        filename: log.log
        maxBytes: 10485760
        backupCount: 3
```

`Handlers` 是处理 `log` 的处理器，主要配置输出模式，这里我设置两种模式，控制台（ `console` ）和日志文件（ `logfile` ）。

`class` 设定log采用的输出模式，不同的 `class` 有着不同的参数， `lever` 指定处理器处理的最小级别。


-  `StreamHandler` 是流输出模式，此处特殊设置流的去处 `stream` 为 `ext：//sys.stdout` , `sys.stdout` 是控制台输出位，加上 `ext：//` 是为了让 `Yaml` 识别。


-  `RotatingFileHandler` 是循环文件模式，此处特殊设置 `filename` 、 `maxBytes` 、 `backupCount` 的参数。其中 `filename` 指定保存文件的名称， `maxBytes` 指定文件大小的最大值， `backupCount` 指定文件保存数目的最大值，以序号标注，如果超过次数目，默认删掉最早的，更新文件名。


``` yaml
loggers:
    logger:
        level: INFO
        handlers: [logfile]
        propagate: yes
root:
    level: WARNING
    handlers: [console]
```

`loggers` 指定自定义的 `log` 名称，此处设置名称为 `logger` ，`propagate` 指定是否将信息传到其他 `loggers` ，这里设置为 `yes` ，这样logger接收到的错误信息可以传到 `root` 那里， 以供显示输出。

完整配置文件（ `logconfig.yaml` ）如下

``` yaml
version: 1
formatters:
    simple:
        format: '%(asctime)s - %(filename)s - %(lineno)d - [%(levelname)s] %(message)s'
handlers:
    console:
        class: logging.StreamHandler
        level: WARNING
        formatter: simple
        stream: ext://sys.stdout
    logfile:
        class: logging.handlers.RotatingFileHandler
        level: DEBUG
        formatter: simple
        filename: log.log
        maxBytes: 10485760
        backupCount: 3
loggers:
    logger:
        level: INFO
        handlers: [logfile]
        propagate: yes
root:
    level: WARNING
    handlers: [console]
```

### `main.py` 文件中导入配置文件

`main.py` 中使用函数导入文件

``` python
import logging
import logging.config
import yaml
def setup_logging(default_path = "./logconfig.yaml",default_level = logging.INFO,env_key = "LOG_CFG"):
    path = default_path
    value = os.getenv(env_key,None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path,"r") as f:
            config = yaml.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level = default_level)
if __name__ == '__main__':
    setup_logging(default_path = "./logconfig.yaml")
    logger = logging.getLogger("logger")

#测试
    logger.debug("测试debug")
    logger.info("测试info")
    logger.warn("测试warn")
    logger.error("测试error")
    logger.critical("测试critical")
```

控制台输出如下：

``` bash
2017-08-17 20:32:11,723 - main.py - 39 - [WARNING] 测试warn
2017-08-17 20:32:11,724 - main.py - 40 - [ERROR] 测试error
2017-08-17 20:32:11,724 - main.py - 41 - [CRITICAL] 测试critical
```

`log.log` 文件输出如下：

``` bash
2017-08-17 20:32:11,723 - main.py - 38 - [INFO] 测试info
2017-08-17 20:32:11,723 - main.py - 39 - [WARNING] 测试warn
2017-08-17 20:32:11,724 - main.py - 40 - [ERROR] 测试error
2017-08-17 20:32:11,724 - main.py - 41 - [CRITICAL] 测试critical
```

### 模块引入配置
如果模块文件需要引入 `log` 配置，
如下使用：

`test.py` 内容如下：

``` python
import logging
logger = logging.getLogger("logger")

def test()
    logger.debug("测试debug")
    logger.info("测试info")
    logger.warn("测试warn")
    logger.error("测试error")
    logger.critical("测试critical")
```

`main.py` 内容如下：

``` python
import test
import logging
import logging.config
import yaml
def setup_logging(default_path = "./logconfig.yaml",default_level = logging.INFO,env_key = "LOG_CFG"):
    path = default_path
    value = os.getenv(env_key,None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path,"r") as f:
            config = yaml.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level = default_level)

if __name__ == '__main__':
    setup_logging(default_path = "./logconfig.yaml")
    logger = logging.getLogger("logger")

#测试
    logger.debug("测试debug")
    logger.info("测试info")
    logger.warn("测试warn")
    logger.error("测试error")
    logger.critical("测试critical")
    test.test()
```

控制台输出如下：

``` bash
2017-08-17 20:45:40,586 - main.py - 40 - [WARNING] 测试warn
2017-08-17 20:45:40,586 - main.py - 41 - [ERROR] 测试error
2017-08-17 20:45:40,587 - main.py - 42 - [CRITICAL] 测试critical
2017-08-17 20:45:40,587 - test.py - 17 - [WARNING] 测试warn
2017-08-17 20:45:40,587 - test.py - 18 - [ERROR] 测试error
2017-08-17 20:45:40,587 - test.py - 19 - [CRITICAL] 测试critical
```

`log.log` 输出如下：

``` bash
2017-08-17 20:45:14,225 - main.py - 39 - [INFO] 测试info
2017-08-17 20:45:14,225 - main.py - 40 - [WARNING] 测试warn
2017-08-17 20:45:14,225 - main.py - 41 - [ERROR] 测试error
2017-08-17 20:45:14,225 - main.py - 42 - [CRITICAL] 测试critical
2017-08-17 20:45:40,586 - main.py - 39 - [INFO] 测试info
2017-08-17 20:45:40,586 - main.py - 40 - [WARNING] 测试warn
2017-08-17 20:45:40,586 - main.py - 41 - [ERROR] 测试error
2017-08-17 20:45:40,587 - main.py - 42 - [CRITICAL] 测试critical
2017-08-17 20:45:40,587 - test.py - 16 - [INFO] 测试info
2017-08-17 20:45:40,587 - test.py - 17 - [WARNING] 测试warn
2017-08-17 20:45:40,587 - test.py - 18 - [ERROR] 测试error
2017-08-17 20:45:40,587 - test.py - 19 - [CRITICAL] 测试critical
```

### 解决模块引入配置的问题

模块引入 `log` 后，`log.log` 的信息有重复。

修复方法：
`logconfig.yaml` 文件添加一条配置
``` yaml
disable_existing_loggers: False
```

`log.log` 输出如下：

``` log
2017-08-17 20:57:32,535 - main.py - 39 - [INFO] 测试info
2017-08-17 20:57:32,535 - main.py - 40 - [WARNING] 测试warn
2017-08-17 20:57:32,536 - main.py - 41 - [ERROR] 测试error
2017-08-17 20:57:32,536 - main.py - 42 - [CRITICAL] 测试critical
2017-08-17 20:57:32,536 - test.py - 16 - [INFO] 测试info
2017-08-17 20:57:32,536 - test.py - 17 - [WARNING] 测试warn
2017-08-17 20:57:32,536 - test.py - 18 - [ERROR] 测试error
2017-08-17 20:57:32,536 - test.py - 19 - [CRITICAL] 测试critical
```

问题解决，控制台输出同上。

### 其他补充


- `logconfig.yaml` 配置文件对大小写敏感。


- `logconfig.yaml` 配置文件使用缩进确认键值包含关系。


- `logconfig.yaml` 配置文件中同样的缩进表示同一级别键值。


- `logconfig.yaml` 配置文件键值冒号后需要一个空格！


- 本文仅提供配置文件的部分参数介绍，需要了解详情，建议参考 [Python 3.5.2 标准库 logging 模块文档（中文）](http://python.usyiyi.cn/documents/python_352/library/logging.html#logging-levels) 。
