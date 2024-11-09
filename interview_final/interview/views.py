from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import InterviewRound  # Add this import
from .forms import InterviewRoundForm, EmailForm
from .utils import send_round_assignment_email

class InterviewRoundListView(ListView):
    model = InterviewRound
    template_name = 'interview/round_list.html'
    context_object_name = 'rounds'

class InterviewRoundCreateView(CreateView):
    model = InterviewRound
    form_class = InterviewRoundForm
    template_name = 'interview/round_create.html'
    success_url = reverse_lazy('interview:round-list')
    
    def form_valid(self, form):
        form.instance.round_number = InterviewRound.objects.count() + 1
        messages.success(self.request, 'Interview round created successfully!')
        return super().form_valid(form)

def send_email_view(request, round_id):
    round_obj = get_object_or_404(InterviewRound, id=round_id)
    
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            success = send_round_assignment_email(
                email,
                round_obj.get_round_type_display(),
                round_obj.round_number
            )
            
            if success:
                messages.success(request, 'Email sent successfully!')
                return redirect('interview:round-list')
            else:
                messages.error(request, 'Failed to send email.')
    else:
        form = EmailForm()
    
    return render(request, 'interview/send_email.html', {
        'form': form,
        'round': round_obj
    })
