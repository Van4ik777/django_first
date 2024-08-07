import json
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .forms import RegisterUserForm
from .utils import DataMixin
from django.contrib.auth import logout
from .forms import ReviewForm
from django.shortcuts import redirect, get_object_or_404
from .models import Review

cart_items = []


def football(request):
    return render(request, 'main/football.html')


def add_like(request, review_id):
    if request.method == 'POST' and request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_id)

        if request.user in review.likes.all():
            review.likes.remove(request.user)
        else:
            review.likes.add(request.user)
        return redirect('pizza_1')
    else:
        return redirect('pizza_1')


def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        review.delete()
    return redirect('pizza_1')


def add_review_1(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        print(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            reply_to_id = request.POST.get('reply_to')
            if reply_to_id:
                parent_review = get_object_or_404(Review, pk=reply_to_id)
                review.reply_to = parent_review
            review.save()
            return redirect('pizza_1')
    else:
        return redirect('pizza_1')


    return redirect('pizza_1')


def profile(request):
    return render(request, 'main/profile.html')


def logout_user(request):
    logout(request)
    return redirect('main')


def register(request):
    return render(request, 'main/register.html')


@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        pizza_name = data.get('pizza_name')
        quantity = data.get('quantity', 1)  # Default quantity is 1 if not provided
        price = data.get('price')

        # Check if the pizza is already in the cart
        for item in cart_items:
            if item['pizza_name'] == pizza_name:
                item['quantity'] += quantity
                break
        else:  # If pizza is not in the cart, add it as a new item
            cart_item = {'pizza_name': pizza_name, 'quantity': quantity, 'price': price}
            cart_items.append(cart_item)

        print('Cart Items:', cart_items)

        total_price = sum(item['price'] * item['quantity'] for item in cart_items)  # Calculate total price
        return JsonResponse({'message': 'Товар успешно добавлен в корзину.', 'total_price': total_price})
    else:
        return JsonResponse({'message': 'Метод запроса не поддерживается.'}, status=405)


@csrf_exempt
def update_quantity(request):
    global cart_items

    if request.method == 'POST':
        data = json.loads(request.body)
        pizza_name = data.get('pizza_name')
        quantity = data.get('quantity', 0)

        for item in cart_items:
            if item['pizza_name'] == pizza_name:
                item['quantity'] = quantity
                item['total_price'] = item['price'] * quantity
                if item['quantity'] == 0:
                    cart_items.remove(item)
                break

        else:
            return JsonResponse({'message': 'Pizza not found in cart.'}, status=404)

        # Recalculate total price for the cart
        total_price = sum(item['total_price'] for item in cart_items)

        # Return updated cart data as JSON response
        return JsonResponse({'cart': cart_items, 'total_price': total_price})
    else:
        return JsonResponse({'message': 'Метод запроса не поддерживается.'}, status=405)


def clear_cart(request):
    global cart_items
    cart_items = []
    return render(request, 'main/cart.html')


def cart(request):
    total_price = sum(item['price'] * item['quantity'] for item in cart_items)
    return render(request, 'main/cart.html', {"cart": cart_items, "total_price": total_price})


def main(request):
    return render(request, 'main/main.html')


def pizza_1(request):
    reviews = Review.objects.all()
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.stars = request.stars
            review.save()
            return redirect('pizza_1')
        else:
            print("gg")

    return render(request, 'main/pizza_1.html', {'form': form, 'reviews': reviews})


def pizza_2(request):
    return render(request, 'main/pizza_2.html')


def pizza_3(request):
    return render(request, 'main/pizza_3.html')



class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = "main/register.html"
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        user = User.objects.get(username=username)
        auth_login(self.request, user)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Register")
        return dict(list(context.items()) + list(c_def.items()))


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('main')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})







