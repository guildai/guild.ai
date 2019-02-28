function trySmoothScroll(href, pushHistory, topMargin) {
  if (href.charAt(0) === '#') {
    const target = $(href);
    if (target.length > 0) {
      if (pushHistory) {
        window.history.pushState(null, null, href);
      }
      var fixedHeaderHeight = $('.site-header.sticky').outerHeight();
      if (fixedHeaderHeight === undefined) {
        fixedHeaderHeight = $(window).width() < 768 ? 20 : 0;
      }
      const scrollTop = target.offset().top - (fixedHeaderHeight || 10);
      $('html, body').animate({scrollTop: scrollTop}, 300);
      return true;
    }
  }
  return false;
}

$(function() {

  "use strict";

  // Lazy image loading (lozad)

  lozad().observe();

  // Typed.js

  const typedEl = document.getElementById('typed');
  if (typedEl !== null) {
    const typed = new Typed(typedEl, {
      strings: [
        "guild run train.py",
        "guild run <span>train.py learning-rate=0.01</span>",
        "guild run <span>train.py learning-rate=[0.1,0.01,0.001]</span>",
        "guild run <span>train.py</span> --optimizer bayesian",
        "guild compare",
        "guild diff",
        "guild tensorboard",
      ],
      typeSpeed: 45,
      backSpeed: 20,
      backDelay: 2000,
      loop: true,
      showCursor: false,
      smartBackspace: true
    });
  }

  // Scroll to page links
  $('a').click(function(e) {
    if (e.target.getAttribute("role") == "tab") {
      return true;
    }
    const href = e.target.getAttribute('href');
    if (href && href !== '#') {
      if (trySmoothScroll(href, true)) {
        return false;
      }
    }
  });

  // Back to top
  $('#scroll-up').on('click', function() {
    $('html, body').animate({scrollTop : 0}, 400);
    return false;
  });

  // Top navbar

  if ($('.site-header').hasClass('sticky') && !$('.site-header').hasClass('navbar-sm')) {
    var navbar_lg = $('.site-header').hasClass('navbar-lg');
    $(window).on('scroll', function() {
      var offset = $('.site-header').offset().top + $('.site-header').height();
      if ($(window).scrollTop() > offset) {
        if (navbar_lg) {
          $('.site-header').removeClass('navbar-lg');
        }
        $('.site-header').addClass('navbar-sm');
      } else {
        if (navbar_lg) {
          $('.site-header').addClass('navbar-lg');
        }
        $('.site-header').removeClass('navbar-sm');
      }
    });
  }

  // Manage transparent navbar
  if ($('.site-header').hasClass('navbar-transparent') && $('.site-header').hasClass('sticky')) {

    if ($('.site-header > .banner').length == 0) {
      $('.site-header').removeClass('navbar-transparent');
    } else {
      if ($('.site-header').hasClass('sticky')) {
        $(window).on('scroll', function() {
          var offset = $('.site-header .navbar').height();
          if ($(window).scrollTop() > offset) {
            $('.site-header').removeClass('navbar-transparent')
          }
          else {
            $('.site-header').addClass('navbar-transparent')
          }
        });
      }
    }
  }

  // Sidebar

  var offcanvas_open = function() {
    $('body').addClass('open-sidebar');
    $('body').prepend('<div class="offcanvas-backdrop"></div>');
    setTimeout(function() {
      $('.offcanvas-backdrop').addClass('in');
    }, 0);
    $('html').css('overflow', 'hidden');
  }

  var offcanvas_close = function() {
    $('body').removeClass('open-sidebar');
    $('.offcanvas-backdrop').removeClass('in');
    setTimeout(function() {
      $('html').css('overflow', 'visible');
      $('.offcanvas-backdrop').remove();
    }, 250);
  }

  // Offcanvas
  $('[data-toggle="offcanvas"]').on('click', function () {
    if ($('body').hasClass('open-sidebar')) {
      offcanvas_close();
    } else {
      offcanvas_open();
    }
  });


  // Close offcanvas upon clicking on backdrop
  $(document).on('click', '.offcanvas-backdrop', function() {
    offcanvas_close();
  });


  // Close offcanvas in single page layouts upon clicking on a menu
  $('.nav.sidenav a').on('click', function() {
    offcanvas_close();
  });

  // Dropdown
  $('.sidenav.dropable > li > a').on('click', function(e) {

    if (0 < $(this).next("ul").length) {
      e.preventDefault();
    }

    if (0 == $(this).next("ul").length) {
      return;
    }

    if ($(this).hasClass('open')) {
      $(this).removeClass('open').next("ul").slideUp(200);
    } else {
      $(this).closest(".sidenav").find("> li > a").removeClass('open');
      $(this).closest(".sidenav").find("ul:visible").slideUp(200);
      $(this).addClass('open').next("ul").slideDown(200, function() {
        update_scrollbar();
      });
    }
  });

  $('.sidenav.dropable > li > a.active').addClass('open');
  $('.sidenav.dropable > li > ul').prev('a').addClass('has-child');

  // Inner menus dropable
  $('.sidenav .dropable a').on('click', function(e){

    if ( 0 < $(this).next("ul").length ) {
      e.preventDefault();
    }

    if ( 0 == $(this).next("ul").length ) {
      return;
    }

    if ( $(this).hasClass('open') ) {
      $(this).removeClass('open').next("ul").slideUp(200);
    } else {
      $(this).closest("ul").find("> li > a").removeClass('open');
      $(this).closest("ul").find("> li > ul:visible").slideUp(200);
      $(this).addClass('open').next("ul").slideDown(200, function() {
        update_scrollbar();
      });
    }
  });

  $('.sidenav .dropable a.active').addClass('open');
  $('.sidenav .dropable ul').prev('a').addClass('has-child');

  // Perfect scrollbar for sidebar
  $('.sidebar-boxed, .sidenav.sticky').perfectScrollbar({
    wheelSpeed: 0.4,
  });

  var update_scrollbar = function() {
    $('.sidebar-boxed, .sidenav.sticky').perfectScrollbar('update');
  }

  if ($(window).width() < 768) {
    $('.sidebar-boxed').removeClass('sidebar-dark');
  }

  // Sticky behaviour
  if ($('.sidenav').hasClass('sticky')) {
    $(window).on('scroll', function() {
      var $sidenav   = $('.sidenav'),
          offset     = $('.sidebar').offset(),
          offset_top = 0;

      if ($(window).scrollTop() > offset.top) {
        if ( $('.site-header.sticky').length ) {
          offset_top = 100;
        }
        $sidenav.css({ position: 'fixed', top: offset_top +'px' });
      } else {
        $sidenav.css('position', 'static');
      }

      // If we are in footer area
      if ($(window).scrollTop() + $(window).height() > $(document).height() - 80) {
        $sidenav.css('bottom', '80px');
        update_scrollbar();
      } else {
        $sidenav.css('bottom', '40px');
      }
    });
  }

  // Equal height

  $('.grid-view > li, .categorized-view > li, .promo.small-icon').matchHeight();
  $('.promo').matchHeight();

  // Code

  $('pre').each(function() {
    const pre = $(this);
    const code = pre.children('code');
    if (code.attr('class')) {
      const cls = code.attr('class').trim().toLowerCase();
      if (cls.startsWith("language-")) {
        const lang = cls.slice(9);
        pre.prepend('<span class="language-name">'+ lang +'</span>');
        if (lang == 'command') {
          pre.addClass('command-line');
          pre.attr('data-prompt', '$');
          // Hack data-output to hide prompt for command line
          // continuations
          const preLines = pre.text().split('\n');
          var outputLines = "";
          for (var i = 0; i < preLines.length; i++) {
            if (preLines[i].endsWith('\\')) {
              outputLines += "," + (i + 2);
            }
          }
          if (outputLines) {
            pre.attr('data-output', outputLines.slice(1));
          }
        }
        pre.hover(function() {
          pre.children('span.language-name').toggleClass('out');
        });
      }
    }
  });

  // Prism highlighting (run after we markup pre/code tags)

  Prism.highlightAll();

  $('pre .language-name').parent().on('scroll', function(){
    $(this).find('.language-name').css('transform', 'translate('+ $(this).scrollLeft() +'px, '+ $(this).scrollTop() +'px)');
  });

  // Set initial focus for modals
  $('.modal').on('shown.bs.modal', function () {
    $('.initial-focus').focus();
  });

  // Search

  var client = algoliasearch('I1IYALZNSK', '4863af8e5dd6e8d374f000181f8bd352');
  var index = client.initIndex('guild.ai');
  var search = algoliasearchHelper(client, 'guild.ai');

  search.on('result', function(content) {
    handleSearchResults(content);
  });

  var hitItem = function(hit) {
    return ''
      + '<li>'
      + '<h6><a href="' + hit.location
      + '" title="' + hit.location + '">'
      + hit._snippetResult.title.value
      + '</a></h6>'
      + '<p>' + hit._snippetResult.text.value + '</p>'
      + '</li>';
  };

  var pageItem = function(index, curPage) {
    return ''
      + '<li' + (index === curPage ? ' class="active"' : '') + '>'
      + '<a href="#nav-page-' + index + '">' + (index + 1) + '</a></li>';
  };

  var pageNavItem = function(type, active) {
    return ''
      + '<li class="' + (active ? '' : 'disabled') + '">'
      + '<a href="' + (active ? '#nav-' + type : '') + '"'
      + ' class="' + type +'"'
      + (active ? '' : ' tabindex="-1"') + '>'
      + '<i class="fa fa-angle-' + (type === 'previous' ? 'left' : 'right')
      + '"></i></a></li>';
  };

  var handleSearchResults = function(content) {
    $('#search-results').html(function() {
      return $.map(content.hits, hitItem);
    });
    $('#search-pages').html(function() {
      var items = [];
      items.push(pageNavItem('previous', content.page > 0));
      const maxPages = 10;
      const startPage = Math.max(
        0, content.page - parseInt(maxPages / 2)
          - (content.page === content.nbPages - 1 ? 1 : 0));
      const endPage = Math.min(
        startPage + parseInt(maxPages / 2) + 1,
        content.nbPages - 1);
      for (var i = startPage; i <= endPage; i++) {
        items.push(pageItem(i, content.page));
      }
      items.push(pageNavItem('next', content.page < content.nbPages - 1));
      return items;
    });
  };

  var clearSearch = function() {
    search.state.query = '';
    $('#search-input').val('');
    $('#search-results').empty();
    $('#search-pages').empty();
  }

  $('#search-input').on('keyup', function(e) {
    if (e.key !== 'Escape') {
      const val = $(this).val().trim();
      if (!val) {
        clearSearch();
      } else if (val != search.state.query) {
        search.setQuery(val).search();
      }
    }
  });

  $('#search-pages').on('click', 'a', function(e) {
    const target = $(e.target).closest('a');
    const href = target.attr('href');
    if (href.startsWith('#nav-page')) {
      search.setPage(href.slice(10)).search();
    } else if (href === '#nav-previous') {
      search.previousPage().search();
    } else if (href === '#nav-next') {
      search.nextPage().search();
    }
    return false;
  });

  // Close search and scroll to internal links
  $('#search-results').on('click', 'a', function(e) {
    const linkHref = e.target.href || '';
    const curHref = ''
          + window.location.protocol + '//'
          + window.location.host
          + window.location.pathname;
    if (linkHref.startsWith(curHref)) {
      const relPath = linkHref.slice(curHref.length);
      if (relPath.startsWith("#")) {
        $('#search-modal').modal('hide');
        trySmoothScroll(relPath, true);
        return false;
      }
    }
  });

  $('#search-modal').on('show.bs.modal', function () {
    clearSearch();
  });

  Mousetrap.bind(["/"], function() {
    if (!($('#search-modal').data('bs.modal') || {}).isShown) {
      $('#search-modal').modal('show');
    } else {
      $('#search-input').focus().select();
      return false;
    }
  });

  // Lightbox for figure images
  $('img.md').each(function() {
    const img = $(this);
    if (!img.hasClass("no-lightbox")) {
      const wrapper = $('<a>');
      wrapper.attr('href', img.attr('src') || img.attr('data-src'));
      wrapper.attr('data-featherlight', 'image');
      img.wrap(wrapper);
    }
  });

  // Scroll to location.hash - run this last to ensure any scripts
  // that effect layout are run before calculating top offsets for
  // targets.

  if (window.performance
      && window.performance.navigation.type
      != window.performance.navigation.TYPE_BACK_FORWARD)
  {
    // We get here only when we know the user hasn't gotten to the
    // page via next or back navigation. We don't want to scroll on
    // navigation to preserve the historic scroll position.
    trySmoothScroll(location.hash, false);
  }
});
