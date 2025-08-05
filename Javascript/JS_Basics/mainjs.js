#!/usr/bin/env node

class newObject{
    constructor(value){
        this.value = value;
    }

    increament(){
        this.value = this.value + 1;
        console.log(this.value)
    }
}


testObject =  new newObject(5);


testObject.increament()
