function initCardCollapsible() {
    $(".caret").on("click", function(i) {
        $(this).toggleClass("active");
        var l = $(this).parent(),
            n = $(l).next();
        $(n[0]).slideToggle()
    })
}

function initMenuCollapsible() {
    $(".nav-item.has-child").on("click", function(i) {
        var l = $(this);
        if (l.hasClass("nav-item") && (l.children("a.nav-link").toggleClass("active"), l.hasClass("has-child"))) {
            var n = l.find(".is-child");
            $(n).slideToggle()
        }
    })
}
$(document).ready(function() {
    initMenuCollapsible(), initCardCollapsible()
});