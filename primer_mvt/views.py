from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, loader, Context
from primer_mvt.models import Familia
from django.template.loader import get_template
# Create your views here.

def familia(self):
    familia1 = Familia(nombre = "juan", apellido = "ramirez", edad = 80, fecha = "1982-01-06")
    familia1.save()

    familia2 = Familia(nombre = "roberto", apellido = "gimenez", edad = 51, fecha = "1988-03-04")
    familia2.save()

    familia3 = Familia(nombre = "maria", apellido = "pereyra", edad = 15, fecha = "2000-08-09")
    familia3.save()

    documento = f"Abuelo: {familia1.nombre} {familia1.apellido}<br> Edad: {familia1.edad}<br> Fecha favorita: {familia1.fecha}<br><br> Padre: {familia2.nombre} {familia2.apellido}<br> Edad: {familia2.edad}<br>Fecha favorita: {familia2.fecha}<br><br> Hermana: {familia3.nombre} {familia3.apellido}<br> Edad: {familia3.edad}<br> Fecha favorita: {familia3.fecha}"
   

    return HttpResponse(documento)