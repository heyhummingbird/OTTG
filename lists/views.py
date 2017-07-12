from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item

def home_page(request):
#    return HttpResponse('<html><title>To-Do Lists</title></html>')
    if request.method == 'POST':
        new_item_text = request.POST['input_item']
        Item.objects.create(text=new_item_text)
        return redirect('/lists/the-only-list/')

    return render(request, 'home.html')

def view_list(request):
    return render(request, 'list.html', {
        'items': Item.objects.all()
    })
