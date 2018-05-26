
// ADD MODAL

// Get the Modal
var modal_add = document.getElementById('addModal');

// Get the button that opens the modal
var btn_add = document.getElementById("addBtn");

// Get the element that closes the modal
var close_add = document.getElementsByClassName("close-add")[0];

// When the user clicks the button, open the modal
btn_add.onclick = function() {
    modal_add.style.display = "block";
}

// When the user clicks on CLOSE, close the modal
close_add.onclick = function() {
    modal_add.style.display = "none";
}

// DELETE MODAL

// Get the Modal
var modal_delete = document.getElementById('deleteModal');

// Get the button that opens the modal
var btn_delete = document.getElementById("deleteBtn");

// Get the element that closes the modal
var close_delete = document.getElementsByClassName("close-delete")[0];

// When the user clicks the button, open the modal
btn_delete.onclick = function() {
    modal_delete.style.display = "block";
}

// When the user clicks on CLOSE, close the modal
close_delete.onclick = function() {
    modal_delete.style.display = "none";
}

// Change style of navbar on scroll
window.onscroll = function()
{myFunction()}; function myFunction() {
    var navbar = document.getElementById("myNavbar");
    if (document.body.scrollTop > 100 ||
document.documentElement.scrollTop > 100) {
        navbar.className = "w3-bar" + " w3-card" + "
w3-animate-top" + " w3-white";
    } else {
        navbar.className = navbar.className.replace(" w3-card
w3-animate-top w3-white", "");
    }
}

// Used to toggle the menu on small screens when clicking on the menu b$
toggleFunction() {
    var x = document.getElementById("navDemo");
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    } else {
        x.className = x.className.replace(" w3-show", "");
    }
}

