from django.shortcuts import render
from django.forms.models import model_to_dict
from .models import Report
from .models import Folder
from .forms import ReportForm
from .forms import deleteReportForm
from .forms import FolderForm
from auth.models import UserProfile
from itertools import chain

from django.db.models import Q
#from .forms import EditReportForm
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404

# Create your views here.

def index(request):
    return render(request, 'report_home.html')

def fmanage(request):
    current_user = request.user
    folder_data = Folder.objects.all()
    permission = ""
    if current_user.is_superuser== False:
        folder_data = Folder.objects.filter(Q(creator=current_user)|Q(private=False)|Q(shared_users=current_user))
    if request.method == "POST":
        for x in folder_data[0:]:
            if request.POST.get(x.uniqueid) != None:
                if x.creator == current_user or UserProfile.objects.get(username=current_user).site_manager is True:
                    x.delete()
                else:
                    permission = "You cannot delete someone else's report."
    return render(request, 'folder_manage.html', {
                'folder_all': folder_data,
                'permission': permission,
            })

def fedit(request, folder_pk):
    f = Folder.objects.get(uniqueid=folder_pk)
    folder_data = Folder.objects.all()
    form = FolderForm(request.POST)
    readonly = ""
    if(f.creator == request.user) or UserProfile.objects.get(username=request.user).site_manager is True:
        if request.method == "POST":
            if form.is_valid():
                folder_name = form.cleaned_data["folder_name"]
                private = form.cleaned_data["private"]
                shared_user_field = form.cleaned_data["shared_user_field"]
                shared_user_names = [x.strip() for x in shared_user_field.split(',')]
                f.shared_users.clear()
                for z in shared_user_names:
                    try:
                        u = User.objects.get(username=z)
                    except User.DoesNotExist:
                        u = None
                    if (u != None):
                        f.shared_users.add(u)
                f.folder_name = folder_name
                f.private = private
                f.save()
                success = "Report has been updated!"
                return render(request, 'folder_edit.html', {
                    'folder': f,
                    'form': form,
                    'success': success
                })
            else:
                failure = "Report edit has failed"
                return render(request, 'report_edit.html', {
                    'folder': f,
                    'form': form,
                    'failure': failure
                })
    else:
        readonly = "READ ONLY"
    form = FolderForm(model_to_dict(f))
    userstring = ""
    for x in f.shared_users.all():
        print(x.username)
        userstring+= x.username
        userstring +=","
    userstring = userstring[:-1]
    fdict = {'folder_name': f.folder_name, 'private': f.private, 'shared_user_field': userstring}
    print(model_to_dict(f))
    form = FolderForm(fdict)
    return render(request, 'folder_edit.html', {
        'readonly': readonly,
        'folder': f,
        'form': form,
    })

def fadd(request, folder_pk):
    f = Folder.objects.get(uniqueid=folder_pk)
    try:
        folder_report = Report.objects.filter(folder=f)
    except Report.DoesNotExist:
        folder_report = None
    try:
        report_mine = Report.objects.filter(creator=request.user).exclude(folder=f)
    except Report.DoesNotExist:
        report_mine = None
    success = ""
    fail = ""
    if f.creator != request.user and UserProfile.objects.get(username=request.user).site_manager is False:
        fail = "You cannot add to a folder you do not own."
    if request.method == "POST":
        for x in report_mine[0:]:
            if f.creator == request.user or UserProfile.objects.get(username=request.user).site_manager is False:
                if request.POST.get(x.uniqueid) != None:
                    x.folder = f
                    x.save()
                    success = "Report has been successfully added to this folder"
    return render(request, 'folder_add.html', {
        'folder_report': folder_report,
        'report_mine': report_mine,
        'folder': f,
        'success': success,
        'fail': fail,
    })

def fremove(request, folder_pk):
    f = Folder.objects.get(uniqueid=folder_pk)
    report_folder = Report.objects.filter(folder=f)
    remove = ""
    fail = ""
    if request.method == "POST":
        for x in report_folder[0:]:
            if x.creator == request.user or UserProfile.objects.get(username=request.user).site_manager is True:
                if request.POST.get(x.uniqueid) != None:
                    x.folder = None
                    x.save()
                    remove = "Report removed successfully!"
            else:
                fail = "You have to own the report to remove it."
    return render(request, 'folder_remove.html', {
        'remove': remove,
        'fail': fail,
        'report_folder': report_folder,
        'folder' : f,
    })


