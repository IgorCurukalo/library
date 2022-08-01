# from django.urls import path
# from apps.books.views import PublishingHouseAction
#     # , PublishingHouseRetrieve
#     # PublishingHouseAPIView, PublishingHouseCreateAPIView, BookAPIView, BookCreateAPIView, AuthorAPIView, AuthorCreateAPIView
#
#
# urlpatterns = [
#     path('publishing_house/', PublishingHouseAction.as_view()),
#     # path('publishing_house_/', PublishingHouseRetrieve.as_view()),
#
from apps.books.router import router as book_router

urlpatterns = book_router.urls




    # path('publishing_house/', PublishingHouseCreateAPIView.as_view()),
    # path('publishing_house/<int:pk>', PublishingHouseAPIView.as_view()),
    # path('publishing_house/', PublishingHouseCreateAPIView.as_view()),
    # path('book/<int:pk>', BookAPIView.as_view()),
    # path('book/', BookCreateAPIView.as_view()),
    # path('author/<int:pk>', AuthorAPIView.as_view()),
    # path('author/', AuthorCreateAPIView.as_view())
# ]