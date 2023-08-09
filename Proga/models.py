from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    
    def __str__(self):
        return self.title


# SupUs = admin
# pas = 1

# Получение всех объектов модели.
# >>> authors = Author.objects.all()
# >>> books = Book.objects.all()
# >>> print(authors, books)
# <QuerySet []> <QuerySet []>

# Фильтрация объектов по определенным условиям.
# >>> filtered_books = Book.objects.filter(title__startswith='The')
# >>> johns = Author.objects.filter(name='John')

# Использование связанных моделей с помощью related_name и related_query_name.
# >>> johns_books = Book.objects.filter(authors__name='John')
# >>> gatsby_authors = Author.objects.filter(book__title='The Great Gatsby')

# Создание новых объектов модели.
# >>> new_author = Author.objects.create(name='Jane')
# >>> new_book = Book.objects.create(title='New Book')
# >>> new_book.authors.add(new_author) - связваем книгу с автором

# Обновление существующих объектов.
# >>> author_to_update = Author.objects.get(name='Jane')
# >>> author_to_update.name = 'Jane Smith'
# >>> author_to_update.save()

# Удаление объектов.
# >>> book_to_delete = Book.objects.get(title='New Book')
# >>> book_to_delete.delete()
# (2, {'Proga.Book_authors': 1, 'Proga.Book': 1})

# Использование агрегирующих функций (например, count, sum, avg) для получения статистики данных.
# >>> from django.db.models import Count, Sum, Avg
# >>> author_count = Author.objects.count()
# >>> average_books_per_author = Author.objects.annotate(book_count=Count('book')).aggregate(Avg('book_count'))
# >>> authors_with_many_books = Author.objects.annotate(book_count=Count('book')).filter(book_count__gt=2)

# Использование операторов сравнения (например, __gt, __lt, __contains) для фильтрации данных.
# >>> from django.db.models import F
# >>> books_with_many_authors = Book.objects.filter(authors__gt=2)
# >>> authors_with_few_books = Author.objects.annotate(book_count=Count('book')).filter(book_count__lt=3)
# >>> books_with_great_in_title = Book.objects.filter(title__contains='Great')

# Работа с ManyToManyField и OneToOneField.
# Создание автора и связанных с ним книг с помощью ManyToManyField
# >>> new_author = Author.objects.create(name='William')
# >>> new_book1 = Book.objects.create(title='Book 1')
# >>> new_book2 = Book.objects.create(title='Book 2')
# >>> new_author.books.add(new_book1, new_book2)

# Создание OneToOne связи между автором и книгой
# >>> new_author = Author.objects.create(name='Emily')
# >>> new_book = Book.objects.create(title='Poems')
# >>> new_author_book = new_author.book_set.create(title='Poems', authors=new_author)
