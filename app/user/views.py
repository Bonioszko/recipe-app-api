"""Views for the usser api"""

from rest_framework import generics

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):

    """Creeate a aneqw user in the systenm"""

    serializer_class = UserSerializer
