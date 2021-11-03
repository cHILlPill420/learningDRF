from re import A
from django.db.models import fields
from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.ModelSerializer):
    #Validators highest priority
    def starts_with_a(value):
        if value[0].lower() != 'a':
            raise serializers.ValidationError('start with A pls')
            
    city = serializers.CharField(max_length=100, validators = [starts_with_a])
    #roll = serializers.IntegerField(read_only = True) #doesn't let update roll
    class Meta:
        model = Student
        fields = ['roll', 'city', 'name'] 
        #read_only_fileds = ['roll', 'name'] #making multiple fields read only
        #extra_kwargs = {'name':{'read_only':True}}#can use any kinds of core arguements
    
    # Field level Validators .is_valid() invokes this kind of validators -2nd highest priority
    def validate_roll(self, value):
        if value>=1000:
            raise serializers.ValidationError('Seat Full')
        return value
    
    #object level validators ie multiple field validators- lowest priority
    def validate(self, attrs): #here attrs is a python dictionary of fields values
        nm = attrs.get('name')
        rl = attrs.get('roll')
        ct = attrs.get('city')
        if rl>=1000:
            raise serializers.ValidationError('No such rolls')
        if nm[0] != 'A' and ct[0] != 'A':
            raise serializers.ValidationError('A chaiyeko thyo regex feri herna parne vayo')
        return attrs
         
# class StudentSerializers(serializers.Serializer):
#     id = serializers.IntegerField()
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100, validators = [starts_with_a])
#     name = serializers.CharField(max_length=100)

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance
    
    # Field level Validators .is_valid() invokes this kind of validators -2nd highest priority
    # def validate_roll(self, value):
    #     if value>=1000:
    #         raise serializers.ValidationError('Seat Full')
    #     return value
    
    #object level validators ie multiple field validators- lowest priority
    # def validate(self, attrs): #here attrs is a python dictionary of fields values
    #     nm = attrs.get('name')
    #     rl = attrs.get('roll')
    #     ct = attrs.get('city')
    #     if rl>=1000:
    #         raise serializers.ValidationError('No such rolls')
    #     if nm[0] != 'A' and ct[0] != 'A':
    #         raise serializers.ValidationError('A chaiyeko thyo regex feri herna parne vayo')
    #     return attrs
        