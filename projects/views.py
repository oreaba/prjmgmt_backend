from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from utils.query import Query
from utils.query_executor import QueryExecutor

from .models import Project
from .serializers import ProjectSerializer
from rest_framework.generics import ListAPIView


def home(request):
    return JsonResponse({"app":'projects'})

def build(request):
    # qe = QueryExecutor()
    results = {}
    for query in Query:
        qe = QueryExecutor(query=query)
        result = qe.execute_query()
        results[query.name] = result
        # print(f"Creating DB Function with id = '{query.name}' ...", end=' ')
        # qe.execute_statement()
        # print('Done.')
        # print(f"*Testing DB Function with id = '{query.name}' ...", end=' ')
        # qe.execute_function()
        # results[query.name] = qe.to_decimal()
        # print(results[query.name])
    return JsonResponse(results)



class ProjectListAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
