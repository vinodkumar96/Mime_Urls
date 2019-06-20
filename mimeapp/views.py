from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
import csv
# Create your views here.
data = """ <table><tr><th>e_id</th>
                        <th>e_name</th>
                        <th>e_sal</th></tr>
                    <tr><td>1001</td>
                        <td>vinod</td>
                        <td>10000.00</td></tr>
                    <tr><td>1002</td>
                        <td>mani</td>
                        <td>15000.00</td></tr>
                    <tr><td>1003</td>
                        <td>vaasu</td>
                        <td>20000.00</td></tr></table>"""
def csvview(request):
    response = HttpResponse(content_type='text/csv')
    response['content-disposition'] = 'attachment:\
                                    filename="myfile.csv"'
    writer = csv.writer(response)
    writer.writerow(['First row', 'foo', 'bar', 'bas'])
    writer.writerow(['second row', 'A', 'B', 'C', "Testing", "Here's a Quote"])
    return response
def pdfview(request):
    response=HttpResponse(content_type='application/pdf')
    response['content-disposition'] = 'attachment:\
                                    filename="myfile.pdf"'
    p= canvas.Canvas(response)
    p.drawString(100,100,"hello world")
    p.showPage()
    p.save()
    return response
def htmlview(request):
    return HttpResponse(data,content_type='text/html')
def xmlview(request):
    return HttpResponse(data,content_type='application/xml')
