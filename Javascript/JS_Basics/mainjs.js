#!/usr/bin/env node

function firstNumbers(a){
    return function(b){
        return (b + a);
    };
}

const newFive = firstNumbers(5)

const newSix = secondNumber(newFive)

return newSix;




