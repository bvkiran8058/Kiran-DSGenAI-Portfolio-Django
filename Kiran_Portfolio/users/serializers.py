from rest_framework import serializers
from .models import CustomUser, Profile, ProfessionalInfo, SocialLinks


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class ProfessionalInfoSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProfessionalInfo
        fields = '__all__'


class SocialLinksSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = SocialLinks
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    professional_info = ProfessionalInfoSerializer(read_only=True)
    social_links = SocialLinksSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }