
from  django.shortcuts import redirect

def change_url(request):

    url = request.POST.get("custom_url")

    if "https://" not in url:
        url = "http://" + url


    if request.META['HTTP_HOST'].count(".") > 1:
        index = request.META['HTTP_HOST'].find(".")
        main_domain = request.META['HTTP_HOST'][index+1:]
        url = url + "." + main_domain
        return redirect(url)

    else:
        url = url + "." + request.META['HTTP_HOST']
        return redirect(url)

