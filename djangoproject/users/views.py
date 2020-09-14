from django.shortcuts import render

# Create your views here.
from users.models import UserModel

def index(request):

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    num_users = UserModel.objects.count()
    num_even_age = UserModel.objects.filter(age__iregex='^\d*[02468]$').count()

    context = {
        "num_users": num_users,
        "num_even_age": num_even_age,
        "num_visits": num_visits,
    }

    return render(request, "index.html", context=context)

from django.views import generic

class EvenUsersView(generic.ListView):
    model = UserModel
    context_object_name = 'even_user_list'
    queryset =  UserModel.objects.filter(age__iregex='^\d*[02468]$')
    template_name = "even.html"

class AllRecords(generic.ListView):
    model = UserModel
    context_object_name = 'user_list'
    queryset = UserModel.objects.all()
    template_name = "all_records.html"