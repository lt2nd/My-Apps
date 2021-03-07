from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect

from emails.forms import InventoryWaitlistForm

from .forms import ProductModelForm
from .models import Product

def featured_product_view(request, *args, **kwargs):
    qs = Product.objects.filter(featured=True)
    product = None
    form = None
    can_order = False
    if qs.exists():
        product = qs.first()
    if product != None:
        can_order = product.can_order
        if can_order: # ()
            product_id = product.id
            request.session['product_id'] = product_id
        form = InventoryWaitlistForm(request.POST or None, product=product)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.product = product
            if request.user.is_authenticated: # ()
                obj.user = request.user
            obj.save()
            return redirect("/waitlist-success")
    context = {
        "object": product,
        "can_order": can_order,
        "form": form,
    }
    return render(request, "products/detail.html", context)



# Create your views here.
def search_view(request, *args, **kwargs): # /search/

    query = request.GET.get('q') # q
    qs = Product.objects.filter(title__icontains=query[0])
    print(query, qs)
    context = {"name": "abc", "query": query}
    return render(request, "home.html", context)


@staff_member_required
def product_create_view(request, *args, **kwargs):
    form = ProductModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():

        obj = form.save(commit=False)
        image = request.FILES.get('image')
        media = request.FILES.get('media')

        if image:
            obj.image = image
        if media:
            obj.media = media
        obj.user = request.user
        obj.save()

        form = ProductModelForm()
    return render(request, "forms.html", {"form": form}) # 200




def product_detail_view(request, pk):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404

    return render(request, "products/detail.html", {"object": obj})


def product_list_view(request, *args, **kwargs):
    qs = Product.objects.all()
    context = {"object_list": qs}
    return render(request, "products/list.html", context)


def product_api_detail_view(request, pk, *args, **kwargs):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found"}) # return JSON with HTTP status code of 404
    return JsonResponse({"id": obj.id})
