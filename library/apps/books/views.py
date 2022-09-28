from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.books.models import Author
from apps.books.tasks import inform_new


class AuthorView(APIView):

    def post(self, request):
        data = request.data
        author = Author(**data)
        author.save()
        # inform_new.delay(4, 4)
        # return Response(status=status.HTTP_202_ACCEPTED)
