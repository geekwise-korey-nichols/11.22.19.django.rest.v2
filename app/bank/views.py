from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from bank.models import Branch
from bank.serializers import Branch_Serializer

@csrf_exempt
def branch_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        branches = Branch.objects.all()
        serializer = Branch_Serializer(branches, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Branch_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def branch_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        branch = Branch.objects.get(pk=pk)
    except Branch.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Branch_Serializer(branch)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Branch_Serializer(branch, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        branch.delete()
        return HttpResponse(status=204)