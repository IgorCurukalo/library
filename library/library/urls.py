from django.contrib import admin
from django.urls import path, include
from library.yasg import urlpatterns as doc_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('apps.books.urls')),
    path('acount/', include('apps.acount.urls')),
]

urlpatterns += doc_urls
