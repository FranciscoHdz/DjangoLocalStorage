import imp
import json
from re import template
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.shortcuts import render
import json

class index(View):

    def get(self,request):
        template_name = 'test.html'
        return render(request, template_name=template_name)

    def post(self,request):
        if len(list(request.POST.keys())) == 0:
            dataTemp = json.loads(request.body)
            postData = dataTemp.get('nombre')
            dataFrom = "tempData"
        else:
            postData = request.POST.get('nombre')
            dataFrom = "origen"
        print(f"prueba de guardado de datos: {postData}  desde {dataFrom}" )

        return JsonResponse({'prueba':1})