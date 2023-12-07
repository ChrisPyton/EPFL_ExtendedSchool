var secret_color = "blue";
var secret_number = 20;

function guess_secrets(color, number){
    color = prompt("Color ? ");
    number = prompt("Number ?");

    if(color == secret_color && number == secret_number){
        console.log("You are awesome! ");

    } else {
        console.log("Try again");
    }
}

guess_secrets();

