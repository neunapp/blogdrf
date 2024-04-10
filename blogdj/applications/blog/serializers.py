from rest_framework import serializers
#
from .models import Suscriptions, Blog, Author, Kword, Category


class SuscriberModelSerializer(serializers.ModelSerializer):
  
  class Meta:
      model = Suscriptions
      fields = ('__all__')



class SuscriberSerializer(serializers.Serializer):
    blog = serializers.CharField()
    email= serializers.EmailField()
    
    def create(self, validated_data):
      #
      blog = Blog.objects.get(id=validated_data['blog'])
      email = validated_data['email']
      
      return Suscriptions.objects.create(blog=blog, email=email)
    
    def update(self, instance, validated_data):
      instance.email = validated_data.get('email', instance.email)
      instance.save()
      return instance
  

def validar_blog(value):
    if not (Blog.objects.filter(id=value).exists()):
      raise serializers.ValidationError('error en id blog')
    return value
    

class SuscriptionSerializer(serializers.Serializer):
    blog = serializers.CharField(validators=[validar_blog])
    email= serializers.EmailField()
    
    # def validate(self, data):
    #     blog_id = data['blog']
    #     if not ( Blog.objects.filter(id=blog_id).exists()):
    #         raise serializers.ValidationError("el id del blog no existe")
        
    #     return data

class AuthorSerializer(serializers.ModelSerializer):

    num_blogs = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Author
        fields = (
          'id',
          'full_name',
          'email',
          'num_blogs',
        )
    
    def get_num_blogs(self, obj):
        blogs = Blog.objects.filter(
          author__id=obj.id
        ).count()
        return blogs

    def get_full_name(self, obj):
        return obj.full_name.upper()


class KwordSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Kword
        fields = ('__all__')


class CategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')


class CategoryHiperLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url',)
        
        extra_kwargs = {
          'url': {
            'view_name':'blog_app:category-detail',
            'lookup_field': 'pk'
          },
        }


class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    kwords = KwordSerilizer(many=True)
    categorys = CategoryHiperLinkSerializer(many=True)
    
    class Meta:
        model = Blog
        fields = (
          'id',
          'author',
          'kwords',
          'categorys',
          'title',
          'resume',
          'image',
          'content',
          'date',
        )