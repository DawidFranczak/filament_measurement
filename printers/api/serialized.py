from rest_framework.serializers import ModelSerializer
from printers.models import Printer


class PrinterSerializer(ModelSerializer):

    class Meta:
        model = Printer
        fields = "__all__"
