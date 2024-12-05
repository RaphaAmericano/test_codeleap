from rest_framework import serializers
from base.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('id', 'username', 'created_datetime')
    
    def validate(self, value):
        if 'id' in self.initial_data:
            raise serializers.ValidationError({'id':'id(primary key) cannot be edited'})
        elif 'username' in self.initial_data:
            raise serializers.ValidationError({'username':'username cannot be edited'})
        elif 'created_datetime' in self.initial_data:
            raise serializers.ValidationError({'created_datetime':'created_datetime cannot be edited'})
        
        return value