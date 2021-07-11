$(document).ready(function () {
    $(".nav-link").click(function () {
        $(this).siblings(".nav-treeview").slideToggle(300);
        if($(this).parent().hasClass("menu-open")) {
            $(this).parent().removeClass("menu-open");
            $(this).removeClass("active");
        } else {
            $(this).parent().addClass("menu-open");
            $(this).addClass("active");
        }
    });
    setInterval(function () {
        var wd = $(window).width();
        var side = $(".main-sidebar");
        if(wd < 991){
            // side.css('visibility', 'hidden');
            side.hide(200);
        } else {
            // side.css('visibility', 'visible');
            side.show(200);
        }

    }, 100);
    $('.select2bs4').select2({
      theme: 'bootstrap4'
    });
    // $(".nav-link-header").click(function () {
    //     var side = $(".main-sidebar");
    //     if (side.isVi)
    // });
});