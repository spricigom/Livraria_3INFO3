from rest_framework.viewsets import ModelViewSet

from core.models import Compra
from core.serializers import CompraCreateUpdateSerializer, CompraSerializer


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    queryset = Compra.objects.order_by('-id')
    serializer_class = CompraSerializer

    def get_serializer_class(self):
        if self.action in {'create', 'update'}:
            return CompraCreateUpdateSerializer
        return CompraSerializer
