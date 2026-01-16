import book

def main():
    book1 = book.Book("Adam Mickiewicz", "Pan Tadeusz", 400, 100)
    
    book1.open_book()
    book1.display_status()
    book1.read_pages(10)
    book1.display_status()
    book1.go_back(30)
    book1.display_status()
    book1.close_book()
    book1.read_pages(10)

if __name__ == "__main__":
   main() 
