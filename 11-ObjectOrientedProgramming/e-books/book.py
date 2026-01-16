class Book():
    def __init__(self, author, title, num_pg, curr_pg_num):
        self.author = author
        self.title = title
        self.num_pg = num_pg
        self.curr_num_pg = curr_pg_num
        self.open = False
    
    def open_book(self):
        self.open = True
        print("Opening book")
    
    def close_book(self):
        self.open = False
        print("Closing book")
    
    def display_status(self):
        if self.open == True:
            print(f"""Book status: \n Author: {self.author}\n Title: {self.title}
 Number of pages: {self.num_pg} \n Current page: {self.curr_num_pg}
    """)
        else:
            print("Book is closed")
    
    def read_pages(self, read_pg_num):
        self.read_pg_num = read_pg_num
        if self.open == True and self.curr_num_pg + self.read_pg_num < self.num_pg:
            self.curr_num_pg += self.read_pg_num
            print(f"{self.read_pg_num} pages readed")
        elif self.open == True and self.curr_num_pg + self.read_pg_num > self.num_pg:
            print(f"""You can't read that much. There are only 
                {self.num_pg - self.curr_num_pg} left
            

            """)
        elif self.open == False:
            print("Book is closed, you can't read for now")

    def go_back(self, go_back):
        self.go_back_num = go_back
        if self.open == True and self.curr_num_pg - self.go_back_num > 0:
            self.curr_num_pg -= self.go_back_num
            print(f"{self.go_back_num} pages returned")
        elif self.open == True and self.curr_num_pg - self.go_back_num < 0:
            print(f"""You can't go back that much. There are only 
                {self.curr_num_pg} left to g back
            

            """)
        elif self.open == False:
            print("Book is closed, you can't go back for now")
