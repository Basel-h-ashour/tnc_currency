from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from user.serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    """create a new user"""
    serializer_class = UserSerializer
    authentication_classes = ()
    permission_classes = ()

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer

    def get_object(self):
        """overrides the builtin fn to get the logged in user not url one"""
        return self.request.user
