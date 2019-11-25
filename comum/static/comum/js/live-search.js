$('.live-search-list li').each(function(){
  $(this).attr('data-search-term', $(this).children().children().next().text().toLowerCase());
});

$('.live-search-box').on('keyup', function(){
  var searchTerm = $(this).val().toLowerCase();

  $('.live-search-list li').each(function(){
      if ($(this).filter('[data-search-term *= ' + searchTerm + ']').length > 0 || searchTerm.length < 1) {
          $(this).show();
      } else {
          $(this).hide();
      }
  });
});
