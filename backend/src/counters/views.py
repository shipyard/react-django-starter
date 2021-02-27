from django.http import JsonResponse
import datetime

from .models import Counter

RESPONSE_TEMPLATE = 'Django server running on port 8080. Pinged {count} {times}, \
most recently on {date}.'


def reset(request):
    counter = Counter.objects.last()
    counter.reset()

    return JsonResponse({'response': counter.value})


def index(request):
    counter = Counter.objects.last()
    if counter:
        counter.increment()
    else:
        counter = Counter()
        counter.save()
    date = datetime.datetime.now()
    date_str = date.strftime('%c')
    times = 'time' if counter.value == 1 else 'times'
    response = RESPONSE_TEMPLATE.format(
        count=counter.value,
        times=times,
        date=date_str)

    return JsonResponse({'response': response})
