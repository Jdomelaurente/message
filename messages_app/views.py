from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Message 

def message_list(request):
    messages = Message.objects.all().order_by('-created_at')  # newest first
    return render(request, 'message_list.html', {'messages': messages})

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MessageForm()
    return render(request, 'send_message.html', {'form': form})

def success(request):
    return render(request, 'success.html')
