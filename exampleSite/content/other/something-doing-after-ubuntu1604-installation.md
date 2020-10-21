---
date: 2017-06-02 07:41:49
tags:
  - ubuntu
  - shadowsocks
  - polipo
  - terminal
title: 一些安装完Ubuntu 16.04需要做的事(网络设置)
---

最近不满足于在 `Windows` 的系统中使用虚拟机的 `Ubuntu` 了，所以我试着装了双系统，虽然有过种种挫折，甚至将引导弄坏了，不得不同时重新装了 `Windows` ，但最后还是装好了觊觎已久的我的第一个 `Linux` 系统—— `Ubuntu` 。下面是我重装一次 `Ubuntu` 后总结的装机后应该要做的事，就酱……

<!--more-->

## 安装 `Ubuntu 16.04`

感觉网上教程很多，但有些误区，毕竟有些资料有点老，所以稍微说说。

> 安装介质： U 盘(个人首推)
>
> 安装的系统： `Ubuntu 16.04 + Windows 10` (个人使用)
>
> U 盘刻录： [Rufus](https://rufus.akeo.ie/) (小巧简单)
>
> 个人硬件： 笔记本(`战神 Z6-SL7D1`)
>
> **温馨提示：请注意备份原系统和相关重要资料，以防各种意外发生……**

### `BIOS` 和 `UEFI` 的提醒

不要随意修改引导，随时记得备份，如果改坏了，可能需要重装系统。

- `BIOS` 引导方式是为了适应一些老机器，基本从现在往后买的机器应该不会有，但是之前的还是可能需要的。(说错别打我啊！)
- `BIOS` 主要区分与 `UEFI` 引导方式，如果你的电脑/笔记本是 `UEFI` 的，那就找个 `UEFI` 的安装教程最好。(虽然百度/谷歌查过，依稀记得说是启动系统的方式，区分于操作系统，具体区别可以自行百度/谷歌……)
- 两种教程的过程基本一致，只有在分区的时候可能设置的启动区不一样，可以自行对比，不知道怎么看自己是哪一种的，建议百度/谷歌查一下怎么看自己的启动方式，就酱……{=.=}！

### 装机后可能的错误

**不知道我是不是倒霉，其实我不是如你所想一次成功，然后捣鼓坏了，觉得好多事要每次装机都做，然后才记录一下。**

- 我因为上面的引导问题装过 **3** 次，终于理解了问题所在时，发现我以前重装的 `Windows 10` 引导是假冒的 `UEFI`的方式(没有 efi 分区，从系统盘的 boot 启动)，重装 `Windows 10`后，才最终正确安装 `Ubuntu 16.04` 。
- 我一晚上正确安装完 `Ubuntu 16.04` 后，觉得没问题就准备第二天起再看看……然后启动时一直有错误。。。我能怎么办，我也很绝望啊~
- 我的错误是
  - “BUG： soft lockup - CPU#5 stuck for 23s！”
  - 什么嘛，我又没编译内核啊，怎么会有这样的错误~
  - 最后我在重启数次无果，放弃后准备重装试试，先去上课了。中午回来继续试试时发现，居然打开了，我一脸懵啊！
  - 嗯，我的猜测是，我的 CPU 它需要一段时间的适应 `Ubuntu 16.04` ，就酱……(后期使用完全没事，不是这个问题的我也很难帮忙了，自行百度/谷歌吧)

## 网络设置

网络没了，怎么算用电脑(我知道我错了……但还好啦)

### 网卡设置

**注意： 本人没有这个问题，本人的笔记本是 `战神 Z6-SL7D1`，没有网卡驱动没有加载的问题。如果有这样的问题，可能需要插网线，或者手机用 USB 共享网络，然后从网上查一下具体的驱动并安装，具体教程请自行百度/谷歌，祝顺……**

### 更换下载源

- **备份源的配置文件**(以防万一……)

```bash
$ sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
```

- 编辑源的配置文件(可能没有安装 `vim` ，就用 `gedit` 也行，高手请出门左转……)

```bash
$ sudo gedit /etc/apt/sources.list
```

> 个人分享的源(其实也是查的)：[sources.list from gist](https://gist.github.com/yi-Xu-0100/b7de5b29ef9cf65ce58147cf5e4ebe21)

- 最后，别忘了更新一下源

```bash
$ sudo apt update
```

> 温馨提示：现在好像建议使用 `apt` 而不是 `apt-get` ，请注意跟上时代，貌似确实好点。

### 设置 ss 科学上网(个人使用)

有一些知识不得不说，百度给出的答案有点答非所问……

- 通过 pip 安装 shadowsocks :

```bash
$ sudo apt update
$ apt install python-pip
$ pip install shadowsocks
```

- 设置配置文件 :

```bash
$ sudo gedit etc/shadowsocks.json
```

文件内容基本格式如下：(具体内容请按照个人情况修改)

```json
{
  "server": "my_server_ip",
  "server_port": 8080,
  "local_address": "127.0.0.1",
  "local_port": 1080,
  "password": "mypassword",
  "timeout": 300,
  "method": "aes-256-cfb",
  "fast_open": false
}
```

- 部署 shadowsocks ，并设置开机自启 :

```bash
$ sslocal -c /etc/shadowsocks.json -d start
$ sudo gedit /etc/rc.local
```

> 如果这个文件打开后没有任何的引导语句，建议不保存并关闭。
>
> 最好 cd 到 etc/ 中去用 ls 看一看，如果没找到，也可能在 rc.d/ 中。

在 `exit 0` 的前面一行添加以下语句 :

```local
sudo /usr/local/bin/sslocal -c /etc/shadowsocks.json -d start
```

### 设置 web 使用

- 个人使用： `chorme`
- 浏览器是我们可视化查询网络资源的途径，设置好浏览器，那些设置会消失， `Google Chorme` 是很好的账户同步设置的方式。(前提：你使用 `Google` 账号以前在同步中)
- 安装 `Google Chorme` 的一般方案：
  - 网上下载安装包，然后本地安装，以下为安装命令：(抱歉本人不会源码编译安装。)
  - 在安装包所在位置使用命令：
  ```bash
  $ sudo dpkg -i google-chrome-stable_current_amd64.deb
  ```
  - 直接使用 `apt install` 安装。
  ```bash
  $ wget -q -O - http://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
  $ sudo sh -c 'echo"deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main">> /etc/apt/sources.list.d/google.list'
  $ sudo apt-get update
  $ sudo apt-get install google-chrome-stable
  ```

> 参考链接： [WTF Daily Blog-Ubuntu 16.04 安装 Google Chorme](http://blog.topspeedsnail.com/archives/4793)

- 安装 `SwitchOmega` 插件
  - 百度/谷歌搜索下载插件，安装后 `proxy` 中配置的代理端口，默认的话，应该为 `127.0.0.1` 和 `1080` 。
  - 如果要走 `PAC` 代理，建议百度/谷歌相关教程，配置 `AutoSwitch` 选项，当然也可以自己尝试。(这里提供 Rule list: <https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt>)

### 设置终端走代理

本人使用 `Atom` ，插件的源一直基本无法链接，遍寻结果后，，发现让终端走代理，然后直接用终端下载插件效果较好。

- 安装 `polipo`

```bash
$ sudo apt install polipo
```

- 打开 `polipo` 的 `config` 文件：

```bash
$ sudo gedit /etc/polipo/config
```

- 编辑 `config` 文件：

```json
# This file only needs to list configuration variables that deviate
# from the default values.  See /usr/share/doc/polipo/examples/config.sample
# and "polipo -v" for variables you can tweak and further information.
logSyslog = true
logFile = /var/log/polipo/polipo.log
logLevel=4
socksParentProxy = "localhost:1080"
socksProxyType = socks5
```

如果没有注释，可能你打开了错误的文档。

- 重新启动 `polipo` ：

```bash
$ sudo service polipo stop
$ sudo service polipo start
```

- 打开 bash 的设置

```bash
sudo gedit ~/.bashrc
```

- 修改配置(文档末尾添加)

```bash
#  add alias for proxy
alias hp="http_proxy=http://localhost:8123"
```

- 验证使用

```bash
$ curl ip.gs
Current IP / 当前 IP: 123.235.2.204
ISP / 运营商:  ChinaUnicom
City / 城市: Qingdao Shandong
Country / 国家: China
Please join Telegram group https://t.me/sbfans if you have any issues. / 如有问题，请加入 Telegram 群 https://t.me/sbfans
 /\_/\
=( °w° )=
 )   (  //
(__ __)//
$ hp curl ip.gs
Current IP / 当前 IP: 139.162.75.147
ISP / 运营商:  linode.com
City / 城市: Shinagawa Tokyo
Country / 国家: Japan
Please join Telegram group https://t.me/sbfans if you have any issues. / 如有问题，请加入 Telegram 群 https://t.me/sbfans
 /\_/\
=( °w° )=
 )   (  //
(__ __)//
```

> 温馨提示：如果没有效果，请关机重启后，重试。
>
> 参考链接：[为终端设置 Shadowsocks 代理 - 技术小黑屋](http://droidyue.com/blog/2016/04/04/set-shadowsocks-proxy-for-terminal/index.html)

## 总结

以上是我的网络设置之路,记录下来希望少走弯路。
