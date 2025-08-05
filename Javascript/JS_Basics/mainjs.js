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
        console.log("I am a human but they want me to say that I am a Dog however that is how they always relate to themselves")
    }
}


const specie = new Dog('Jimmy');

specie.speak()
