from django.shortcuts import render
from .models import Student
# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
#Function based views
def index(request):
    obj=Student.objects.all()
    print(obj)
    return render(request,'course/index.html',{'name':obj})


#List Based Class view
# class MyView(ListView):
#     template_name = 'course/index_class.html'
#     model=Student
#     def get_context_data(self, *args, **kwargs):
#         context=super().get_context_data()
#         print(context)
#         return context



#Detail based view
# class MyDetailView(DetailView):
#     template_name = 'course/index_detail.html'
#     model=Student
#     def get_context_data(self,*args, **kwargs):
#         context=super().get_context_data(*args,**kwargs)
#         print(context)
#         print(*args)
#         return context







