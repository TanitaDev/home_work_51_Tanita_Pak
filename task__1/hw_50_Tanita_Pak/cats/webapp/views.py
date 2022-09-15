from django.shortcuts import render

from webapp.data_base import cat


def index_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        context = {
            'name': request.POST.get('name'),
            'image': cat.change_image(),
            'age': cat.age,
            'satiety': cat.change_satiety(request.POST.get('cat_actions')),
            'happiness': cat.change_happiness(request.POST.get('cat_actions')),
            'activity': cat.set_activity(request.POST.get('cat_actions')),
        }
        return render(request, 'view_cat.html', context)
