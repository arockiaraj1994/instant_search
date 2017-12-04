from django.http import HttpResponse
from models import Student
from django.shortcuts import render
import simplejson as json


def get_students(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        students = Student.objects.filter(name__icontains = q )[:20]
        results = []
        for drug in students:
            drug_json = {}
            drug_json['id'] = drug.id
            drug_json['label'] = drug.name
            drug_json['value'] = drug.name
            results.append(drug_json)
        data = json.dumps(results)
    else:
        data = 'fails'
    mimetype = 'application/json'
    #return render(request, 'base.html')
    print data
    return HttpResponse(data, mimetype)

def index(request):
    return render(request, 'base.html')