document.addEventListener("DOMContentLoaded", function () {
  var dropdownButtons = document.querySelectorAll(".dropdown-btn");

  dropdownButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      var dropdownContent = this.nextElementSibling;

      // Toggle the display of the dropdown content
      if (dropdownContent.style.display === "block") {
        dropdownContent.style.display = "none";
      } else {
        dropdownContent.style.display = "block";
      }
    });
  });
});
