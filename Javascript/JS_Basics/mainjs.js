#!/usr/bin/env node

function outerFunction(){
    let counter = 0
    return function(){
      counter += 1;
      return counter;
    }
}


const testFunction = outerFunction();
testFunction();
testFunction();
testFunction();
testFunction();
testFunction();
testFunction();

console.log(testFunction())
