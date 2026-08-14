const express = require('express');
let books = require("./booksdb.js");
let isValid = require("./auth_users.js").isValid;
let users = require("./auth_users.js").users;
const public_users = express.Router();
const axios = require('axios');

public_users.post("/register", (req, res) => {
    const username = req.body.username;
    const password = req.body.password;

    if (username && password) {
        if (!isValid(username)) {
            users.push({ "username": username, "password": password });
            return res.status(200).json({ message: "Customer successfully registered. Now you can login" });
        } else {
            return res.status(400).json({ message: "User already exists!" });
        }
    }
    return res.status(404).json({ message: "Unable to register user." });
});

// Task 10: Get the book list available in the shop using Promises / Async-Await
public_users.get('/', function (req, res) {
    const getBooks = new Promise((resolve, reject) => {
        resolve(books);
    });
    getBooks.then((bks) => {
        res.send(JSON.stringify(bks, null, 4));
    }).catch((err) => {
        res.status(500).json({ message: "Error fetching books" });
    });
});

// Task 11: Get book details based on ISBN using Promises / Async-Await
public_users.get('/isbn/:isbn', function (req, res) {
    const isbn = req.params.isbn;
    const getBookByISBN = new Promise((resolve, reject) => {
        if (books[isbn]) {
            resolve(books[isbn]);
        } else {
            reject("Book not found");
        }
    });
    getBookByISBN.then((book) => {
        res.send(JSON.stringify(book, null, 4));
    }).catch((err) => {
        res.status(404).json({ message: err });
    });
});

// Task 12: Get book details based on Author using Promises / Async-Await
public_users.get('/author/:author', function (req, res) {
    const author = req.params.author;
    const getBooksByAuthor = new Promise((resolve, reject) => {
        let booksByAuthor = [];
        let keys = Object.keys(books);
        keys.forEach((key) => {
            if (books[key].author.toLowerCase() === author.toLowerCase()) {
                booksByAuthor.push(books[key]);
            }
        });
        if (booksByAuthor.length > 0) {
            resolve(booksByAuthor);
        } else {
            reject("No books found by this author");
        }
    });
    getBooksByAuthor.then((result) => {
        res.send(JSON.stringify(result, null, 4));
    }).catch((err) => {
        res.status(404).json({ message: err });
    });
});

// Task 13: Get all books based on Title using Promises / Async-Await
public_users.get('/title/:title', function (req, res) {
    const title = req.params.title;
    const getBooksByTitle = new Promise((resolve, reject) => {
        let booksByTitle = [];
        let keys = Object.keys(books);
        keys.forEach((key) => {
            if (books[key].title.toLowerCase() === title.toLowerCase()) {
                booksByTitle.push(books[key]);
            }
        });
        if (booksByTitle.length > 0) {
            resolve(booksByTitle);
        } else {
            reject("No books found with this title");
        }
    });
    getBooksByTitle.then((result) => {
        res.send(JSON.stringify(result, null, 4));
    }).catch((err) => {
        res.status(404).json({ message: err });
    });
});

// Get book review based on ISBN
public_users.get('/review/:isbn', function (req, res) {
    const isbn = req.params.isbn;
    if (books[isbn]) {
        res.send(JSON.stringify(books[isbn].reviews, null, 4));
    } else {
        res.status(404).json({ message: `Book with ISBN ${isbn} not found` });
    }
});

module.exports.general = public_users;
