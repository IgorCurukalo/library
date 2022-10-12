from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.books.models import Author


class AuthorView(APIView):

    def post(self, request):
        data = request.data
        author = Author(**data)
        author.save()

