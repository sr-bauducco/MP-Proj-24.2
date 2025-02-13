from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User, Produto, Feira, Banca, Avaliacao
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=['cliente','feirante', 'administrador'])  # Adicionando campo role

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']

    def create(self, validated_data):
        # Criação do usuário com base nos dados recebidos
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role = validated_data['role']
        )
        # Se necessário, adicione o campo 'role' em outro modelo relacionado (como 'Perfil')
        user.save()
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Customizar para usar email e password no login"""
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        # Buscar o usuário com o email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("E-mail ou senha inválidos.")
        
        # Verificar se a senha está correta
        if not user.check_password(password):
            raise serializers.ValidationError("E-mail ou senha inválidos.")

        # Se a autenticação for bem-sucedida, gere o token
        data = super().validate(attrs)
        data['user'] = {
            'id': user.id,
            'email': user.email,
            'username': user.username
        }
        return data


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class FeiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feira
        fields = '__all__'

class BancaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banca
        fields = '__all__'

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'
