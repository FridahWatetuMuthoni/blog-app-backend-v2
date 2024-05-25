from rest_framework import serializers
from blog.models import Post, Categories

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    category = serializers.CharField()

    class Meta:
        model = Post
        fields = ['id','title','author', 'excerpt','published','content','status','category', 'image']
        read_only_fields = ['author', 'published', 'status']
        depth = 1


    def create(self, validated_data):
        new_category = validated_data.pop('category')
        category_instance, created = Categories.objects.get_or_create(name=new_category)
        post_instance = Post.objects.create(**validated_data, category = category_instance)
        return post_instance

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.excerpt = validated_data.get('excerpt', instance.excerpt)
        instance.content = validated_data.get('content', instance.content)
        instance.status = validated_data.get('status', instance.status)
        instance.image = validated_data.get('image', instance.image)
        new_category = validated_data.pop('category')
        if new_category:
            category_instance, created = Categories.objects.get_or_create(name=new_category)
            instance.category = category_instance
        elif new_category is None:
            instance.category = instance.category
        instance.save()
        return instance
