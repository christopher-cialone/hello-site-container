
from django.urls import path
from hello_app.views import HelloWorldView

urlpatterns = [
    path('', view = HelloWorldView.as_view()),
]