def fcreate(request):
    form = FolderForm(request.POST)
    failure = ""
    success = ""
    if request.method == "GET":
        render(request,'folder_create.html', {'form':form})
    elif request.method =="POST":
        creator = request.user
        if form.is_valid():
            folder_name = form.cleaned_data["folder_name"]
            private = form.cleaned_data["private"]
            shared_user_field = form.cleaned_data["shared_user_field"]
            shared_user_names = [x.strip() for x in shared_user_field.split(',')]
            unique = True
            folder_data = Folder.objects.all()
            for x in folder_data[0:]:
                if x.folder_name == folder_name:
                    unique = False
            if unique:
                f = Folder(creator=creator, folder_name=folder_name, private=private)
                f.save()
                for z in shared_user_names:
                    try:
                        u = User.objects.get(username=z)
                    except User.DoesNotExist:
                        u = None
                    if(u != None):
                        f.shared_users.add(u)
                success = "Folder has been saved!"
            else:
                failure = "Please use a unique folder name."
        else:
            failure = "Folder creation has failed."
    return render(request, 'folder_create.html', {
        'success': success,
        'form': form,
        'failure': failure,
    })

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





            report_data = Report.objects.all()
            unique = True
            # for x in report_data[0:]:
            #     if x.report_name == report_name:
            #         unique = False
            if unique:
                rep = Report(creator_id=cid, report_name=report_name, date=date, sdesc=sdesc, ldesc=ldesc, private=priv, file_1=file1, encrypt_1=encrypt1, file_2=file2, encrypt_2=encrypt2, file_3=file3, encrypt_3=encrypt3, f1n=file1.name, f2n = file2.name, f3n = file3.name)
                rep.save()
                success = "Report has been saved!"
                return render( request, 'report_create.html', {
                'form': form,
                'success': success
                })
            else:
                failure = "Please use a unique report name"
                return render( request, 'report_create.html', {
                    'form': form,
                    'failure': failure
                })
        else:
            failure = "Submission Failed"
            return render( request, 'report_create.html', {
                'form': form,
                'failure': failure
            })
        page_data = { 'form': ReportForm() }
        return render( request, 'report_create.html', {
            'form': form,
        } )
    else:
        return render(request, 'report_create.html')

def manage(request):
    current_user = request.user
    permission = ""
    report_data = Report.objects.all()
    #if(current_user.site_manager == False):
    if request.user.is_superuser == False:
        report_data = Report.objects.filter(Q(creator_id=current_user)|Q(private=False))
    if request.method == "POST":
        for x in report_data[0:]:
            if x.creator == request.user or UserProfile.objects.get(username=request.user).site_manager is True:
                if request.POST.get(x.uniqueid)!= None:
                    x.delete()
            else:
                permission = "You cannot delete someone else's report."
    return render(request, 'report_manage.html', {
                'report_all': report_data,
                'form': deleteReportForm(),
                'permission': permission
            })

def reportedit(request, report_pk):
    r = Report.objects.get(uniqueid=report_pk)
    report_data = Report.objects.all()
    readonly = ""
    form = ReportForm( request.POST , request.FILES)
    if(request.user == r.creator) or UserProfile.objects.get(username=request.user).site_manager is True:
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
                if encrypt1 != None:
                    r.f1n = encrypt1.name
                if(encrypt2 != None):
                    r.f2n = encrypt2.name
                if(encrypt3 != None):
                    r.f3n = encrypt3.name
                r.report_name = report_name
                r.date = date
                r.sdesc = sdesc
                r.ldesc = ldesc
                r.private = priv
                r.file_1 = file1
                r.file_2 = file2
                r.file_3 = file3
                r.encrypt_1 = encrypt1
                r.encrypt_2 = encrypt2
                r.encrypt_3 = encrypt3
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
    else:
        readonly = 'READ ONLY'
    form = ReportForm(model_to_dict(r))
    f1n = "None"
    f2n = "None"
    f3n = "None"
    if(r.f1n!= None):
        f1n = r.f1n;
    if (r.f2n != None):
        f2n = r.f2n;
    if (r.f3n != None):
        f3n = r.f3n;
    print("FILE1:" + f1n  + " asdfdsa" + f1n)
    return render(request, 'report_edit.html', {
        'readonly': readonly,
        'report': r,
        'form': form,
        'f1n': f1n,
        'f2n': f2n,
        'f3n': f3n,
    })

def addreport(request, folder_pk, report_pk):
    return render(request, 'report_home.html')



