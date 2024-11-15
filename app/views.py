from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework import status

from .serializers import AuthorSerializers, MessageSerializers

from .models import Author, Mesage

# Create your views here.

@api_view(['GET'])
def getMessages(request):
    messages = Mesage.objects.all().order_by('created_at')
    serializer = MessageSerializers(messages, many = True)
    return Response(serializer.data)

@api_view(["POST"])
def createMessages(request):
    username = request.data.get("username")
    content = request.data.get("content")

    if not username or not content:
        return Response(
            {'error': 'los campos son requeridos'}, status = status.HTTP_400_BAD_REQUEST
        )
    
    author, _ = Author.objects.get_or_create(name = username)

    serializer = MessageSerializers(data = {"author": author.id, "content": content})

    if serializer.is_valid():
        serializer.save(author = author)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
