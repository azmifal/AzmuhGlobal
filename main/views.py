import json
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from django.core import serializers
from main.forms import ItemForm
from main.models import Item
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    item_count = items.count()

    context = {
        'name': request.user.username,
        'npm': '2206082285',
        'class': 'PBP B',
        'items': items,
        'amount_items': item_count,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, amount=amount, description=description, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def edit_item(request, id):
    item = Item.objects.get(pk = id)    # Get item berdasarkan ID

    form = ItemForm(request.POST or None, instance=item)     # Set item sebagai instance dari form

    if form.is_valid() and request.method == "POST":
        form.save() # Simpan form dan kembali ke halaman awal
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)

def delete_item(request, id):
    item = Item.objects.get(pk = id)    # Get data berdasarkan ID
    item.delete()   # Hapus data
    return HttpResponseRedirect(reverse('main:show_main'))  # Kembali ke halaman awal

@csrf_exempt
def delete_item_ajax(request, id):
    if request.method == 'DELETE':
        item = get_object_or_404(Item, pk=id, user=request.user)
        item.delete()
        return HttpResponse(status=204)
    return HttpResponseNotFound()

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_item_json(request):
    item_items = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', item_items))

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def create_item_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_item = Item.objects.create(
            user = request.user,
            name = data["name"],
            amount = int(data["amount"]),
            description = data["description"]
        )

        new_item.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)