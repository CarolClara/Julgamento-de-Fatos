function activateButtonLink() {
    let element = document.getElementsByClassName("a-active");
    if (element.length > 0){
        jQuery(element).removeClass("a-active");
    }
    jQuery(this).addClass('a-active');
}

function activateButtonListItem() {
    let element = document.getElementsByClassName("li-active");
    if (element.length > 0){
        jQuery(element).removeClass("li-active");
    }
    jQuery(this).addClass('li-active');
}