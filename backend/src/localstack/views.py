import uuid

import localstack_client.session

from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token
import time

BUCKET = 'test-bucket'


def s3_client():
    return localstack_client.session.Session().client('s3')


def index(request):
    s3_client().create_bucket(Bucket=BUCKET)
    return JsonResponse(s3_client().list_objects(Bucket=BUCKET))


def create(request):
    s3_client().put_object(Bucket=BUCKET,
                           Key='{}.txt'.format(uuid.uuid1()),
                           Body=b'some content')
    return redirect('index')


@ensure_csrf_cookie
def upload(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        if file:
            ext = file.name.split('.')[-1]
            timestr = time.strftime('%Y%m%d%H%M%S')
            filename = f'upload-{timestr}.{ext}'
            s3_client().put_object(Bucket=BUCKET,
                                   Key=filename,
                                   Body=file)

    return JsonResponse({'message': filename})


def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})
