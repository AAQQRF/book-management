

#add sinh vien
#nhap du lieu sinh vien
students = []
while True:
    n = input('So luong sinh vien can nhap: ')
    if not n.isdigit():
        print('vui long nhap con so')
    else:
        break
    
n =int(n)

for i in range (1, n+1):
    print('Sinh vien thu ', i)
    staff_id = input ('enter id ')
    fullname =input('enter name ')
     
    
    student ={
        'id': staff_id,
        'fullname': fullname
    }

    students.append(student)
    
#tao ra id ngau nhien
import random

def generate_id():
    return random.randint(1, 9999)

#nhap du lieu sach

books =[]

while True:
    y = input('So luong sach can nhap: ')
    if not y.isdigit():
        print('vui long nhap con so')
    else:
        break
y =int(y) 
for i in range (1, y+1):
    print('sach thu ', i)
    book_id = generate_id()
    fullname =input('enter ten sach ')
    type = input('enter type ')

    book = {
        'book_id': book_id,
        'fullname': fullname,
        'the_loai': type,
    }
    
    books.append(book)
    
print(students)
print(books)



    

