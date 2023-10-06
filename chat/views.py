from django.shortcuts import render,redirect
from .models import Customers,UserProfile,Message
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from chat.serializers import MessageSeriallizer
from django.contrib.auth import logout

# Create your views here.

def getcustomerlist(id):
    try:
        user=UserProfile.objects.get(id=id)
        customerlist=list(user.customers_set.all())
        customers =[]
        for customerid in customerlist:
            num =str(customerid)
            data= UserProfile.objects.get(id=int(num))
            customers.append(data)
        return customers
    except:
        return []

def getuserid(username):
    """
    get user id by using username
    Arg:username
    return:int
    """
    UserPro=UserProfile.objects.get(username=username)
    result =UserPro.id
    return result

def chat(request,username):
    """
    Get the chat between two users.
    :param request:
    :param username:
    :return:
    """
    friend = UserProfile.objects.get(username=username)
    id = getuserid(request.user.username)
    curr_user = UserProfile.objects.get(id=id)
    messages = Message.objects.filter(user_name=id, staff_name=friend.id) | Message.objects.filter(user_name=friend.id, staff_name=id)
    result = messages.order_by("time_taken")
    users = list(UserProfile.objects.all())
    print(messages)

    for user in users:
        if user.username == request.user.username:
            users.remove(user)
            break
    try:
        users = users[:10]
    except:
        users = users[:]
    if request.method == "GET":
        friends = getcustomerlist(id)
        return render(request, "chat/base.html",
                      {'messages': result,
                       'customers': friends,
                       'curr_user': curr_user, 'reciever': friend,'users':users})

def index(request):
    """
    check if the user is authenticated
    for safetety reason
    """
    if not request.user.is_authenticated:
        print('not yet login')
        return render(request,'chat/login.html')
    else:
        username=request.user.username
        id = getuserid(username)
        customerresult = getcustomerlist(id)
        users = list(UserProfile.objects.all())
        for user in users:
            if user.username == request.user.username:
                users.remove(user)
                break
        try:
         users = users[:10]
        except:
         users = users[:]
        print(customerresult)

        return render(request,'chat/base.html',{'customers':customerresult,'users':users})

def addcustomer(request, name):
    """
    Add a user to the customers list
    :param request:
    :param name:
    :return: route
    """

    username = request.user.username
    id = getuserid(username)
    customer = UserProfile.objects.get(username=name)
    curr_user = UserProfile.objects.get(id=id)
    print(curr_user.name)
    ls = curr_user.customers_set.all()
    flag = 0
    for username in ls:
        if username.customer == customer.id:
            flag = 1
            break
    if flag == 0:
        print("Friend Added!!")
        curr_user.customers_set.create(customer=customer.id)
        customer.customers_set.create(customer=id)
    return redirect("/chat")

@csrf_exempt
def message_list(request, sender=None, receiver=None):
    if request.method == 'GET':
        messages = Message.objects.filter(user_name=sender, staff_name=receiver, seen=False)
        serializer = MessageSeriallizer(messages, many=True, context={'request': request})
        for message in messages:
            message.seen = True
            message.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = MessageSeriallizer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
