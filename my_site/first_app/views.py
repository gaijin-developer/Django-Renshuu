from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseNotFound,Http404,HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def simple_view(request):
   return render(request,"first_app/example.html",)































# articles={"sports":"sports page","finance":"finance page","history":"history page"}

# def news_view(request,topic):
#    try:
#       result=articles[topic]
#       return HttpResponse(articles[topic])
#    except:
#       result="No page for this topic"
#       raise Http404(result)

# # def finance_view(request):
# #    return HttpResponse(articles["finance"])

# def add_view(request,num1,num2):
#     result = num1 + num2
#     return HttpResponse(str(result))
 
# def num_page_view(request,num_page):
#    try:
#       topics_list=list(articles.keys())
#       topic=topics_list[num_page]
      
#       webpage = reverse("topics-page",args=[topic])
#       return HttpResponseRedirect(webpage)
#    except:
#       raise Http404("page not found")
    