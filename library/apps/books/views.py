from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.books.models import PublishingHouse, Book, Author
from apps.books.serializers import PublishingHouseSerializers, BookSerializers, AuthorSerializers

class PublishingHouseAPIView(APIView):

    def get(self, request, pk):
        qweryset = PublishingHouse.objects.filter(pk=pk)
        serializer = PublishingHouseSerializers(qweryset, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        publishing_house = PublishingHouse.objects.get(pk=pk)
        serializer = PublishingHouseSerializers(data=request.data, instance=publishing_house)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        publishing_house = PublishingHouse.objects.get(pk=pk)
        publishing_house.delete()
        return Response(status=status.HTTP_200_OK)

class PublishingHouseCreateAPIView(APIView):

    def post(self, request):
        serializer = PublishingHouseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # serializer = PublishingHouseSerializers(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response(serializer.data)


class BookAPIView(APIView):

    def get(self, request, pk):
        qweryset = Book.objects.filter(pk=pk)
        serializer = BookSerializers(qweryset, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = PublishingHouseSerializers(data=request.data, instance=book)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_200_OK)

class BookCreateAPIView(APIView):

    def post(self, request):
        serializer = BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorAPIView(APIView):

    def get(self, request, pk):
        qweryset = Author.objects.filter(pk=pk)
        serializer = AuthorSerializers(qweryset, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        author = Author.objects.get(pk=pk)
        serializer = PublishingHouseSerializers(data=request.data, instance=author)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = Author.objects.get(pk=pk)
        author.delete()
        return Response(status=status.HTTP_200_OK)

class AuthorCreateAPIView(APIView):

    def post(self, request):
        serializer = AuthorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)