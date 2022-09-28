from rest_framework import serializers
from apps.books.models import Book, Author, PublishingHouse
from signals.signals import *
from apps.books.tasks import inform_new


class PublishingHouseSerializers(serializers.ModelSerializer):

    publishing_house_name = serializers.CharField(required=False)
    adress = serializers.CharField(required=False)
    contact_phone = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    website_linck = serializers.URLField(required=False)

    class Meta:
        model = PublishingHouse
        fields = "__all__"

    def create(self, validated_data):
        inform_new.delay()
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
