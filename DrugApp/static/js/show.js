$(document).ready(function () {
    $(".p-menu").click(function () {
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
    $(".btn-tool").click(function (){
        var celement = $(this).children("i");
        var pelement = $(this).parent().parent().siblings(".card-body");
        if(celement.hasClass("fa-minus")) {
            pelement.slideUp(300);
            celement.removeClass("fa-minus");
            celement.addClass("fa-plus");
        } else {
            pelement.slideDown(300);
            celement.removeClass("fa-plus");
            celement.addClass("fa-minus");
        }

    })

    // $(".nav-link-header").click(function () {
    //     var side = $(".main-sidebar");
    //     if (side.isVi)
    // });
});