from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_root(request):
    return Response({"message": "Welcome to Octofit Tracker API"})
