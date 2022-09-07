from rest_framework import serializers
from apps.books.models import PublishingHouse, Book, Author
from apps.books.signals import log_book_save, post_save

class PublishingHouseSerializers(serializers.ModelSerializer):
    class Meta:
        model = PublishingHouse
        fields = "__all__"

    def create(self, validated_data):
        return PublishingHouse.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
