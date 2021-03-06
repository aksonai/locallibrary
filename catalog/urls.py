from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'), # 127.0.0.1:8000/catalog/
    path('books/', views.BookListView.as_view(), name='books'),  # 127.0.0.1:8000/catalog/books/
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'), # 127.0.0.1:8000/catalog/books/1
    path('authors/', views.AuthorListView.as_view(), name='authors'),
]