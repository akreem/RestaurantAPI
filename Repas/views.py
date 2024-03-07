from django.shortcuts import get_object_or_404,render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .filtters import RepasFilter
from rest_framework import status
from .models import Repas, Review
from .serializers import RepasSerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Avg
# Create your views here.
@api_view(['GET'])
def get_all_repass(request):
   
   filterset = RepasFilter(request.GET,queryset=Repas.objects.all().order_by('id'))
   count = filterset.qs.count()
   resPage = 12
   paginator = PageNumberPagination()
   paginator.page_size = resPage
   
   queryset =  paginator.paginate_queryset(filterset.qs, request)
   serializer = RepasSerializer(queryset,many=True)
   return Response({"repass":serializer.data, "per page":resPage, "count":count})

@api_view(['GET'])
def get_by_id_repas(request,pk):
    repass = get_object_or_404(Repas,id=pk)
    serializer = RepasSerializer(repass,many=False)
    print(repass)
    return Response({"repas":serializer.data})


@api_view(['POST'])
@permission_classes([IsAuthenticated,IsAdminUser])
def new_repas(request):
    data = request.data
    serializer = RepasSerializer(data = data)

    if serializer.is_valid():
       repas = Repas.objects.create(**data,user=request.user)
       res = RepasSerializer(repas,many=False)
 
       return Response({"repas":res.data})
    else:
        return Response(serializer.errors)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated,IsAdminUser])
def update_repas(request,pk):
    repas = get_object_or_404(Repas,id=pk)

    if repas.user != request.user:
        return Response({"error":"Sorry you can not update this product"}
                        , status=status.HTTP_403_FORBIDDEN)
    
    repas.name = request.data['name']
    repas.description = request.data['description']
    repas.price = request.data['price']
    repas.category = request.data['category']
    repas.ratings = request.data['ratings']
    repas.stock = request.data['stock']

    repas.save()
    serializer = RepasSerializer(repas,many=False)
    return Response({"repas":serializer.data})
        

@api_view(['DELETE'])
@permission_classes([IsAuthenticated,IsAdminUser])
def delete_repas(request,pk):
    repas = get_object_or_404(Repas,id=pk)

    if repas.user != request.user:
        return Response({"error":"Sorry you can not update this product"}
                        , status=status.HTTP_403_FORBIDDEN)
     

    repas.delete() 
    return Response({"details":"Delete action is done"},status=status.HTTP_200_OK)







@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request,pk):
    user = request.user
    repas = get_object_or_404(Repas,id=pk)
    data = request.data
    review = repas.reviews.filter(user=user)
   
    if data['rating'] <= 0 or data['rating'] > 10:
        return Response({"error":'Please select between 1 to 5 only'}
                        ,status=status.HTTP_400_BAD_REQUEST) 
    elif review.exists():
        new_review = {'rating':data['rating'], 'comment':data['comment'] }
        review.update(**new_review)

        rating = repas.reviews.aggregate(avg_ratings = Avg('rating'))
        repas.ratings = rating['avg_ratings']
        repas.save()

        return Response({'details':'Repas review updated'})
    else:
        Review.objects.create(
            user=user,
            repas=repas,
            rating= data['rating'],
            comment= data['comment']
        )
        rating = repas.reviews.aggregate(avg_ratings = Avg('rating'))
        repas.ratings = rating['avg_ratings']
        repas.save()
        return Response({'details':'Repas review created'})
    


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_review(request,pk):
    user = request.user
    repas = get_object_or_404(repas,id=pk)
   
    review = repas.reviews.filter(user=user)
   
 
    if review.exists():
        review.delete()
        rating = repas.reviews.aggregate(avg_ratings = Avg('rating'))
        if rating['avg_ratings'] is None:
            rating['avg_ratings'] = 0
            repas.ratings = rating['avg_ratings']
            repas.save()
            return Response({'details':'Repas review deleted'})
    else:
        return Response({'error':'Review not found'},status=status.HTTP_404_NOT_FOUND)






