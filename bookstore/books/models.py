from django.db import models


class Book(models.Model):
    GENRES = [
        ('Action', 'Action and Adventute'),
        ('Children\'s', 'Children\'s'),
        ('Crime', 'Crime'),
        ('Drama', 'Drama'),
        ('Fairytale', 'Fairytale'),
        ('Horror', 'Horror'),
        ('Fantasy', 'Fantasy'),
        ('Poetry', 'Poetry'),
        ('Novel', 'Novel'),
        ('Self Help', 'Self Help'),
        ('Business', 'Business'),
    ]

    title = models.CharField(max_length=150)
    description = models.TextField()
    availability = models.BooleanField()
    price = models.IntegerField()
    publication_date = models.DateField(auto_now=False)
    genre = models.CharField(max_length=100, choices=GENRES)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, default='author')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


    def __str__(self):
        return self.first_name + ' ' + self.last_name

