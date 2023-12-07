// converter Farenheit

function Farenheit(celsius){
    var farenheit = (celsius * 9/5) + 32;
    return farenheit;

}

console.log(Farenheit(32));

function ConvertE(amount){
    var FinalAmount = amount * 0.95;
    return FinalAmount;

}

console.log(ConvertE(Number(prompt(" What to convert ? "))));