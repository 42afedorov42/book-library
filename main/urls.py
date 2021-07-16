from django.urls import path
from .views import *


urlpatterns = [
	path('', BookList.as_view(), name='main'),
	path('search/', BookSearch.as_view(), name='search'),

	path('book/add/', BookCreate.as_view(), name='book_add'),
	path('book/<int:pk>/update/', BookUpdate.as_view(), name='book_update'),
	path('book/<int:pk>/delete/', BookDelete.as_view(), name='book_delete'),

	path('author/add/', AuthorCreate.as_view(), name='author_add'),
	path('author/<int:pk>/', author_filter, name='author_filter'),
	path('author/<int:pk>/update/', AuthorUpdate.as_view(), name='author_update'),
	path('author/<int:pk>/delete/', AuthorDelete.as_view(), name='author_delete'),
]