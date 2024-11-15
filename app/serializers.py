from rest_framework import serializers
from .models import Author, Mesage

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class MessageSerializers(serializers.ModelSerializer):
    author = AuthorSerializers(read_only = True)
    class Meta:
        model = Mesage
        fields = "__all__"