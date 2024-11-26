from rest_framework import serializers
from .models import Author, Mesage

class AuthorSerializers(serializers.ModelSerializer):

    profile_picture = serializers.ImageField(allow_empty_file = True, required = False)

    class Meta:
        model = Author
        fields = "__all__"

class MessageSerializers(serializers.ModelSerializer):
    author = AuthorSerializers(read_only = True)
    class Meta:
        model = Mesage
        fields = "__all__"