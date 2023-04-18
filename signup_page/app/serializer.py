from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    class Meta:
      model = User
      fields = ('first_name','last_name','email', 'password','password1','username')

    def validate(self, attr):
       validate_password(attr['password'])
       return attr

    def create(self, validated_data):
        password = validated_data['password']
        password1 = validated_data.pop('password1', None)

        if password != password1:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})

        user = User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                

                )
        user.set_password(validated_data['password'])
        user.save()
        return user





# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =User
#         fields =['username','password','first_name','last_name']

        # extra_kwargs = {
        #     'password':{'write_only': True},
        # }


        # def create(self, validated_data):
        #     return User.objects.create_user(**validated_data)
        

# class LoginSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model= User
#         fields =['username','password']      