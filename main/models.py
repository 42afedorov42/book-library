from django.db import models
from django.urls import reverse


class Author(models.Model):
	name = models.CharField(max_length=150, default='', db_index=True)

	def get_absolute_url(self):
		return reverse('Author', kwargs={'pk': self.pk})

	def __str__(self):
		return self.name


class Book(models.Model):
	title = models.CharField(max_length=150, blank=True, db_index=True)
	author = models.ManyToManyField(Author, blank=True, related_name='book')
	file = models.FileField(null=False)
	description = models.CharField(max_length=1000, blank=True, db_index=True)

	def get_absolute_url(self):
		return reverse('Book', kwargs={'pk': self.pk})

	def __str__(self):
		return self.title