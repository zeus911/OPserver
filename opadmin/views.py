from django.shortcuts import render

# Create your views here.
from opadmin.models import ServerFunCateg
from opadmin.models import ServerAppCateg
from opadmin.models import ServerHostList
from opadmin.models import ModuleList

###########################################

def index(request):
	return render(request, 'main.html')
"""
return server function categ
"""
