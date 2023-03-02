from django.shortcuts import render, get_object_or_404
from datetime import datetime
from . models import Event


def details(request, id):
    event = get_object_or_404(Event, id = id)
    return render(request, 'events/details.html', {"event": event})


def list(request):
    today = datetime.today()
    # events = Event.objects.filter(datetime__gte = today).order_by('datetime')
    # return render(request, 'events/list.html', {'events': events})

    query_params = request.GET

    filter_map ={
        "title":"name__iexact",
        # "is_free" : "cost"
    }

    filters = {}
    for key, value in query_params.items():
        filter_key = filter_map[key]
        if value:
            filters[filter_key] = value

    events = Event.objects.filter(**filters)   

    context = {
        "events": events
    }

    return render(request, 'events/list.html', context)   
