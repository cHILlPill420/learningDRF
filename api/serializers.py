from rest_framework import serializers

class StudentSerializers(serializers.Serializer):
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
