#!/usr/bin/env node

class Person {
    name;

    constructor(name){
        this.name = name;

    }

    introduceSelf() {
        console.log(`Hi I am ${this.name} and welcome to my world`);
    }
}

class Professor extends Person{
    constructor(name, course){
        super(name);
        this.course = course;
    }

    introduceSelf(){
        console.log(
            `My name is ${this.name}, and I will be your ${this.course} professor.`
        )
    }
}


const firstPerson = new Person('John');
const firstProf = new Professor('John', 'Physics');

firstPerson.introduceSelf()
firstProf.introduceSelf()


