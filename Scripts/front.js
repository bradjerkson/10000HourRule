function generateText(textname){
  document.getElementById('inputfile')
    .addEventListener('change', function() {

    var fr=new FileReader();
    fr.onload=function(){
        document.getElementById('results-div')
                .textContent=fr.result;
    }

    fr.readAsText(this.files[0]);
});
}

$(document).ready(function(){
  generateText("history.txt")


});
