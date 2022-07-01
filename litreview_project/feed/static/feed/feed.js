    var fixed = false;

window.addEventListener('scroll', function (e) {
    topActionsSection = document.getElementById('top-actions-section');
    whiteSpace = document.createElement("div");
    whiteSpace.style = "width:100%;height:59.25px;margin:0;";
    whiteSpace.id = "topActionWhiteSpace"
    topActionPreviousSection = topActionsSection.previousElementSibling;
    if (window.scrollY >= 71) {
        topActionsSection.classList.add("buttons__fixed");
        if (!fixed) {
            topActionPreviousSection.appendChild(whiteSpace);
            fixed = true;
        }
    } else {
        topActionsSection.classList.remove("buttons__fixed");
        domWhiteSpace = document.getElementById('topActionWhiteSpace');
        domWhiteSpace.remove()
        fixed = false
    }
});