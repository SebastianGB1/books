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
}
