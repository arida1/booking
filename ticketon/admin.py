from django.contrib import admin
from .models import User, Cinema, Movie, Schedule, Tickets

admin.site.register(User)
admin.site.register(Cinema)
admin.site.register(Movie)
admin.site.register(Schedule)
admin.site.register(Tickets)
