document.getElementById("guide-button").addEventListener("click", function () {

  if (document.getElementById("guide-content").classList.length == 2) {
    document.getElementById("guide-content").classList.toggle("hide-guide");
  }
  document.getElementById("guide-content").classList.toggle("show-guide");
})