

import datetime
import logging
import traceback

from book1.models import Book1
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from book1.forms import Book1Form, StudentForm, AddressForm

logger = logging.getLogger("book")

# Create your views here.
@csrf_exempt
def homepage(request):
    ''' display book form to add  book details'''
    logger.info("Homepage accessed")
    # print(request.method)
    # print(request.POST, type(request.POST))
    name = request.POST.get("bname")                # fetching data from frontend
    price = request.POST.get("bprice")
    qnty = request.POST.get("bqnty")
    if request.method == "POST":
        if not request.POST.get("bid"):         # if id request method is not returning id then create a new id and add details
            Book_Name = name
            Book_Price = price
            Book_qnty = qnty
            Book1.objects.create(name = Book_Name,price = Book_Price, qnty = Book_qnty) 
            return redirect("homepage")
        
        else:                                   # if request method is returning id then update the details
            bid = request.POST.get("bid")
            try:
                book_obj = Book1.objects.get(id = bid)
            except Exception as msg:
                logger.error(msg)
            book_obj.name = name
            book_obj.price = price
            book_obj.qnty = qnty
            book_obj.save()
            return redirect("show_all_books")

    elif request.method == "GET":
        return render(request, "home.html")
    
def show_all_books(request):
    '''display all books  '''
    logger.info(request.POST)
    active_books = Book1.active_objects.all()           # fetch data of all books 
    logger.info(f"all_books:- {active_books}  show books accessed")
    return render(request, "show_books.html", {"books": active_books})     # pass it to html page

def show_inactive_books(request):
    inactive_books = Book1.Inactive_objects.all()
    logger.info(f"Soft deleted books:- {inactive_books} show soft deleted books accessed at {datetime.datetime.now()} Hours")
    return render(request, "deleted_books.html", {"books": inactive_books})

def edit_data(request, id):
    ''' Edit the book name, price, quantity from id'''
    book = Book1.objects.get(id = id)                      # fetch data of book whose id is present
    logger.info(f"Edited book:- {book}")
    return render(request, template_name='home.html', context={"single_book": book})  # pass it to html page

def delete_data(request,id):
    '''delete a book details from id'''
    print(request.method)
    if request.method == "POST":
        try:
            book = Book1.objects.get(id = id)
        except Book1.DoesNotExist as err_msg:
            traceback.print_exc()            # print detailed exception message
            return HttpResponse(f"Book does not exists for id:- {id}")
        else:
            book.delete()
            return redirect("show_all_books")
    else:
        return HttpResponse(f"Request method {request.method} not allowed. Only post method allowed")

@csrf_exempt
def delete_all_data(request):
    '''Delete all books'''
    print(request.method)
    all_books = Book1.objects.all()
    logger.warning("all books deleted")
    all_books.delete()
    return redirect("show_all_books")

def soft_delete(request, id):
    '''soft delete-only make status as inactive'''
    book = Book1.objects.get(id=id)
    logger.warning(f"{book} is made inacive")
    book.is_active = 'N'
    book.save()
    return redirect("show_all_books")

def soft_delete_all(request):
    '''make all books inactive'''
    all_book = Book1.objects.all()
    logger.warning(f"Book data:- {all_book} status made inactive")
    for book in all_book:
        book.is_active = 'N'
        book.save()
    return redirect("show_all_books")

def recover_books(request, id):
    '''recover soft deleted books'''
    book = Book1.objects.get(id=id)
    logger.info(f"Book Name:- {book} restored")
    book.is_active = 'Y'
    book.save()
    return redirect("show_all_books")

def form_home(request):                 # django form
    context = {'form': StudentForm()}
    return render(request, 'form.html', context)

def book_data(request):                 # django model form
    if request.method == 'POST':
        form = Book1Form(request.POST)
        if form.is_valid():
            try:
                return redirect('book_data')
            except:
                pass
    else:
        form = Book1Form()
        return render(request,'book_form.html', {'form':form})

def address_form(request):                 # django form
    context = {'form': AddressForm()}
    return render(request, 'add_form.html', context)

from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    user_list = list(User.objects.all())
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 5)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {'users': users}
    # sending the page object to index.html
    return render(request, 'index.html', context)
