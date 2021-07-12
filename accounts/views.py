from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from purbeurre.models import My_product_save, Name
from .forms import RegisterForm


@login_required
def my_account_views(request):
    """
    Access to personal space.
    :param request:
    :return: Direction personal space with the products saved.
    """
    user = request.user
    fav = Name.objects.filter(my_product_save__username=user.id)
    if fav:
        product = Name.objects.filter(pk__in=fav)
    else:
        product = []

    return render(request, "accounts/my_account.html", {'favorite': product})


@login_required
def my_product_views(request, product_id):
    """
    We save the products.
    :param request: User id.
    :param product_id: The product id we want to save.
    :return: Direction personal space.
    """
    try:
        My_product_save.objects.get(
            username_id=request.user.id, product_id=product_id)

        messages.warning(request,
                         'Ce produit est déjà dans vos favoris. '
                         'Allez à nouveau sur votre compte pour '
                         'voir vos produits sauvegarder.')

        return render(request, "accounts/my_account.html")

    except ObjectDoesNotExist:
        My_product_save.objects.create(
            username_id=request.user.id, product_id=product_id)

        messages.success(request, 'Le produit a bien été enregistré. '
                                  'Allez à nouveau sur votre compte pour voir '
                                  'vos produits sauvegarder.')

        return render(request, "accounts/my_account.html")


def registrer_views(request):
    """
    User registration.
    :param request:
    :return: Direction to main page or register.
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Votre compte a été crée avec succès.')
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})
