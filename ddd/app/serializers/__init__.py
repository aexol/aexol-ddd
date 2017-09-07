from ..models import *
from rest_framework import serializers
#Put all models you want to create default serializers from
uniClasses = []
for c in uniClasses:
    cName = c.__name__+"Serializer"
    globals()[cName] = type(cName,(serializers.ModelSerializer,),{
        "Meta":type("Meta",(),{
            "model":c,
            "fields":"__all__"
        })
    })

#Example of user owned objects default serializers - put them in userOwnedClasses
userOwnedClasses = []

def _user(cls,obj):
    request = cls.context.get("request")
    profile = User.objects.get(user=request.user)
    return profile.id

for c in userOwnedClasses:
    cName = c.__name__+"Serializer"
    globals()[cName] = type(cName,(serializers.ModelSerializer,),{
        "Meta":type("Meta",(),{
            "model":c,
            "fields":"__all__"
        }),
        "user":serializers.SerializerMethodField('_user'),
    })
    def create(cls, validated_data):
        validated_data.update({
            "user":cls.context['request'].user
        })
        r = super(globals()[cName],cls).create(validated_data)
        return r
    setattr(globals()[cName], '_user', _user)
    setattr(globals()[cName], 'create', create)
