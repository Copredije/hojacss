from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Acta
from .forms import ActaForm
from django.shortcuts import redirect
from django.views.generic import View
from django.http import HttpResponse
#from weasyprint import HTML
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from django.template.loader import get_template
from io import BytesIO
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader
#import cv2



def acta_list(request):
    actas = Acta.objects.order_by('fecha')
    return render(request,'cssapp/acta_list.html',{'actas': actas})

def acta_detail(request, pk):
    acta = get_object_or_404(Acta, pk=pk)
    return render(request,'cssapp/acta_detail.html',{'acta': acta})

def acta_new(request):
    if request.method == "POST":
        form = ActaForm(request.POST)
        if form.is_valid():
            acta = form.save(commit=False)
            acta.coordinador = request.user
            acta.save()
            return redirect('cssapp:acta_detail',acta.pk)            
    else:
        form = ActaForm()
    return render(request,'cssapp/acta_edit.html',{'form':form})

def acta_edit(request, pk):
    acta=get_object_or_404(Acta, pk=pk)
    if request.method == "POST":
        form = ActaForm(request.POST, instance=acta)
        if form.is_valid():
            acta = form.save(commit=False)
            acta.coordinador = request.user
            acta.save()
            return redirect('cssapp:acta_detail',acta.pk)            
    else:
        form = ActaForm(instance=acta)
    return render(request, 'cssapp/acta_edit.html', {'form': form})

#from firma import firmado
#def acta_firmacss(request):
    #firmadocss=


#class ActaCssPdf(View):

    #def get(self, request, *args, **kwargs):
        #template=get_template('cssapp/acta_detail_pdf.html')
        #data={
        #   'acta':acta
        #}
        #html=template.render(data)
        #response=HttpResponse(content_type='cssapp/pdf')
        #pisaStatus=pisa.CreatePDF(html, dest=response)
        #return response

# defining the function to convert an HTML file to a PDF file
def actacss_pdf(request, pk):
     acta=get_object_or_404(Acta, pk=pk)
     context={'acta': acta}
     template = get_template('cssapp/acta_pdf.html')
     html  = template.render(context)
     result = BytesIO()
     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
     if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='cssapp/pdf')
     return none

#Creating a class based view
#class ActaPdf(View):

    #def get(self, request, pk, *args, **kwargs):
        
        #getting the template
        #pdf = html_to_pdf('cssapp/acta_pdf.html')
         
         # rendering the template
        #return HttpResponse(pdf, content_type='cssapp/pdf')
        

