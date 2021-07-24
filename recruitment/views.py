from django.shortcuts import render, redirect
from .models import ManagementTeamRecs, WebTeamRecs, MediaTeamRecs
# Create your views here.

def index(request):
    return render(request,'recruitment/index.html',{})
    
def management_form(request):
    if request.method == 'POST':
        print(request.POST)
        m = ManagementTeamRecs(name=request.POST['name'],
        email = request.POST['email'],
        phone = request.POST['phone'],
        roll_number = request.POST['roll_number'],
        answer1 = request.POST['answer1'],
        answer2 = request.POST['answer2'],
        answer3 = request.POST['answer3'])
        
        if request.POST['content_writing']=="yes":
            m.content_writing=True
        
        if request.POST['web']:
            m.web=True
        
        if request.POST['media']:
            m.media=True
        
        m.save()
        return render(request, 'recruitment/management_form.html', {'success_message':"Congrats! you have successfully registered for the management    team"})
    else:    
        return render(request, 'recruitment/management_form.html',{})

def media_form(request):
    
    if request.method == 'POST':
        print(request.POST)
        m = MediaTeamRecs(name=request.POST['name'],
        email = request.POST['email'],
        phone = request.POST['phone'],
        roll_number = request.POST['roll_number'],
        answer1 = request.POST['answer1'],
        answer2 = request.POST['answer2'],
        answer3 = request.POST['answer3'])

        area_of_interest = ''       
        interest_fields = ['digital_marketing', 'poster_creation', 'social_media_content', 'digital_art', 'videography', 'audio_editing']
        for i in interest_fields:
            if request.POST.get(i,False):
                area_of_interest = area_of_interest + i + " " 
        
        if request.POST.get('other_interests',"-") != '-':
            m.other_interests = request.POST.get('other_skills','-')
        m.area_of_interest = area_of_interest

        skills = ''
        if request.POST.get('none_skills',False):
            skills = "NONE";
        else:
            skill_fields = ['illustrator', 'photoshop', 'after_effects','premier_pro','canva']
            for i in skill_fields:
                if request.POST.get(i,False):
                    skills = skills + i + " " 
            if request.POST.get('other_skills',"-") != '-':
                m.other_skills = request.POST.get('other_skills','-')
        m.skills = skills

        m.save()
        print (m.skills)
        print (m.area_of_interest)
        return render(request, 'recruitment/media_form.html', {'success_message':"Congrats! you have successfully registered for the media team"})
    else:    
        return render(request, 'recruitment/media_form.html',{})

def web_form(request):
    if request.method == 'POST':
        print(request.POST)
        w = WebTeamRecs(name=request.POST['name'],
        email = request.POST['email'],
        phone = request.POST['phone'],
        roll_number = request.POST['roll_number'],
        answer1 = request.POST['answer1'],
        answer2 = request.POST['answer2'],
        answer3 = request.POST['answer3'])
        
        skills = ' '
        skill_fields = ['html_css', 'javascript', 'django_or_node', 'git', 'ui_ux', 'react_angular']
        for i in skill_fields:
            if request.POST.get(i,False):
                skills = skills + i + " "
        if request.POST.get('other_skills',"-"):
            w.other_skills = request.POST.get('other_skills','-')

        w.area_of_interest = request.POST['interest']
        w.skills = skills
        w.save()
        return render(request, 'recruitment/web_form.html',{'success_message':"Congrats! you have successfully registered for the web team"})
    else:    
        return render(request, 'recruitment/web_form.html',{})
