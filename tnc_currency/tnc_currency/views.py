from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import UserSerializer

class ListAPIEndpointsView(APIView):
    """create a new user"""
    authentication_classes = ()
    permission_classes = ()
    def get(self, request):
        return Response(
            {
                'API Documentation': 'http://127.0.0.1:8000/docs/',
                'Login': 'http://127.0.0.1:8000/users/login/',
                'Refresh JWT': 'http://127.0.0.1:8000/users/login/refresh',
                'Create User': 'http://127.0.0.1:8000/users/create/',
                'Display/Edit User': 'http://127.0.0.1:8000/users/me/',
                'Fiats': 'http://127.0.0.1:8000/currency/fiats/',
            }
        )

