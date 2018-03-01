+++
categories = "其他分享"
date = "2017-03-25 09:17:43"
tags = ["Hexo", "Yelee", "Simiki", "Github"]
title = "Hello World"

+++

这本是`Hexo`搭建博客时自动生成的页面，我将其搬运到我的[`Wiki`](https://wiki.yixuju.cn/Introduction/getting-started-for-hexo.html)中，并在此处填写我的填坑之旅。
<!--more-->
## 基于`Hexo+Github`搭建博客
基于`Hexo+Github`搭建博客，你可以从参考的相关文章在[`Baidu`](https://www.baidu.com/baidu?tn=64075107_1_dg&ie=utf-8&wd=%E5%9F%BA%E4%BA%8EHexo%2BGithub%E6%90%AD%E5%BB%BA%E5%8D%9A%E5%AE%A2)或[`Google`](https://www.google.com/search?q=%E5%9F%BA%E4%BA%8EHexo%2BGithub%E6%90%AD%E5%BB%BA%E5%8D%9A%E5%AE%A2&oq=%E5%9F%BA%E4%BA%8EHexo%2BGithub%E6%90%AD%E5%BB%BA%E5%8D%9A%E5%AE%A2&aqs=chrome..69i57j69i65l2j69i60.8760j0j4&sourceid=chrome&ie=UTF-8)上一找一大堆，我就不在此处赘述了。

>我的参考链接如下：
>
>[教你免费搭建个人博客，Hexo&Github](https://zhuanlan.zhihu.com/p/25729240)
>
>[最简便的方法搭建Hexo+Github博客,基于Next主题](http://chaserr.github.io/2016/06/01/%E6%9C%80%E7%AE%80%E4%BE%BF%E7%9A%84%E6%96%B9%E6%B3%95%E6%90%AD%E5%BB%BAHexo-Github%E5%8D%9A%E5%AE%A2-%E5%9F%BA%E4%BA%8ENext%E4%B8%BB%E9%A2%98/#more)
>
> [GITHUB PAGES + HEXO 搭建博客从入门到进阶](https://munen.cc/tech/hexo-init.html)


我仅在此留下我在搭建博客中遇到的一些问题，并给出相关解决方案。
### 题材选择
>* 博主仅使用[`Hexo`](https://hexo.io/)搭建了个人博客，不了解其他的搭建过程，请恕我不能帮忙解答其他相关搭建方法的问题。
>* 博主仅使用[`Simiki`](http://simiki.org/)搭建了个人Wiki，其他同上。
>* 博主仅使用[`Yelee`](https://github.com/MOxFIVE/hexo-theme-yelee)作为个人博客的主题，其他同上。
>* 博主仅使用[`Sample2`](https://github.com/tankywoo/simiki-themes)的作为个人Wiki的主题，其他同上。

### Github Pages的准备
>* 温馨提示：`username`请务必认真选择，毕竟改掉会影响很多的内容。
>* [`Github`](https://github.com)网站页面为全英文的，**如非强烈必要，请勿用全网页翻译**，影响理解和使用，个别单词不认识，查一查正好可以扩充一下词汇量嘛。

### 环境准备
>* `Git`虽说是初次接触，但我非常喜欢他的版本管理，喜欢它的观念，使用教程参考[Git教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)。
>* `Node.js`我并不了解，以后要是能够学到，或有更多的接触，再来添加相关建议。
>* `Atom`是一款编辑器，目录树我非常喜欢，介绍请参考[新编码神器Atom使用纪要](http://jeffjade.com/2016/03/03/2016-03-02-how-to-use-atom/)和[中文Atom社区](https://atom-china.org/)。
>* `Markdown`自接触之后非常喜欢，在线编辑可选[作业部落](https://www.zybuluo.com/mdeditor)，语法说明见[Markdown中文简明语法](http://wowubuntu.com/markdown/)。

### 域名相关
>* **域名购买建议慎重，毕竟花钱**。考虑好，做过的事不后悔就行。对了，如要购买，可以网上找找优惠码，你要买的域名在任何域名发售商那都是可以购买的，买完之后，别人就不能购买你的域名了，当然别忘了续费。
>* 你可以解析不同的页面地址到你的域名下，我同时部署在[`Github Pages`](https://pages.github.com/)和[`Coding Pages`](https://coding.net/help/doc/pages/index.html)上，但显示内容只有`Coding Pages`的内容，但我还是一直部署两个在，感觉以后弄懂再说。

### 主题选择
>* 主题选择看自己喜欢，主题配置找该主题的教程就行，大部分都非常详细。实在不行，去`Github`上提issue，作者或其他热心人会很乐意回答你的。这是[我的主题Yelee配置教程](http://moxfive.coding.me/yelee/)。

个人对主题的小修改如下：

>* **下方的`Copy`改成`Copyright`**。以下为解决方案：
在`themes\yelee\layout\_partial\footer.ejs`中找到以下内容：
>``` js
<div class="footer-left">
  <i class="fa fa-copyright"></i>
    <% if (theme.since && !isNaN(theme.since) && theme.since < date(new Date(), 'YYYY')) { %><%- theme.since%>-<% } %><%= date(new Date(), 'YYYY') %> <%= config.author || config.title %>
</div>
```
>将内容修改为：
>``` js
<div class="footer-left">
    Copyright
    <i class="fa fa-copyright"></i>
    <% if (theme.since && !isNaN(theme.since) && theme.since < date(new Date(), 'YYYY')) { %><%- theme.since%>-<% } %><%= date(new Date(), 'YYYY') %> <%= config.author || config.title %>
</div>
```

>* **添加打赏功能**，教程参考：[为Hexo博客添加版权说明和打赏功能](http://colin1994.github.io/2016/06/02/hexo-copyright-and-donate/)，当然我只是选取其中部分进行匹配我的需要。以下为解决方案：
>在`themes\yelee\_config.yml`中添加以下内容：
>``` yaml
#打赏
donate:
  on: true
  text: 如果觉得我的文章有值得赞赏的地方，可以给予支持！
  wechat:
  #此处填上你的微信支付图片地址。
  alipay:
  #此处填上你的支付宝支付图片地址。
```
>在`themes\yelee\layout\_partial\article.ejs`找到以下内容：
>``` js
<% if (!index && theme.share.on && (post.share != false || post.share)){ %>
  <%- partial('post/share') %>
<% } %>
```
>在这个的上面加上以下内容：
>``` js
<% if (!index && theme.donate.on && (post.donate != false || post.donate)){ %>
  <% if (theme.donate) { %>
      <!-- css -->
      <style type="text/css">
          .center {
              text-align: center;
          }
          .hidden {
              display: none;
          }
        .donate_bar a.btn_donate{
          display: inline-block;
          width: 82px;
          height: 82px;
          background: url("http://7xsl28.com1.z0.glb.clouddn.com/btn_reward.gif") no-repeat;
          _background: url("http://7xsl28.com1.z0.glb.clouddn.com/btn_reward.gif") no-repeat;

          <!-- http://img.t.sinajs.cn/t5/style/images/apps_PRF/e_media/btn_reward.gif
               因为本 hexo 生成的博客所用的 theme 的 a:hover 带动画效果，
             为了在让打赏按钮显示效果正常 而 添加了以下几行 css，
             嵌入其它博客时不一定要它们。 -->
          -webkit-transition: background 0s;
          -moz-transition: background 0s;
          -o-transition: background 0s;
          -ms-transition: background 0s;
          transition: background 0s;
          <!-- /让打赏按钮的效果显示正常 而 添加的几行 css 到此结束 -->
        }

        .donate_bar a.btn_donate:hover{ background-position: 0px -82px;}
        .donate_bar .donate_txt {
          display: block;
          color: #9d9d9d;
          font: 14px/2 "Microsoft Yahei";
        }
        .bold{ font-weight: bold; }
      </style>
      <!-- /css -->

        <!-- Donate Module -->
    <div id="donate_module">

      <!-- btn_donate & tips -->
      <div id="donate_board" class="donate_bar center">
          <br>
          ------------------------------------------------------------------------------------------------------------------------------
          <br>
        <a id="btn_donate" class="btn_donate" target="_self" href="javascript:;" title="Donate 打赏"></a>
        <span class="donate_txt">
          <%= theme.donate.text %>
        </span>


      </div>
      <!-- /btn_donate & tips -->

      <!-- donate guide -->

      <div id="donate_guide" class="donate_bar center hidden">
            <br>
          ------------------------------------------------------------------------------------------------------------------------------
          <br>

        <a href="<%= theme.donate.wechat %>" title="用微信扫一扫哦~" class="fancybox" rel="article0">
          <img src="<%= theme.donate.wechat %>" title="微信打赏 yi_Xu" height="190px" width="auto"/>
        </a>

            &nbsp;&nbsp;

        <a href="<%= theme.donate.alipay %>" title="用支付宝扫一扫即可~" class="fancybox" rel="article0">
          <img src="<%= theme.donate.alipay %>" title="支付宝打赏 yi_Xu" height="190px" width="auto"/>
        </a>

        <span class="donate_txt">
          <%= theme.donate.text %>
        </span>

      </div>
      <!-- /donate guide -->

      <!-- donate script -->
      <script type="text/javascript">
        document.getElementById('btn_donate').onclick = function() {
          $('#donate_board').addClass('hidden');
          $('#donate_guide').removeClass('hidden');
        }

        function donate_on_web(){
          $('#donate').submit();
            }

        var original_window_onload = window.onload;
            window.onload = function () {
                if (original_window_onload) {
                    original_window_onload();
                }
                document.getElementById('donate_board_wdg').className = 'hidden';
        }
      </script>
      <!-- /donate script -->
    </div>
  <% }%>
<% }%>
```
>效果显示见文章下方。
>
>* **保持图片居中**，主题默认不居中，我参考了主题中的[issue#87](https://github.com/MOxFIVE/hexo-theme-yelee/issues/87)。以下为解决方案:
> 在`\themes\yelee\source\css\_partial\article.styl`的末尾添加：
> ``` css
.article img {display: block;}
```
