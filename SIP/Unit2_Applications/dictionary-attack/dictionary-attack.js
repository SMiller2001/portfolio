var wordsList = [];

function init() {
  // Load the words from the dictionary text file to wordsList
  var wordsFile = "https://raw.githubusercontent.com/GirlsFirst/SIP-2017/master/Unit2_Applications/dictionary-attack/dictionary.txt?token=ADcVhZjRMd86ZdhPE2jVvIaJdQdzLA6Yks5YvvVSwA%3D%3D";
  $.get(wordsFile, function(data) {
    document.getElementById("btnSubmit").disabled = true;
    wordsList = data.split('\n');
    document.getElementById("btnSubmit").disabled = false;
  });
}

window.onload = init;

/* ADD YOUR CODE BELOW */

function checkPassword() {
  var pw = document.getElementById("pw").value;
  var length = wordsList.length;
  for ( var i = 0; i < length; i++) {
// see if the password entered matches any words in wordsFile
    if (wordsList[i]==pw){
      document.getElementById("results").innerHTML="This password is susceptible to an attack. Please consider changing it."
      break;
    }
    else{
      document.getElementById("results").innerHTML="This password is not susceptible to an attack. Good choice!"
    }
  }
function checksymbol(pw){
  pw = pw.replace(/[1!]/g, "i");
  pw = pw.replace(/2/g,"z");
  pw = pw.replace(/3/g, "e");
  pw = pw.replace(/[@4]/g, "a");
  pw = pw.replace(/[$5]/g, "s");
  pw = pw.replace(/[69]/g, "g");
  pw = pw.replace(/7/g, "t");
  pw = pw.replace(/8/g, "b");
  pw = pw.replace(/0/g, "o");
  return pw;
}
}
