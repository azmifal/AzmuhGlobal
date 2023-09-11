from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Muhammad Azmi Falah',
        'npm': '2206082285',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)