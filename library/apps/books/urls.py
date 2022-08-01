from django.urls import path
from apps.books.views import PublishingHouseAPIView, PublishingHouseCreateAPIView, BookAPIView, BookCreateAPIView, AuthorAPIView, AuthorCreateAPIView


urlpatterns = [
    path('publishing_house/<int:pk>', PublishingHouseAPIView.as_view()),
    path('publishing_house/', PublishingHouseCreateAPIView.as_view()),
    path('book/<int:pk>', BookAPIView.as_view()),
    path('book/', BookCreateAPIView.as_view()),
    path('author/<int:pk>', AuthorAPIView.as_view()),
    path('author/', AuthorCreateAPIView.as_view())
]