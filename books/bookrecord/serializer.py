from rest_framework import serializers
from .models import bookrecord

class bookrecordSerializer(serializers.Serializer):
	bname=serializers.CharField(max_length=20)
	bauthor=serializers.CharField(max_length=45)
	bquantity=serializers.CharField(max_length=34)

class bookrecordModelSerializer(serializers.ModelSerializer):
	class Meta:
		model=bookrecord
		fields='__all__'


