from django.shortcuts import render

# Create your views here.
import os
from django.shortcuts import render
from django.shortcuts import redirect


def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        # user = request.POST.get('user',None)
        # pwd = request.POST.get('pwd',None)
        # gender = request.POST.get('gender',None)
        # favor = request.POST.getlist('favor',None)  #get the more value
        # city = request.POST.getlist('city',None)
        obj = request.FILES.get('msg',None)
        print(obj,type(obj),obj.name)

        file_path = os.path.join('upload',obj.name)
        with open(file_path,'wb') as f:
            for info in obj.chunks():
                f.write(info)
        return render(request,'register.html')
    else:
        return render(request,'register.html')
