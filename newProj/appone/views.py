from django.shortcuts import render,HttpResponse
from appone.models import User
# import pdb; pdb.set_trace()
# Create your views here.
def index(request):
	return render(request,'appone/index.html')

def users(request):

	user_list = User.objects.order_by('first_name')
	user_dict = {'users': user_list}
	return render(request,'appone/users.html',context=user_dict)