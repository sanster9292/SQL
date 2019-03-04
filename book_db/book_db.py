import mysql.connector
import sys


def main():

    def get_info():
        title = input('What is the title of the book? ')
        author = input('Who is the author(s) of this book? ')
        genre = input('Use 1 to 3 genres which describe this book seperated by commas: ')
        thoughts = input('In 140 characters put out your thoughts about this book: ')

        return title, author, genre, thoughts

    title, author, genre, thoughts = get_info()
    print('\n This is what you entered \n')
    print('\n')
    print(title,'|',author,'|', genre,'|', thoughts,'\n')

    confir = input('\n\n Does this information seem okay? Type in Y or N to confirm or deny: ')

    def get_confir(confir):
        if confir.lower() == 'y':
            return 1
        elif confir.lower() == 'n':
            return 0

    good_not = get_confir(confir)

    if good_not ==1:
        pass
    else:
        title, author, genre, thoughts = get_info()
        confir = input('\n\n Does this information seem okay? Type in Y or N to confirm or deny: ')
        get_confir(confir)


    book_db = mysql.connector.connect(
        host = "localhost",
        user= "root",
        passwd = "Adeline61",
        database = "books")


    cur = book_db.cursor()

    # cur.execute('DROP DATABASE IF EXISTS books')
    sql = "INSERT INTO books_read(TITLE, AUTHOR, GENRE, THOUGHTS) VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (title, author, genre, thoughts))

    book_db.commit()
    print('1 record inserted, ID: ', cur.lastrowid)


if __name__ == "__main__":
    main()
