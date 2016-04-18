from django.shortcuts import render
from .models import Report
from .forms import ReportForm
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404

# Create your views here.

def index(request):
    return render(request, 'report_home.html')
def create(request):
    if request.method == "GET":
        success = ""
        page_data = { 'form': ReportForm() }
        return render( request, 'report_create.html', page_data )
    elif request.method == "POST":
        cid = request.user.id
        form = ReportForm( request.POST )
        success = ""
        failure = ""
        if form.is_valid():
            report_name = request.POST.get("report_name")
            date = form.cleaned_data['date']
            sdesc = form.cleaned_data["sdesc"]
            ldesc = form.cleaned_data['ldesc']
            priv = form.cleaned_data["private"]
            if(request.POST.get("file1") != None):
                file1 = request.POST.get("file1")
            if(request.POST.get("file2") != None):
                file2 = request.POST.get("file2")
            if(request.POST.get("file3") != None):
                file3 = request.POST.get("file3")
            rep = Report(creator_id=cid, report_name=report_name, date=date, sdesc=sdesc, ldesc=ldesc, private=priv)
            rep.save()
            success = "Report has been saved!"
            return render( request, 'report_create.html', {
            'form': ReportForm(),
            'success': success
        } )
        else:
            failure = "Submission Failed"
            return render( request, 'report_create.html', {
                'form': ReportForm(),
                'failure': failure
            })
        page_data = { 'form': ReportForm() }
        return render( request, 'report_create.html', {
            'form': ReportForm(),
        } )
    else:
        return render(request, 'report_create.html')
def manage(request):
    if request.method=="POST":
        hi = "hi"
    report_data = Report.objects.all()
    return render(request, 'report_manage.html', {
                'report_all': report_data
            })