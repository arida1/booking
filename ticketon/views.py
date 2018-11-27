from django.shortcuts import render, get_object_or_404

from .models import Cinema, Schedule, Tickets

def user_list(request):
    return render(request, 'ticketon/user_list.html', {})

def cinema_list(request):
    cinemas = Cinema.objects.all()
    return render(request, 'ticketon/cinema_list.html', {'cinemas': cinemas})

def cinema_detail(request, pk):
    schedule = Schedule.objects.filter(cinema_name=pk)
    cinema = get_object_or_404(Cinema, pk=pk)
    return render(request, 'ticketon/cinema_detail.html', {'cinemas': cinema, 'schedules': schedule})
#
#
def ticket_list(request, pk1):
    ticket = Tickets.objects.filter(schedule=pk1)
    post = get_object_or_404(Schedule, pk=pk1)
    return render(request, 'ticketon/ticket_list.html', {'schedules': post, 'tickets': ticket})
