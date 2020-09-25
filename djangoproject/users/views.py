from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from users.forms import CreateRecord

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


class EvenUsersView(LoginRequiredMixin, generic.ListView):
    model = UserModel
    context_object_name = 'even_user_list'
    queryset =  UserModel.objects.filter(age__iregex='^\d*[02468]$')
    template_name = "even.html"


class AllRecords(LoginRequiredMixin, generic.ListView):
    model = UserModel
    context_object_name = 'user_list'
    queryset = UserModel.objects.all()
    template_name = "all_records.html"


import users.urls 


@login_required
def create_record(request):
    new_user = UserModel

    if request.method == "POST":
        form = CreateRecord(request.POST)
        
        if form.is_valid():
            new_user.age = form.cleaned_data["age"]
            form.save()
            
            return HttpResponseRedirect("../all_records")
        
    else:
        form = CreateRecord(initial={'age': "101"})
    
    context = {
        'form': form,
        'new_user': new_user
    }

    return render(request, 'create_record.html', context)