dailychallenge
export type Book = {
  id: number;
  title: string;
  author: string;
};

type ListProps<T> = {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
};

function List<T>({ items, renderItem }: ListProps<T>) {
  return (
    <ul>
      {items.map((item, index) => (
        <li key={index}>
          {renderItem(item)}
        </li>
      ))}
    </ul>
  );
}

export default List;

import { useState } from "react";
import List from "./components/List";
import { Book } from "./types/Book";

function BookApp() {

  const [books, setBooks] = useState<Book[]>([
    {
      id: 1,
      title: "Harry Potter",
      author: "J.K. Rowling"
    },
    {
      id: 2,
      title: "The Hobbit",
      author: "J.R.R. Tolkien"
    },
    {
      id: 3,
      title: "Dune",
      author: "Frank Herbert"
    }
  ]);

  // Add new book
  const addBook = () => {

    const newBook: Book = {
      id: books.length + 1,
      title: `Book ${books.length + 1}`,
      author: `Author ${books.length + 1}`
    };

    setBooks([...books, newBook]);
  };

  return (
    <div>

      <h1>Book List</h1>

      <button onClick={addBook}>
        Add Book
      </button>

      <List
        items={books}
        renderItem={(book) => (
          <>
            <strong>{book.title}</strong>
            {" - "}
            {book.author}
          </>
        )}
      />

    </div>
  );
}

export default BookApp;

import BookApp from "./BookApp";

function App() {
  return (
    <>
      <BookApp />
    </>
  );
}

export default App;

