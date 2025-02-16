import { Component, OnInit } from '@angular/core';
import { BooksService } from '../../services/books.service';
import { Book } from '../../interfaces/book';

@Component({
  selector: 'app-books',
  imports: [],
  templateUrl: './books.component.html',
  styleUrl: './books.component.css'
})
export class BooksComponent implements OnInit {
  books: Book[] = []
  constructor(private booksService: BooksService) { }
  ngOnInit(): void {
    this.getBooks()
  }

  getBooks() {
    this.booksService.fetchBooks().subscribe({
      next: (books) => {
        this.books = books
      },
      error: (error) => {
        alert(error.message)
      }
    })
  }

  deleteBook(book: Book){
    if(!confirm(`Are you sure the delete the book ${book.title}?`)) return
    this.booksService.deleteBook(book).subscribe({
      next: () => {
        this.getBooks()
      },
      error: (error) => {
        alert(error.error.message)
      }
    })
  
  }
}
