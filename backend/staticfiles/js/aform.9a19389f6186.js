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
    /*window.location.href="C:\Users\LENOVO\Desktop\guide website\GUIDE-SELECTION-PROJECT\Front-end\admin register\submitted.html";*/
}    