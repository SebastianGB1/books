import { Component, OnInit } from '@angular/core';
import { BooksService } from '../../services/books.service';
import { Book } from '../../interfaces/book';
import { ModalComponent } from "../../components/modal/modal.component";

@Component({
  selector: 'app-books',
  imports: [ModalComponent],
  templateUrl: './books.component.html',
  styleUrl: './books.component.css'
})
export class BooksComponent implements OnInit {
  books: Book[] = []
  actualBook!: Book;
  showDialog: boolean = false;
  edit: boolean = false;
  constructor(private booksService: BooksService) { }
  ngOnInit(): void {
    this.getBooks()
  }

  openNew() {
    this.actualBook = {
      id: '',
      title: '',
      author: '',
      read: false
    }
    this.showDialog = true
    this.edit = false
  }

  openEdit(book: Book) {
    this.actualBook = { ...book }
    this.showDialog = true
    this.edit = true
  }
  modalAccept(event: Book) {
    console.log(event)
    if (this.edit) {
      this.updateBook(event)
    }
    else {
      this.addBook(event)
    }
  }

  closeDialog() {
    this.showDialog = false
  }
  getBooks() {
    this.booksService.fetchBooks().subscribe({
      next: (books) => {
        this.books = books
      },
      error: (error) => {
        alert(error.error.message)
      }
    })
  }

  deleteBook(book: Book) {
    if (!confirm(`Are you sure the delete the book ${book.title}?`)) return
    this.booksService.deleteBook(book).subscribe({
      next: () => {
        this.getBooks()
      },
      error: (error) => {
        alert(error.error.message)
      }
    })
  }

  updateBook(book: Book) {
    this.booksService.updateBook(book).subscribe({
      next: () => {
        this.getBooks()
        this.closeDialog()
      },
      error: (error) => {
        alert(error.error.message)
      }
    })
  }

  addBook(book: Book) {
    this.booksService.addBook(book).subscribe({
      next: () => {
        this.getBooks()
        this.closeDialog()
      },
      error: (error) => {
        alert(error.error.message)
      }
    })
  }

}
