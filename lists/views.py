from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item, List
import json

def home_page(request):
#    return HttpResponse('<html><title>To-Do Lists</title></html>')
    return render(request, 'home.html')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {
        'list':list_
    })

def new_list(request):
    new_item_text = request.POST['input_item']
    list_ = List.objects.create()
    Item.objects.create(text=new_item_text, list=list_)
    return redirect(f'/lists/{list_.id}/')

def add_item(request, list_id):
    new_item_text = request.POST['input_item']
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=new_item_text, list=list_)
    return redirect(f'/lists/{list_.id}/')

def delete_item(request, list_id, item_id):
    if request.method == 'POST':
        Item.objects.filter(id=item_id).delete()
        return redirect(f'/lists/{list_id}/')

def done_item(request, list_id):
    if request.method == 'POST':
#        print(request)
#        print(type(request))
#        print(request.META)
#        print(request.META['CONTENT_TYPE'])
#        print(type(request.META))
#        print(dir(request.META))
#        print(getattr(request, "META"))
        body_unicode = request.body.decode('utf-8')
#        print(body_unicode)
        body_data = json.loads(body_unicode)
#        print(body_data)
        item = Item.objects.filter(id=body_data['item_id'])[0]
        item.done = not item.done
        item.save()
        return redirect(f'/lists/{list_id}/')
