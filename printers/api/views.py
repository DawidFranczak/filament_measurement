from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serialized import PrinterSerializer
from printers.models import Printer


@api_view(['GET'])
# /api/printer/all/
def get_printer_all(request):
    pinters = Printer.objects.all()

    return Response(PrinterSerializer(pinters, many=True).data)
