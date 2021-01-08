from django.shortcuts import render, redirect
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
        'url': "/get_ticket/inflate_tires/",
        'time': 5,
        'type': 'tires'
    },
    {
        'text': "Get diagnostic test",
        'url': "/get_ticket/diagnostic/",
        'time': 30,
        'type': 'test'
    },
]

line_of_cars = {
    'oil': [],
    'tires': [],
    'test': []
}

REFNUM = 0
customer = 0


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        http = "<h2>Welcome to the Hypercar Service!</h2>"
        return HttpResponse(http)


def menu(request):
    context_menu = {
        'links': links,
        'line_of_cars': line_of_cars,
        'refnum': REFNUM,
    }

    return render(request, 'tickets/menu.html', context_menu)


class Wait(View):

    def get(self, request, *args, **kwargs):
        global line_of_cars, REFNUM
        REFNUM += 1
        full_path = request.get_full_path()
        if full_path == "/get_ticket/change_oil/":
            line_of_cars['oil'].append(REFNUM)
            wait = (len(line_of_cars['oil']) - 1) * links[0]['time']
        elif full_path == '/get_ticket/inflate_tires/':
            line_of_cars["tires"].append(REFNUM)
            wait = (len(line_of_cars['oil'])) * links[0]['time'] + (len(line_of_cars['tires']) - 1) * links[1]['time']
        elif full_path == '/get_ticket/diagnostic/':
            line_of_cars["test"].append(REFNUM)
            wait = (len(line_of_cars['oil'])) * links[0]['time'] + (len(line_of_cars['tires'])) * links[1]['time'] + (
                        len(line_of_cars['test']) - 1) * links[2]['time']
        else:
            wait = 0

        return render(request, 'tickets/waiting_room.html', {
            'ref_num': REFNUM,
            "wait": wait
        })


clicks = 0


class Processing(View):
    global REFNUM

    def get(self, request, *args, **kwargs):
        return render(request, 'tickets/processing.html',
                      {'clicks': clicks, "queue": line_of_cars, 'customer': customer})

    def post(self, request, *args, **kwargs):
        global customer
        if request.method == "POST":
            if len(line_of_cars['oil']) > 0:
                customer = line_of_cars['oil'].pop(0)
            elif len(line_of_cars['tires']) > 0:
                customer = line_of_cars['tires'].pop(0)
            elif len(line_of_cars['test']) > 0:
                customer = line_of_cars['test'].pop(0)
            else:
                customer = 0

        else:
            customer = 0

        return redirect('/processing')


class Next(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tickets/next.html', {'customer': customer})




