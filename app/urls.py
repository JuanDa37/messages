from django.urls import path
from . import views

urlpatterns = [
    path("messages/", view = views.getMessages, name = "get-messages"),
    path("messages/created/", view = views.createMessages, name = "create-messages"),
]