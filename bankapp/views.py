from django.shortcuts import get_object_or_404, render
from .models import District, Branches, AccountType, Userdetails, Materials
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.http import JsonResponse
# from .forms import RegistrationForm
# Create your views here.
def home(request):
    district_name = District.objects.all()
    return render(request, 'index.html', locals())

def details(request,distname):
    district_name = District.objects.all()
    dist_id = District.objects.filter(dist_name=distname)
    for i in dist_id:
        branch = Branches.objects.all().filter(district_name=i.id)

    return render(request, 'details.html', locals())

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        # email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already Taken')
                return render('register')
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request, 'Email Id already Taken')
            #     return render('register')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
        
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('newpage')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
        
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def newpage(request):
    district_name = District.objects.all()

    return render(request,'newpage.html', locals())


    
def form(request):
    district_name = District.objects.all()
    acctype = AccountType.objects.all()
    materials= Materials.objects.all()
    # form = RegistrationForm()
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        address = request.POST['address']
        district = request.POST['district']
        branch = request.POST['branch']
        account_type = request.POST['account_type']
        material = request.POST.getlist('materials[]')
        print(material)
        # print(account_type)
        # print(district)
        # print(branch)
        # districtname = District.objects.filter(id=district).values('dist_name').first()
        # branchname = Branches.objects.filter(id=branch).values('branch_name').first()
        # x = districtname['dist_name']
        # print(x)
        # y = branchname['branch_name']
        # print(y)
        district_instance = get_object_or_404(District, id=district)
        branch_instance = get_object_or_404(Branches, id=branch)
        account_instance = get_object_or_404(AccountType, id=account_type)
        # material_instance = get_object_or_404(Materials, id=)
        user = Userdetails(name=name, dob=dob, age=age, gender=gender, phone_number=phone_number, email=email,
                           address=address, district=district_instance, branch=branch_instance, 
                           account_type=account_instance, materials=material)
        user.save()
        return redirect('confirmationpage')

    return render(request, 'form.html', locals())

def get_topics_ajax(request):
    if request.method == "GET":
        district_id = request.GET.get('district_id')  # Use get() to handle missing key gracefully
        data = {}  # Initialize data as a dictionary

        try:
            district = District.objects.filter(id=district_id).first()
            branch = Branches.objects.filter(district_name=district)
        except Exception:
            data['error_message'] = 'error'
            return JsonResponse(data)

        return JsonResponse(list(branch.values('id', 'branch_name')), safe=False)
    
def confirmationpage(request):
    return render(request, 'confirmationpage.html')
# def formdist(request):
   
#     form = RegistrationForm()
       
#     return render(request, 'form.html', locals())

# def my_def_in_view(request):
#     result = request.GET.get('distname', None)
#     print(result)
#     # Any process that you want
#     data = {
#             # Data that you want to send to javascript function
#     }
#     return JsonResponse(data)

# def my_def_in_view(request):
    
    
#     result = request.GET.get('result')
#     print(result)
#     formdist_id = District.objects.filter(dist_name=result)
    
#     for i in formdist_id:
        
#         formbranch = Branches.objects.all().filter(district_name=i.id)
#         print(formbranch)
        
        
        
#     # Any process that you want
    
#     data = {
#             # Data that you want to send to javascript function
            
#     }

#     return JsonResponse(data)

