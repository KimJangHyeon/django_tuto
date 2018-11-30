from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from django.shortcuts import render
from swapp.models import TodoList, Memo, Time
from swapp.serializers import TodoSerializer, MemoSerializer, TimeSerializer

#show all
@api_view(['GET'])
def todo_all(request, format=None):
  if request.method == 'GET':
    todos = TodoList.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def memo_all(request, format=None):
  if request.method == 'GET':
    memos = Memo.objects.all()
    serializer = MemoSerializer(memos, many=True)
    return Response(serializer.data)
#===============================================================================================================================
#create
@api_view(['POST'])
def todo_create(request, format=None):
  if request.method == 'POST':
    serializer = TodoSerializer(data=request.data)
    if not serializer.is_valid():
      return ErrorResponse.error_response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
      serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def memo_create(request, format=None):
  if request.method == 'POST':
    serializer = MemoSerializer(data=request.data)
    if not serializer.is_valid():
      return ErrorResponse.error_response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    else:
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)


#update
@api_view(['PUT'])
def todo_update(request, format=None):
  if request.method == 'PUT':
    lid = request.data.get('lid')
    todo_entry = TodoList.objects.get(lid=lid)
    todo_entry.date = request.data.get('date')
    todo_entry.title = request.data.get('title')
    todo_entry.context = request.data.get('context')
    todo_entry.save()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['PUT'])
def memo_update(request, format=None):
  if request.method == 'PUT':
    mid = request.data.get('mid')
    memo_entry = Memo.objects.get(mid=mid)
    memo_entry.context = request.data.get('context')
    memo_entry.save()
    return Response(status=status.HTTP_202_ACCEPTED)


#delete
@api_view(['DELETE'])
def todo_delete(request):
  if request.method == 'DELETE':
    todo_entry = TodoList.objects.get(lid=request.data.get('lid'))
    todo_entry.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def memo_delete(request):
  if request.method == 'DELETE':
    memo_entry = Memo.objects.get(mid=request.data.get('mid'))
    memo_entry.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
#
# @api_view(['GET'])
# def time_get(request):
#   if request.method == 'GET':
#



class ErrorResponse:
	@staticmethod
	def error_response(error_code, message):
		data = {"message": message, "ErrorCode": error_code}
		return Response(data)
