# django_get_data
register.html的form加上enctype="multipart/form-data"会把所有的input提交的东西放到post中，文件内容会放到files中,\
        添加此参数POST中使用get时获取不到文件名的,需要使用obj.name获取文件名	
obj = request.FILES.get('msg',None)
        print(obj,type(obj),obj.name)
