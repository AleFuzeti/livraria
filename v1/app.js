import { BookCatalogClient } from './generated/book_catalog_pb_service.js';
import { Empty } from './generated/book_catalog_pb.js';

function listBooks() {
    const client = new BookCatalogClient('http://localhost:8080'); // URL do proxy Envoy

    const request = new Empty();
    client.listBooks(request, {}, (err, response) => {
        if (err) {
            console.error('Erro ao listar livros:', err.message);
            return;
        }
        console.log('Livros disponíveis:');
        const bookListDiv = document.getElementById('book-list');
        bookListDiv.innerHTML = ''; // Limpa a lista de livros
        response.getBooksList().forEach(book => {
            const bookItem = document.createElement('div');
            bookItem.textContent = `${book.getTitle()} by ${book.getAuthor()}, Price: $${book.getPrice()}`;
            bookListDiv.appendChild(bookItem);
        });
    });
}

// Chamada da função para listar livros ao carregar a página
window.onload = listBooks;
