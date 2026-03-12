function getResponse(){

var user = document.getElementById("userInput").value.toLowerCase();

var response = "";

if(user.includes("elder")){
response = "Recommended caregiver: Elder care nurse.";
}

else if(user.includes("surgery")){
response = "Recommended caregiver: Post surgery specialist.";
}

else if(user.includes("physio")){
response = "Recommended caregiver: Physiotherapy support nurse.";
}

else{
response = "Please upload medical reports or contact support.";
}

document.getElementById("botResponse").innerHTML = response;

}


function searchCaregiver(){

var input = document.getElementById("search").value.toLowerCase();

var caregivers = document.getElementsByClassName("caregiver");

for(var i=0;i<caregivers.length;i++){

var text = caregivers[i].innerText.toLowerCase();

if(text.includes(input)){
caregivers[i].style.display="block";
}
else{
caregivers[i].style.display="none";
}

}

}