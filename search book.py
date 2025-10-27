#tim sach theo id
def search_book():
    while True:
        for book in books:
            search = int(input('hay nhap id sach '))
            if search == book_id:
                return(book)
            elif search != book_id:
                print('invalid id')
                
print(search_book())