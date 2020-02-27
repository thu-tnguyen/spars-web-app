$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });

  });

  $(document).ready(function () {

  $("#sidebar").mCustomScrollbar({
      theme: "minimal"
  });

  $('#sidebarCollapse').on('click', function () {
      // open or close navbar
      $('#sidebar').toggleClass('active');
      // close dropdowns
      $('.collapse.in').toggleClass('in');
      // and also adjust aria-expanded attributes we use for the open/closed arrows
      // in our CSS
      $('a[aria-expanded=true]').attr('aria-expanded', 'false');
  });

  });

  $('.list-group-item .custom-control-label').on('click', function(){
    var checkBox = $(this).prev('input'); 
    
    if($(checkBox).attr('checked'))
      $(checkBox).removeAttr('checked');
    else
      $(checkBox).attr('checked', 'checked');
      
    return false;

  })