from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import bookrecord as bookrecord
from .serializer import bookrecordSerializer,bookrecordModelSerializer



class bookmain(APIView):





	def get(self,request):
		if 'id' in request.GET:

			data=bookrecord.objects.filter(id=request.GET['id']).values('bname','bauthor','bquantity')

		elif 'bname' in request.GET:
			data=bookrecord.objects.filter(bname__icontains=request.GET['bname'])


		else:
			data=bookrecord.objects.all()
		obj=bookrecordSerializer(data,many=True)
		return Response({"data":obj.data})


	def post(self,request):
		obj=bookrecordModelSerializer(data=request.data)
		if obj.is_valid():

			obj.save()
			return Response({"message":"record added"})
		else:
			return Response({"message":obj.errors})

		
		

	def put(self,request,album_id):
		#id=request.data['id']
		data=request.data
		#data.pop('id')
		bookrecord.objects.filter(id=album_id).update(**data)
		return Response({"message":"hello test"})


	#def delete(self,request,pk):
		#data=bookrecord.objects.filter(bname__contain=request.GET['bname']).values('bname','bauthor','bquantity')
		


	



		
		












