#!/usr/bin/env node

// your code goes here
class Person {
    constructor(firstName, lastName, age, hobbie){
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        this.hobbie = hobbie;
    }
    
    greet(){
        console.log(`Hello ${firstName} ${lastName} I am glad to meet you here today for you are a good guy`)
    }
}

const student = new Person('John', 'Ezekiel', 23, 'coding')

student.greet()




