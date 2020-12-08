from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'), # 127.0.0.1:8000/catalog/
    path('books/', views.BookListView.as_view(), name='books'),  # 127.0.0.1:8000/catalog/books/
]