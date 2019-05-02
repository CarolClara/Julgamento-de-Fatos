function activateButton() {
    let element = document.getElementsByClassName("active");
    if (element){
        element.classList.remove("active");
    }
    this.addClass('active');
}