from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from json import loads


@api_view(['POST'])
def login_view(request):
    data = loads(request.body)
    user = authenticate(request._request, email=data['email'], password=data['password'])

    if user is not None:
        if user.is_active:
            login(request._request,user)

        return Response({
            "success": True,
            "user": user
        })

    return Response({
        "success": False,
        "message": "Incorrect credentials"
    })