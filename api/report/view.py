from api.report.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(http_method_names=["GET"])
def get_cases(request):
    queryset = Case.objects.all()
    return Response({"cases" : list(queryset.values())}, status=200)
