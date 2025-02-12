from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProdutoViewSet, FeiraViewSet, BancaViewSet, AvaliacaoViewSet,RegisterView, CustomTokenObtainPairView, logout_view

# Criando o roteador para registrar os viewsets
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'feiras', FeiraViewSet)
router.register(r'bancas', BancaViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
   # path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/logout/', logout_view, name='logout'),

]
