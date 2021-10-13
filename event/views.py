from django.http import HttpResponse
from django.views.generic import View
from django.contrib.sites.shortcuts import get_current_site

#importing get_template from loader
from django.template.loader import get_template
 
#import render_to_pdf from util.py 
from .utils import render_to_pdf 
from certificate.settings import BASE_DIR
from .models import student
import pyqrcode
import time
import os


# class Index(View):
#     def get(self, request, *args, **kwargs):
        
#Creating our view, it is a class based view
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        s = student.objects.filter(uid = kwargs['uid']).select_related('event').first()
        print(s)
        milliseconds = str(round(time.time() * 1000))
        file  = str(BASE_DIR)+"/event/templates/"+ milliseconds + ".html"
        with open(file, 'w') as f:
            f.write(s.event.html)

        site = "localhost:8000" + "/pdf/{id}".format(id = s.uid)
        code = pyqrcode.create(site)
        image_as_str = code.png_as_base64_str(scale=5)
        html_img = '<img src="data:image/png;base64,{}">'.format(image_as_str)
        pdf = render_to_pdf(file, 
                                    {   'first_name':s.first_name, 
                                        'last_name':s.last_name,
                                        'position': s.position,
                                        'event': s.event.name,
                                        'uid': s.uid,
                                        'qr_code': html_img,
                                    }
                            )
        os.remove(file)
         #rendering the template
        return HttpResponse(pdf, content_type='application/pdf')