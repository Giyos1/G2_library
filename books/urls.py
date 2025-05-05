from django.urls import path
from books import views

urlpatterns = [
    # path('', views.books, name='books'),

    # class Based View URL
    path('book/', views.BookListView.as_view(), name='book'),
    path('create/', views.BookCreateView.as_view(), name='book_create'),
    path('detail/<int:pk>/', views.BookDetailView.as_view(), name='book_detail_'),
    path('update/<int:pk>/', views.BookUpdateView.as_view(), name='book_update_'),

    path('book_list/', views.book_list, name='books_list'),
    path('book_detail/<int:id>/', views.book_detail, name='book_detail'),
    path('book_create/form/', views.book_create, name='book_create'),
    path('book_create/', views.book_create_save, name='book_create_save'),
    path('update/form/<int:id>/', views.book_update_form, name='book_update_form'),
    path('update/<int:id>/', views.book_update, name='book_update'),
    path('delete/<int:id>/', views.book_delete, name='book_delete'),
]
