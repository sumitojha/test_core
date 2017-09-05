from rest_framework import throttling
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .models import Tenant
from datetime import datetime
import random
from django.utils import timezone

ALLOWED_PATH_LIST = [
    "/qa/view/"
]
ALLOWED_LIMIT = 100


class RandomRateThrottle(throttling.BaseThrottle):
    # rate = '10/second'
    def allow_request(self, request, view):
        if request.method == 'GET' or str(request.path) not in ALLOWED_PATH_LIST:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        if request.method == 'GET' and str(request.path) in ALLOWED_PATH_LIST :
            try:
                tenantobj = Tenant.objects.get(api_key=str(request.META['HTTP_API_KEY']))
                tenantobj.count += 1
                tenantobj.save()
                if tenantobj.count <= 1:
                    return True
                differnce = timezone.now() - tenantobj.last_modified
                if differnce.seconds > 10:
                    tenantobj.last_modified = timezone.now()
                    tenantobj.save()
                    return True
                else:
                    return False

            except ObjectDoesNotExist:
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

            except KeyError as e:
                return HttpResponse("KeyError : {0}".format(e.__str__()), status=status.HTTP_400_BAD_REQUEST)

    def wait(self):
        return 10