from rest_framework import viewsets
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, RegisterSerializer, CustomTokenObtainPairSerializer
from .models import User, Produto, Feira, Banca, Avaliacao
from .serializers import UserSerializer, ProdutoSerializer, FeiraSerializer, BancaSerializer, AvaliacaoSerializer

# ViewSet para User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ViewSet para Produto
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(vendedor=self.request.user)

# ViewSet para Feira
class FeiraViewSet(viewsets.ModelViewSet):
    queryset = Feira.objects.all()
    serializer_class = FeiraSerializer

# ViewSet para Banca
class BancaViewSet(viewsets.ModelViewSet):
    queryset = Banca.objects.all()
    serializer_class = BancaSerializer


# ViewSet para Avaliacao
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

# Registro de novo usuário
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# Login com JWT
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# Logout (Opcional: apenas remove o token do frontend)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    return Response({"message": "Logout realizado com sucesso."}, status=200)