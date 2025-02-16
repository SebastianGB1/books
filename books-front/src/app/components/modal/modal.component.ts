import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Book } from '../../interfaces/book';
import { FormsModule } from '@angular/forms';
import { BooksService } from '../../services/books.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-modal',
  imports: [FormsModule, CommonModule],
  templateUrl: './modal.component.html',
  styleUrl: './modal.component.css'
})
export class ModalComponent {
  @Input() isOpen: boolean = false;
  @Input() title: string = '';
  @Input() book: Book = {
    id: '',
    title: '',
    author: '',
    read: false
  };
  @Output() close = new EventEmitter<void>();
  @Output() onAccept = new EventEmitter<Book>();
  submitted: boolean = false;

  closeModal() {
    this.submitted = false
    this.isOpen = false;
    this.close.emit();
  }

  accept() {
    this.submitted = true
    if (!this.book.title || !this.book.author) return
    this.onAccept.emit(this.book)
  }

}
