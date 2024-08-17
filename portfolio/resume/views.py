from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

# views.py

def project(request):
    projects_show = [

        {
            'title': 'CRUD operations APP : Django',
            'path': 'images/crud.png',
            'github_url': 'https://github.com/hari200320/CRUD-operations-in-DJANGO',  
        },
        {
            'title': 'MultiModel Vision',
            'path': 'images/mmv.png',
            'github_url': 'https://multi-model-vision.streamlit.app/',  
        },

        {
            'title': 'Sales Data Analysis : Power BI',
            'path': 'images/sales_data_analysis.PNG',
            'github_url': 'https://github.com/hari200320/PowerBi-Project-Sales-Data-Analysis', 
                },

        {
            'title': 'Amazon Prime Data Analysis : Power BI',
            'path': 'images/amazon_data_analysis.PNG',
            'github_url': 'https://github.com/hari200320/PowerBi-Project-Amazon-Prime-Data-Analysis',  
        },

        {
            'title': 'GetMyAudit',
            'path': 'images/GetMyAudit.png',
            'github_url': 'https://getmyaudit.com/',  
        },
        
        {
            'title': 'PGLife',
            'path': 'images/PGLife.png',
            'github_url': 'https://www.pglifes.com/', 
        },
        
        
        {
            'title': 'Portfolio',
            'path': 'images/portfolio.PNG',
            'github_url': 'https://github.com/hari200320/Portfolio_Django',  
        },
        
    ]
    return render(request, "project.html", {"projects_show": projects_show})


def experience(request):
    experience=[
        {"company":"CodeSight Global Solutions Pvt.Ltd",
         "position":"Web developer"},
        {"company":"KalpinTech Pvt.Ltd",
         "position":"Drone Integration"},
        {"company":"Google Developer Student Clubs",
         "position":"Student Member"},
        
    ]
    return render (request,"experience.html",{"experience":experience})


def certification(request):
    return render(request, "certification.html")

def contact(request):
    return render(request, "contact.html")

def resume(request):
    resume_path="resume/Hariharan_R.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="resume.pdf"
            return response
    else:
        return HttpResponse("resume not found", status=404)
