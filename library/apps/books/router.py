from rest_framework.routers import SimpleRouter
from apps.books.views import PublishingHouseAction

router = SimpleRouter()

router.register(r'publishing_house', PublishingHouseAction, basename='PublishingHouse')






