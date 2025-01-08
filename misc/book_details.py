import copy

books = []

current_book = {'Title': '',
                'Author': '',
                'Year': '',
                'Notes': '',
                'ISBN 10': 0}

# Title
while True:
    title = input('Enter the title of the book: ')
    if 0 < len(title) <= 255:
        current_book['Title'] = title
        break

# Author
while True:
    author = input('Enter the author of the book: ')
    if 0 < len(author) <= 255:
        current_book['Author'] = author
        break

# Year
while True:
    try:
        year = int(input('Enter the year the book was written: '))
        if year <= 2025:
            current_book['Year'] = year
            break
        else:
            print('Invalid year')
    except ValueError:
        print('Enter a number')

# Notes
notes = input('Add any notes here: ')
current_book['Notes'] = notes

# ISBN
while True:
    isbn_c = input('Enter the ISBN (11 characters): ')
    if len(isbn_c) == 11 and isbn_c[9] == '-':
        isbn = list(isbn_c)
        # print(isbn)
        checksum = 0
        pos = 0
        for i in range(len(isbn) -2, 0, -1):
            # print(i)
            checksum += int(isbn[pos]) * (i+1)
            # print(f'{int(isbn[pos])} * {i+1} = {int(isbn[pos]) * (i+1)}')
            pos += 1
        # print(f'total {checksum}')
        _checksum = copy.copy(checksum)
        for i in range(10):
            if checksum % 11 == 0:
                if checksum - _checksum != 10:
                    if checksum - _checksum == int(isbn[10]):
                        print('correct isbn')
                        current_book['ISBN 10'] = isbn_c
                        break
                    else:
                        print('incorrect isbn')
                        break
                elif checksum - _checksum == 10:
                    if isbn[10] == 'x':
                        print('correct isbn')
                        current_book['ISBN 10'] = isbn_c
                        break
                    else:
                        print('incorrect isbn')
                        break
            else:
                checksum += 1
        if current_book['ISBN 10']:
            break

print(current_book)