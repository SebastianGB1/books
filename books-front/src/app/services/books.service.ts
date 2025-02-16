import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment.development';
import { Observable } from 'rxjs';
import { Book } from '../interfaces/book';

@Injectable({
  providedIn: 'root'
})
export class BooksService {
  url = environment.API_URL + "/api/books"

  constructor(private http: HttpClient) { }

  fetchBooks():Observable<Book[]> {
    return this.http.get<Book[]>(this.url)
  }
  addBook(book: Book):Observable<Book> {
    const {id, ...newBook} = book
    return this.http.post<Book>(this.url, newBook)
  }
  deleteBook(book: Book):Observable<Book> {
    return this.http.delete<Book>(this.url + "/" + book.id)
  }
  updateBook(book: Book):Observable<Book> {
    const {id, ...newBook} = book
    return this.http.put<Book>(this.url + "/" + book.id, newBook)
  }
}
