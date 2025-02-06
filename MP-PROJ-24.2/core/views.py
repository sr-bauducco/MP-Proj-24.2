from rest_framework import viewsets
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
