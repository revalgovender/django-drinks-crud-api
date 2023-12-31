from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Drink
from .serializers import DrinkSerializer


@api_view(["GET", "POST"])
def drink_list(request):
    if request.method == "GET":
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response({"drinks": serializer.data})

    if request.method == "POST":
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"drink": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def drink_detail(request, id):
    try:
        drink = Drink.objects.get(id=id)
    except Drink.DoesNotExist:
        return Response({"error": "Drink not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = DrinkSerializer(drink)
        return Response({"drink": serializer.data})

    elif request.method == "PUT":
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"drink": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        drink.delete()
        return Response({"message": "Drink was deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
