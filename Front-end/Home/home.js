function terms_changed(termsCheckBox){
    const btn = document.getElementById('submit_button');
    btn.style.backgroundColor = 'lightslategray';
    btn.style.color = 'white';
    if(termsCheckBox.checked){
        document.getElementById("submit_button").disabled = false;
        btn.style.backgroundColor = '#831238';
        btn.style.color = 'white';
    } else{
        document.getElementById("submit_button").disabled = true;
    }
}