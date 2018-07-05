from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User 

from .serializers import UserSerializer

# Create your views here.
class UserDetail(APIView):
	def get(self, request):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)
