from django.shortcuts import render,redirect
from django.http import Http404
from .models import Code,Category
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q
from .forms import CreateCodeForm,UpdateCodeForm
from django.contrib import messages

# Create your views here.
def codes_list(request):
    code_list = Code.objects.filter(is_active=True).order_by('?')
    paginator = Paginator(code_list,18)
    page_number = request.GET.get('page',1)
    try:
        codes = paginator.page(page_number)
    except EmptyPage:
        codes = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        codes = paginator.page(1)
    return render(request,'codes/home.html',{'codes':codes})
    

def code_detail(request,code_slug):
    try:
        code = Code.objects.get(slug=code_slug,is_active=True)
    except Code.DoesNotExist:
        raise Http404
    return render(request,'codes/code-detail.html',{'code':code})

def codes_per_category(request,category_name):
    category = Category.objects.get(name__iexact = category_name)
    codes = Code.objects.filter(category=category,is_active=True)
    return render(request,'codes/codes-per-category.html',{'codes':codes,'category':category})

def search_code(request):
    query = request.GET.get('q')
    codes = Code.objects.all()

    if query:
        codes = codes.filter(
            Q(name__icontains= query) |
            Q(description__icontains = query)
        )

    return render(request,'codes/results.html',{'codes':codes,'query':query})

def create_code(request):
    code = None
    if request.method == 'POST':
        form = CreateCodeForm(request.POST)
        if form.is_valid():
            code = form.save(commit=False)
            code.author = request.user
            code.save()
            messages.success(request,'Code added successfully...')
            return redirect('codes:codes-list')
        else:
            messages.warning(request,'Oops, something went wrong. Please try again!')
            return redirect('codes:create-code')
    else:
        form = CreateCodeForm()
        return render(request,'codes/create-code.html',{'form':form})
    
def update_code(request,code_pk):
    code = Code.objects.get(pk = code_pk)
    if request.method == 'POST':
        form = UpdateCodeForm(request.POST,instance=code)
        if form.is_valid():
            form.save()
            return redirect('codes:codes-list')
        else:
            messages.warning(request,'Oops, something went wrong. Please try again!')
            return redirect('codes:update-code')
    else:
        form = UpdateCodeForm(instance=code)
        return render(request,'codes/update-code.html',{'form':form})
    
def faqs(request):
    return render(request,'faqs.html')
        






