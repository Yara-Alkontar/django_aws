from django.shortcuts import render
from.models import Order
from.serializers import OrderSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# from django.core.mail.backends.smtp import EmailBackend

from django.conf import settings
from django.core.mail import send_mail
from backend.settings import EMAIL_HOST_USER

# Create your views here.
class OrderView(APIView):
    def get(self,request):
        try:
            orders=Order.objects.all()
            serializer=OrderSerializer(orders,many=True)

            return Response({
                'data':serializer.data,
                'message':"Orders Data fetched Successfully",
            },status=status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return Response({
                 'data':{},
                 'message':"Something went wrong while fetching this data",
                
            },status=status.HTTP_400_BAD_REQUEST)
   

    def post(self, request):
        try:
            data = request.data
            serializer = OrderSerializer(data=data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': "Something went wrong",
                }, status=status.HTTP_400_BAD_REQUEST)
            
            subject = "New order is placed"
            message = "Dear Customer" + " " +data['customer_name'] + "Your order is placed now, thanks for your order."
            email = data['customer_email']
            recipient_list = [email]
            send_mail(subject, message, EMAIL_HOST_USER, recipient_list, fail_silently=True)
            
            serializer.save()
            
            return Response({
                'data': serializer.data,
                'message': "New Order is created",
            }, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            print(e)
            return Response({
                'data': {},
                'message': "Something went wrong in creation in order",
            }, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request):
        try:
            data = request.data
            order = Order.objects.filter(id=data.get('id'))

            if not order.exists():
                 return Response({
                 'data':{},
                 'message':"Order id not found with this id",
                
            },status=status.HTTP_404_NOT_FOUND)

            serializer=OrderSerializer(order[0],data=data,partial=True)

            if not serializer.is_valid():
                  return Response({
                    'data':serializer.errors,
                    'message':"Something went wrong",
                },status=status.HTTP_500_BAD_REQUEST)
            serializer.save()
            return Response({
                    'data':serializer.data,
                    'message':"Order is updated successfully ",
                },status=status.HTTP_200_OK)
        except:
            return Response({
                 'data':{},
                 'message':"Something went wrong in creation in order"
                
            },status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        try:
            data=request.data
            order=Order.objects.filter(id=data.get('id'))

            if not order.exists():
                 return Response({
                 'data':{},
                 'message':"Order id not found with this id",
                
            },status=status.HTTP_404_NOT_FOUND)

            order[0].delete()
            return Response({
                    'data':{},
                    'message':"Order is  Deleted ",
                },status=status.HTTP_200_OK)
        except:
            return Response({
                 'data':{},
                 'message':"Something went wrong in deleting in order",
                
            },status=status.HTTP_400_BAD_REQUEST)



        
    


