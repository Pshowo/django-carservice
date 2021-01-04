from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        http="<h2>Welcome to the Hypercar Service!</h2>"
        return HttpResponse(http)


def menu(request):
    links = [
        {
            'text': "Change oil",
            'url': "/get_ticket/change_oil",
        },
        {
            'text': "Inflate tires",
            'url': "/get_ticket/inflate_tires",
        },
        {
            'text': "Get diagnostic test",
            'url': "/get_ticket/diagnostic",
        },
    ]
    context_menu = {'links': links}
    return render(request, 'tickets/menu.html', context_menu)

