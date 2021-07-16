from django.shortcuts import render
from .forms import BookForm, AuthorForm
from .models import Book, Author
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q


class BookList(ListView):
    queryset = Book.objects.all()
    context_object_name = "books"
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super(BookList, self).get_context_data(**kwargs)
        context['authors_dropdown'] = Author.objects.raw('SELECT DISTINCT ON (name) name, id FROM main_author;')
        return context


class BookCreate(CreateView):
    form_class = BookForm
    success_url = reverse_lazy('main')
    template_name = 'main/forms/book_create.html'


class BookUpdate(UpdateView):
    model = Book
    fields = ('title', 'author', 'file', 'description')
    success_url = reverse_lazy('main')
    template_name = "main/forms/book_update.html"


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('main')
    template_name = "main/forms/book_delete.html"


class AuthorCreate(CreateView):
    form_class = AuthorForm
    success_url = reverse_lazy('book_add')
    template_name = "main/forms/author_create.html"


class AuthorUpdate(UpdateView):
    model = Author
    fields = ('name',)
    success_url = reverse_lazy('main')
    template_name = "main/forms/author_update.html"


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('main')
    template_name = "main/forms/author_delete.html"


class BookSearch(ListView):
    queryset = Book.objects.all()
    context_object_name = "books"
    template_name = "main/index.html"

    def get_queryset(self):
        query = self.request.GET.get('search')
        search = Book.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        context_object_name = search
        return context_object_name


def author_filter(request, pk):
    authors_dropdown = Author.objects.raw('SELECT DISTINCT ON (name) name, id FROM main_author;')
    author = Author.objects.filter(pk=pk)
    for a in author:
        books = Book.objects.raw(
                f"SELECT * FROM main_book \
                LEFT JOIN main_book_author ON main_book.id = main_book_author.book_id \
                LEFT JOIN main_author ON main_book_author.author_id = main_author.id \
                WHERE main_author.name = '{a}';"
        )
    return render(request, 'main/index.html', {'books': books, 'authors_dropdown': authors_dropdown})