var apples = 9;
var oranges = Number(prompt(" how many oranges ? "));

if(apples + oranges == 11){
    console.log("bg! ");
} else {
    console.log("Try again ");
}
 
Gender = prompt(" Your gender ?");

function greet(gender){
    if(gender == "male"){
        return "Welcome Sir! Pleasure to see you!";
    } else if(gender == "female"){
        return "Welcome Madame! Pleasure to see you!";
    } else {
        return "Welcome thing!";
    }
}

console.log(greet(Gender));


