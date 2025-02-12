from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserViewSet, ProdutoViewSet, FeiraViewSet, BancaViewSet, AvaliacaoViewSet

# Criando o roteador para registrar os viewsets
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'feiras', FeiraViewSet)
router.register(r'bancas', BancaViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('produtos.urls')),
]
