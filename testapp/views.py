from django.shortcuts import render
from testapp import forms
# Create your views here.
def studentview(request):
    form=forms.StudentForm()
    if request.method=="POST":
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("data inserted successfully")

    return render(request,'testapp/register.html',{'form':form})
