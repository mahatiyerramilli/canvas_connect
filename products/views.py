
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Product, Feedback
from .forms import FeedbackForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.product = product
            feedback.save()
    else:
        form = FeedbackForm()
    
    return render(request, 'products/detail.html', {
        'product': product,
        'form': form,
    })

def feedback_report(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')
    return render(request, 'products/feedback_report.html', {'feedbacks': feedbacks})
