from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Inventory

# Create your views here.
def index(request):
    if request.method == 'POST':
        # print(request.POST)
        try:
            name = request.POST['name'].strip()
            price = request.POST['price'].strip()
            desc = request.POST['desc'].strip()

            if not name or not price or not desc:
                return JsonResponse({"data": name}, status=500)

            item = Inventory.objects.create(name=name, desc=desc, price=price)

            item.save()


            return JsonResponse({"data": {"name": name, "price": price, "id": item.id}}, status=200)
        except Exception as e:
            return JsonResponse({"data": name}, status=500)
        # return HttpResponse("Added")

    else:
        items = Inventory.objects.all()
        context = {
            "items": items
        }
        return render(request, "index.html", context)

def remove_item(request):

    if request.method == 'POST':
        try:
            pk = request.POST['id']

            item = Inventory.objects.get(pk=pk)
            name = item.name

            item.delete()

            return JsonResponse({"data": {"name": name}}, status=200)
        except Exception as e:
            return JsonResponse({"data": name}, status=500)


def detail(request, item_id):

    item = get_object_or_404(Inventory, pk=item_id)

    return render(request, 'detail.html', {'item': item})
    # return HttpResponse("{} Added Successfully".format(name))