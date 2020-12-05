from django.shortcuts import render
from cap.models import CampusAmbassador
from cap.forms import CampusAmbassadorForm
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def cap_index(request):

    leaderboard_list = CampusAmbassador.objects.all().order_by('points')[:4]
    context = { 'leaderboad' : leaderboard_list }

    if request.method == "POST":
        form = CampusAmbassadorForm(request.POST)
        if form.is_valid():
            ambassador = form.save(commit=False)
            ambassador.points = 0
            ambassador.save()
            messages.success(request, 'You have successfully registered')
        else:
            errors = dict(form.errors)
            if "already exists" in errors['email'][0]:
                messages.error(request, 'You have already registered')
            elif "already exists" in errors['phone_number'][0]:
                messages.error(request, 'You have already registered')
            else:
                messages.error(request, 'Form Submission Unsuccessful')
        return HttpResponseRedirect(reverse('cap:index'))
    else:
        form = CampusAmbassadorForm()
        context['register_form'] = form

    return render(request, 'cap/index.html', context=context)