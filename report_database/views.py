from django.shortcuts import render
from django.forms.models import model_to_dict
from .models import Report
from .forms import ReportForm
from .forms import deleteReportForm
#from .forms import EditReportForm
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from FileUpload.models import Document
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
        form = ReportForm( request.POST , request.FILES)
        success = ""
        failure = ""
        if form.is_valid():
            report_name = form.cleaned_data["report_name"]
            date = form.cleaned_data['date']
            sdesc = form.cleaned_data["sdesc"]
            ldesc = form.cleaned_data['ldesc']
            priv = form.cleaned_data["private"]
            file1 = form.cleaned_data["file_1"]
            file2 = form.cleaned_data["file_2"]
            file3 = form.cleaned_data["file_3"]
            encrypt1 = form.cleaned_data["encrypt_1"]
            encrypt2 = form.cleaned_data["encrypt_2"]
            encrypt3 = form.cleaned_data["encrypt_3"]


            # if(request.POST.get("file1") != None):
            #     file1 = request.POST.get("file1")
            #     encrypt1 = request.POST.get("")
            # if(request.POST.get("file2") != None):
            #     file2 = request.POST.get("file2")
            # if(request.POST.get("file3") != None):
            #     file3 = request.POST.get("file3")

            report_data = Report.objects.all()
            unique = True
            # for x in report_data[0:]:
            #     if x.report_name == report_name:
            #         unique = False
            if unique:
                rep = Report(creator_id=cid, report_name=report_name, date=date, sdesc=sdesc, ldesc=ldesc, private=priv, file_1=file1, encrypt_1=encrypt1, file_2=file2, encrypt_2=encrypt2, file_3=file3, encrypt_3=encrypt3)
                rep.save()
                #added some changes
                #newdoc = Document(docfile = request.FILES['file_1'])
                #newdoc.save()
                #newdoc = Document(docfile = request.FILES['file_2'])
                #newdoc.save()
                #newdoc = Document(docfile = request.FILES['file_2'])
                #newdoc.save()
                #end changes
                success = "Report has been saved!"
                return render( request, 'report_create.html', {
                'form': ReportForm(),
                'success': success
                })
            else:
                failure = "Please use a unique report name"
                return render( request, 'report_create.html', {
                    'form': ReportForm(),
                    'failure': failure
                })
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
    report_data = Report.objects.all()
    if request.method == "POST":
        for x in report_data[0:]:
            if request.POST.get(x.uniqueid)!= None:
                x.delete()
    return render(request, 'report_manage.html', {
                'report_all': report_data,
                'form': deleteReportForm()
            })

def reportedit(request, report_pk):
    r = Report.objects.get(uniqueid=report_pk)
    report_data = Report.objects.all()

    form = ReportForm( request.POST , request.FILES)

    if request.method == "POST":
        if form.is_valid():
            report_name = form.cleaned_data["report_name"]
            date = form.cleaned_data['date']
            sdesc = form.cleaned_data["sdesc"]
            ldesc = form.cleaned_data['ldesc']
            priv = form.cleaned_data["private"]
            file1 = form.cleaned_data["file_1"]
            file2 = form.cleaned_data["file_2"]
            file3 = form.cleaned_data["file_3"]
            encrypt1 = form.cleaned_data["encrypt_1"]
            encrypt2 = form.cleaned_data["encrypt_2"]
            encrypt3 = form.cleaned_data["encrypt_3"]
            r.report_name = report_name
            r.date = date
            r.sdesc = sdesc
            r.ldesc = ldesc
            r.priv = priv
            r.file_1 = file1
            r.file_2 = file2
            r.file_3 = file3
            r.encrypt_1 = encrypt1
            r.encrypt_2 = encrypt2
            r.encrypt_3 = encrypt3
            print(r.report_name)
            r.save()
            success = "Report has been updated!"
            return render(request, 'report_edit.html', {
                'report': r,
                'form': form,
                'success': success
            })
        else:
            failure = "Report edit has failed"
            return render(request, 'report_edit.html',{
                'report': r,
                'form': form,
                'failure': failure
            })


    form = ReportForm(model_to_dict(r))
    return render(request, 'report_edit.html', {
        'report': r,
        'form': form,
    })