#!/usr/bin/env node

class Vehicle {
    constructor(make, model){
        this.make = make;
        this.model = model;
    }

    start(){
        console.log(`The ${this.make} with the model ${this.model} have started`)
    }
}


class Car extends Vehicle{
    constructor(make, model, year){
        super(make, model)
        this.year = year;
    }
    start(){
        console.log(`This is the new vihicle I got with make of ${this.make} and model of ${this.model}`)
    }
}

const newCar =new Car("Benz", 'GLE', 2023)


newCar.start()
