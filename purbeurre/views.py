from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from purbeurre.models import Name


def home(request):
    """
    Show home page.
    """

    return render(request, "index.html")


def ml(request):
    """
    Display the 'legal notices' page.
    """

    return render(request, "mentions_legales.html")


def search(request):
    """
    The user is looking for a product.
    I'm trying to find it in the database.
    I search for substitutes in the same
    categories and post them on the page.
    """

    search = request.GET.get('search_user')
    search_user = search.capitalize()

    try:
        product = Name.objects.filter(name_product=search_user).first()
        substitutes = Name.objects.filter(
            category=product.category,
            nutrition_grade__lt=product.nutrition_grade).\
            order_by("nutrition_grade")

        paginator = Paginator(substitutes, 6)
        page = request.GET.get('page')
        alt_products = paginator.get_page(page)

        context = {
            'alt_products': alt_products,
            'paginate': True,
            'title': search_user,
            'image': product.picture_product,
            'nutri': product.nutrition_grade,
        }

    except AttributeError:
        messages.warning(request,
                         "Ce produit est introuvable. "
                         "Vérifiez l'orthographe de la "
                         "recherche.")
        return redirect('home')

    return render(request, 'search.html', context)


def detail(request, substitut_detail):
    """
    The user chooses to learn more
    about the surrogate. I show him the
    different information.
    """

    product_detail = Name.objects.get(id=substitut_detail)

    context_detail = {
        'title_page': 'Informations supplémentaires',
        'title': product_detail.name_product,
        'nutri': product_detail.nutrition_grade,
        'image': product_detail.picture_product,
        'image_nutri': product_detail.picture_nutrition,
        'url': product_detail.url_product,
    }

    return render(request, 'detail.html', context_detail)
