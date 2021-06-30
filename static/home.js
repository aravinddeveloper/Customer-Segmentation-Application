//alert('Hi');

var txtfields = [
    'age',
    'Experience',
    'familysize',   
];

var cbfields = [
    'gender',
    'married',
    'graduated',
    'profession',
    'spendingscore',
    'category'
];



function validate_forms(){
    lst=[];
    for(var i=0; i <txtfields.length; i++) 
    {
        if (document.getElementById(txtfields[i]).value===""){
            console.log(document.getElementById(txtfields[i]).value);
            document.getElementById(txtfields[i]+'Val').style.visibility = "visible";
            lst.push(false);
        }
        else{
            console.log(document.getElementById(txtfields[i]).value); 
            document.getElementById(txtfields[i]+'Val').style.visibility = "hidden";
            lst.push(true);
        }
    }
    for(var i=0; i <cbfields.length; i++) 
    {
        if (document.getElementById(cbfields[i]).value===""){
            document.getElementById(cbfields[i]+'Val').style.visibility = "visible";
            lst.push(false);
        }
        else{
            console.log(document.getElementById(cbfields[i]).value); 
            document.getElementById(cbfields[i]+'Val').style.visibility = "hidden";
            lst.push(true);
        }
    } 
    if (lst.includes(false)){
        console.log(lst);
        return false;
    }    
    else{
        console.log(lst);
        return true;
    }    
}
