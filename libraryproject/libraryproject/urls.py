from django.contrib import admin
from django.urls import include, path
from apps.bookmodule import views

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', views.index, name='bookmodule.index'),  
    path('list_books/', views.list_books, name='bookmodule.list_books'),
    path('aboutus/', views.aboutus, name='bookmodule.aboutus'),
    path('<int:bookId>/', views.viewbook, name='bookmodule.view_one_book'),
    path('books/', include('apps.bookmodule.urls')),  
]
