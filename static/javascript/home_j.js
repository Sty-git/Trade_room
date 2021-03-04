function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  // Close the dropdown if the user clicks outside of it
  window.onclick = function(e) {
    if (!e.target.matches('.dropbtn')) {
    var myDropdown = document.getElementById("myDropdown");
      if (myDropdown.classList.contains('show')) {
        myDropdown.classList.remove('show');
      }
    }
  }


// function postYourAdd() {
//     var iframe = $("#forPostyouradd");
//     iframe.attr("src", iframe.data("src"));
//     document.getElementById("iframe").style.border = "2px solid black";
// }
