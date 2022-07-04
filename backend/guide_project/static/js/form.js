function myFunction() {
    let text;
    let person = prompt("Please enter CONFIRM to proceed:", "CONFIRM");
    if (person == null || person == "") 
    {
      text = "User cancelled the prompt.";
    } 
    else 
    {
      text =window.alert("You have submitted the form successfully");
    }
}  


function preventBack() { window.history.forward(); }  
            setTimeout("preventBack()", 0);  
            window.onunload = function () { null }; 
