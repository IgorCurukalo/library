from django.contrib import admin
from django.urls import path, include
from library.yasg import urlpatterns as doc_urls
from apps.books.views import AuthorView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('apps.books.urls')),
    path('acount/', include('apps.acount.urls')),
    path('books/author/', AuthorView.as_view()),
]

urlpatterns += doc_urls
