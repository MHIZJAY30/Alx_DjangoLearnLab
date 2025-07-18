from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]


from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]



from django.urls import path
from . import views

urlpatterns = [
    path('librarian-role/', views.librarian_view, name='librarian_view'),
]



from django.urls import path
from . import views

urlpatterns = [
    path('add_book/', views.add_book, name='add-book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit-book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete-book'),
]
