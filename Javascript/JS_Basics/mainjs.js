#!/usr/bin/env node

class Animal{
    constructor(name){
        this.name = name;
    }

    speak(){
        console.log('I am an animal and I speak some language like JS, Python')
    }
}


class Dog extends Animal{
    constructor(name){
        super(name)
    }

    speak(){
        super.speak();
        console.log(`Hello my name is ${this.name}`)
    }
}


const specie = new Dog('Jimmy');

specie.speak()
