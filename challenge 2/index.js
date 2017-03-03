var x = ""
window.onload = function() {
    paragraphs = document.getElementById("gi").getElementsByClassName("selectionShareable");
    Array.prototype.forEach.call(paragraphs, function(paragraph){
        x += paragraph.textContent + "\n\n";
    });
    console.log(x);
}