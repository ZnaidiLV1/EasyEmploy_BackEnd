from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import *


@api_view(["POST"])
def create_field(request):
    try:
        data = request.data
        field = Fields.objects.create(
            name=data["name"]
        )
        serializer = fieldserializer(field, many=False)
        return Response(serializer.data)
    except Fields.DoesNotExist:
        return Response("field does not exist")
    except Exception as e:
        return Response("exc " + str(e))


@api_view(["GET"])
def get_field(request, field_id):
    try:
        field = Fields.objects.get(id=field_id)
        serializer = fieldserializer(field, many=False)
        return Response(serializer.data)
    except Fields.DoesNotExist:
        return Response("Field Does not exist")
    except Exception as e:
        return Response(str(e))


@api_view(["PUT"])
def update_field(request, field_id):
    try:
        data = request.data
        field = Fields.objects.get(id=field_id)
        field.name = data["name"]
        field.save()
        serializer = fieldserializer(field, many=False)
        return Response(serializer.data)
    except Fields.DoesNotExist:
        return Response("Field Does not exist")
    except Exception as e:
        return Response(str(e))


@api_view(["DELETE"])
def delete_field(request, field_id):
    try:
        field = Fields.objects.get(id=field_id)
        field.delete()
        return Response("field deleted successfully")
    except Fields.DoesNotExist:
        return Response("Field Does not exist")
    except Exception as e:
        return Response(str(e))


# CVPERFIELD
@api_view(["POST"])
def create_cvPerField(request):
    try:
        data = request.data
        field = Fields.objects.get(id=data["field_id"])
        cv = CV.objects.get(id=data["cv_id"])
        cpf = CvPerField.objects.create(
            field_id=field,
            cv_id=cv
        )
        serializer = cvPerFieldserializer(cpf, many=False)
        return Response(serializer.data)
    except CvPerField.DoesNotExist:
        return Response("cvPerField does not exist")
    except Exception as e:
        return Response(str(e))


@api_view(["GET"])
def get_cvFields(request, cv_id):
    try:
        cpf = CvPerField.objects.filter(cv_id=cv_id).values_list("field_id",flat=True)
        fields=Fields.objects.filter(id__in=cpf)
        serializer = fieldserializer(fields, many=True)
        return Response(serializer.data)
    except CvPerField.DoesNotExist:
        return Response("cpf does not exist")
    except Exception as e:
        return Response(str(e))


@api_view(["DELETE"])
def delete_cvPerField(request):
    try:
        data = request.data
        cpf = CvPerField.objects.get(field_id=data["field_id"],cv_id=data["cv_id"])
        cpf.delete()
        return Response("cpf deleted")
    except CvPerField.DoesNotExist:
        return Response("CvPerField does not exist")
    except Exception as e:
        return Response(str(e))

# CompanyCardPerField
@api_view(["POST"])
def create_ccpf(request):
    try:
        data = request.data
        comanyCard = CompanyCard.objects.get(id=data["companyCard_id"])
        field = Fields.objects.get(id=data["field_id"])
        ccpf = CompanyCardPerField.objects.create(
            companyCard_id=comanyCard,
            field_id=field
        )
        serializer = companyCardPerFieldserializer(ccpf, many=False)
        return Response(serializer.data)
    except Fields.DoesNotExist:
        return Response("Field does not exist")
    except CompanyCard.DoesNotExist:
        return Response("CompanyCard does not exist")
    except Exception as e:
        return Response(str(e))

@api_view(["GET"])
def get_companyCardFields(request,companyCard_id):
    try:
        data = request.data
        ccpf = CompanyCardPerField.objects.filter(companyCard_id=companyCard_id).values_list("field_id",flat=True)
        fields = Fields.objects.filter(id__in=ccpf)
        serializer = fieldserializer(fields, many=True)
        return Response(serializer.data)
    except CompanyCard.DoesNotExist:
        return Response("CompanyCard does not exist")
    except Exception as e:
        return Response(str(e))

@api_view(["DELETE"])
def delete_ccpf(request):
    try:
        data = request.data
        ccpf = CompanyCardPerField.objects.get(id=data["ccpf_id"])
        ccpf.delete()
        return Response("deleted")
    except CompanyCardPerField.DoesNotExist:
        return Response("ccpf des not exist")
    except Exception as e:
        return Response(str(e))

# Create your views here.
