from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Review
from .serializers import CategoryListSerializer, CategoryDetailSerializer, ProductListSerializer, ProductDetailSerializer, ReviewListSerializer, ReviewDetailSerializer, ReviewSerializer, ProductReviewSerializer, CategorySerializer
from django.db.models import Avg, Count
# Create your views here.

# HW 1
@api_view(http_method_names=['GET'])
def category_list_api_view(request):
    categories = Category.objects.all()
    list_ = CategoryListSerializer(categories, many=True).data
    return Response(
        data=list_
    )

@api_view(http_method_names=['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = CategoryDetailSerializer(category, many=False).data
    return Response(data=data)

@api_view(http_method_names=['GET'])
def product_list_api_view(request):
    products = Product.objects.all()
    list_ = ProductListSerializer(products, many=True).data
    return Response(
        data=list_
    )

@api_view(http_method_names=['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = ProductDetailSerializer(product, many=False).data
    return Response(data=data)

@api_view(http_method_names=['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    list_ = ReviewListSerializer(reviews, many=True).data
    return Response(
        data=list_
    )

@api_view(http_method_names=['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = ReviewDetailSerializer(review, many=False).data
    return Response(data=data)



# HW 2

@api_view(http_method_names=['GET'])
def product_review_list_api_view(request):
    products = (Product.objects.annotate(rating=Avg('reviews__stars')).prefetch_related('reviews'))
    list_ = ProductReviewSerializer(products, many=True)

    return Response(
        list_.data
    )

@api_view(http_method_names=['GET'])
def category_list_count_api_view(request):
    categories = Category.objects.annotate(product_count=Count('products'))
    list_ = CategorySerializer(categories, many=True)
    return Response(
        list_.data
    )