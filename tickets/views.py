from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

links = [
    {
        'text': "Change oil",
        'url': "/get_ticket/change_oil/",
        'time': 2,
        'type': 'oil'
    },
    {
        'text': "Inflate tires",
        'url': "/get_ticket/inflate_tires",
        'time': 5,
        'type': 'tires'
    },
    {
        'text': "Get diagnostic test",
        'url': "/get_ticket/diagnostic",
        'time': 30,
        'type': 'test'
    },
]

line_of_cars = {
    'oil': [],
    'tires': [],
    'test': []
}


REFNUM = 1

class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        http="<h2>Welcome to the Hypercar Service!</h2>"
        return HttpResponse(http)


def menu(request):
    global REFNUM
    context_menu = {
        'links': links,
        'line_of_cars': line_of_cars,
        'refnum': REFNUM,
    }
    REFNUM += 1
    return render(request, 'tickets/menu.html', context_menu)


class Wait(View):

    def get(self, request, *args, **kwargs):

        global line_of_cars
        print(request.GET.get())
        services = 0 if request.GET.get('services') is None else request.GET.get('services')
        if request.GET.get('ref_num') is None:
            ref_num = 0
        else:
            ref_num = request.GET.get('ref_num')
            line_of_cars[services].append(ref_num)

        if services == 'oil':
            wait = (len(line_of_cars['oil'])-1) * links[0]['time']
        elif services == 'tires':
            wait = (len(line_of_cars['oil']))*links[0]['time'] + (len(line_of_cars['tires'])-1)*links[1]['time']
        elif services == 'test':
            wait = (len(line_of_cars['oil']))*links[0]['time'] + (len(line_of_cars['tires']))*links[1]['time'] + (len(line_of_cars['test'])-1)*links[2]['time']
        else:
            wait = 0
        return render(request, 'tickets/waiting_room.html', {
            'ref_num': ref_num,
            'services': services,
            "wait": wait
        })
