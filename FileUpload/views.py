from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.utils.encoding import smart_str
from django.conf import settings
import os

#from report_database.models import Report
from FileUpload.models import Document
from FileUpload.forms import DocumentForm


def list(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            return HttpResponseRedirect(reverse('FileUpload.views.list'))
    else:
        form = DocumentForm()

    documents = Document.objects.all()

    return render_to_response(
            'list.html',
            {'documents': documents, 'form': form},
            context_instance=RequestContext(request)
    )

def download(request):
    file_name = request.GET.get('per_page')
    #file_path = settings.MEDIA_ROOT +'/'+ file_name
    #file_wrapper = FileWrapper(file(file_path,'rb'))
    #file_mimetype = mimetypes.guess_type(file_path)
    path_to_file = "/media/{0}".format(file_name)
    response = HttpResponse(content_type='application/force-download')
    #response = HttpResponse(file_wrapper, content_type=file_mimetype )
    #response['Content-Length'] = os.stat(file_name).st_size
    response['Content-Disposition'] = 'attachment; filename=%s/' % smart_str(file_name)
    response['X-Sendfile'] = smart_str(path_to_file)
    return response

#def download(request,file_name):
 #   file_path = settings.MEDIA_ROOT +'/'+ file_name
  #  file_wrapper = FileWrapper(file(file_path,'rb'))
   # file_mimetype = mimetypes.guess_type(file_path)
#    response = HttpResponse(file_wrapper, content_type=file_mimetype )
 #   response['X-Sendfile'] = file_path
  #  response['Content-Length'] = os.stat(file_path).st_size
   # response['Content-Disposition'] = 'attachment; filename=%s/' % smart_str(file_name) 
    #return response

#def getFile(request):
 #   reports = Report.objects.all()
    #privReports = Report.objects.all().filter(private=True)
    #if request.method == 'POST':
     #   for i in reports[0:]:
      #      if i.private == False:
       #         if i.file_1:
        #            newdoc = Document(docfile = i.file_1)
         #           newdoc.save()
          #      if i.file_2:
           #         newdoc = Document(docfile = i.file_2)
            #        newdoc.save()
             #   if i.file_3:
              #      newdoc = Document(docfile = i.file_3)
               #     newdoc.save()
  #  document = Document.objects.all()
   # return render(request, 'files.html',{'files' : reports, 'documents': document})

