from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from .models import User,Blog
from .forms import NewBlog
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.shortcuts import redirect
from django.core.paginator import Paginator

def home(request):
    return render(request, 'index.html')

def register(request):
    User = get_user_model()

    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        re_password = request.POST.get('re-password',None)
        useremail = request.POST.get('useremail',None)
        userschool = request.POST.get('userschool',None)
        res_data = {}
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다..'
            return render(request, 'register.html', res_data)

        elif not (username and password and re_password and userschool):
            res_data['error'] = '모든값을 입력해 주세요.'
            return render(request, 'register.html', res_data)
        
        else:
            user = User.objects.create_user(username = username, password =password, useremail = useremail,userschool=userschool)
            auth.login(request, user)
            return redirect('logined')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('logined')
        else:
            return render(request,'login.html',{'error':'아이디나 패스워드를 확인하십시오.'})
    else:
        return render(request,'login.html')

def logined(request):
    return render(request,'index_logined.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
    return render(request,'index.html')

# 여기서부터 CRUD 들어감

def read(request):
    blogs = Blog.objects
    #블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list,3)
    #request된 페이지가 뭔지를 알아내고 ( request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)
    
    return render(request, 'funccrud.html', {'blogs':blogs, 'posts':posts})

def create(request):
        # 새로운 데이터 새로운 블로그 글 저장하는 역할 == POST
    if request.method == 'POST':
        form = NewBlog(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('home')
        else:
            return render(request, 'new.html', {'form':form})
    #입력된 블로그 글들을 저장해라         
    # 글쓰기 페이지를 띄워주는 역할 == GET
    else:
        #단순히 입력받을 수 있는 form을 띄어줘라
        form = NewBlog()
        return render(request, 'new.html', {'form':form})

def update(request, pk):
    blog = get_object_or_404(Blog,pk = pk)
    form = NewBlog(request.POST,instance=blog)

    if form.is_valid():
        form.save()
        return redirect('home')
    
    return render(request,'new.html',{'form' : form})
    
def delete(request, pk):
    blog = get_object_or_404(Blog,pk = pk)
    blog.delete()
    return redirect('home')

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'details':details})