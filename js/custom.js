$(document).ready(function () {
  // 置顶设置
  $(window).scroll(function () {
    if ($(window).scrollTop() > 60) {
      $('.gotop').show();
    } else {
      $('.gotop').hide();
    }
  });
  $('.gotop').click(function () {
    $('html, body').animate({ scrollTop: 0 }, 300);
  });

  // 头像抖动设置
  $('#avatar-img').mouseenter(function () {
    $('#avatar-img').removeClass('zoomIn');
    $('#avatar-img').addClass('headShake');
  });
  $('#avatar-img').mouseleave(function () {
    $('#avatar-img').removeClass('headShake');
  });

  // 移动端页面设置
  $('#mobile-navbar').click(function () {
    $('#jquery-menu').toggle(500);
    $('header').toggleClass('mobile-header');
    $('#site-title').toggleClass('mobile-title');
    $('.mobile-navbar').toggleClass('mobile-title');
  });
  $('#mobile-toc-title').click(function () {
    $('#mobile-toc').toggle(500);
    $('#down-up').toggleClass('icon-double-angle-down');
    $('#down-up').toggleClass('icon-double-angle-up');
  });
  $('#mobile-toc-title').mouseleave(function () {
    $('#down-up').removeClass('icon-double-angle-up');
    $('#down-up').addClass('icon-double-angle-down');
    $('#mobile-toc').hide();
  });
  $('#mobile-toc-title a').click(function () {
    $('#jquery-menu').toggle(500);
    $('header').toggleClass('mobile-header');
    $('#site-title').toggleClass('mobile-title');
    $('.mobile-navbar').toggleClass('mobile-title');
  });
  $('header').headroom();
  $('#mobile-avatar').headroom();
  $('#gotop').headroom();

  // 剪贴板设置
  // eslint-disable-next-line no-undef
  var clipboard = new ClipboardJS('.copy-path');

  clipboard.on('success', function (e) {
    console.info('Action:', e.action);
    console.info('Text:', e.text);
    console.info('Trigger:', e.trigger);
    alert('copied!');

    e.clearSelection();
  });

  clipboard.on('error', function (e) {
    console.error('Action:', e.action);
    console.error('Trigger:', e.trigger);
    alert('error!');
  });
});
