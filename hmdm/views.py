from django.shortcuts import render

def akc_notice_form(request):
    return render(request, 'hmdm/akc_notice_form.html')