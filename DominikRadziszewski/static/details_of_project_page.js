var modal = document.getElementById("myModal");

var img = document.getElementsByClassName("myImg");
for(var i=0; i<img.length; i++) {img[i].onclick = showCaption;}
var modalImg = document.getElementById("img01");
function showCaption(){
  modal.style.display = "block";
  modalImg.src = this.src;
}

var span = document.getElementsByClassName("close")[0];

span.onclick = function() {
  modal.style.display = "none";
}
modal.onclick = function() {
  modal.style.display = "none";
}