#!/usr/bin/env node

class Book {
    constructor(title, author, year){
        this.title = title;
        this.author = author;
        this.year = year;
    }

    getDetails(){
        console.log(`${this.title} ${this.author} ${this.year}`)
    }
}

const newBook = new Book('A new earth', 'Ekhart Tolle', 1990)


newBook.getDetails()

