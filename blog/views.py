from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.http import JsonResponse
from django.template import RequestContext
from .models import Post, Contact, Comments, Specialization, Doctor, Reception
from django.utils import timezone
from .forms import ContactForm, CommentForm, ReceptionForm
from django.db.models.signals import post_save
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import auth
from django.dispatch import receiver
from django.views import generic




def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
	
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        user = auth.get_user(request)
     
        if comment_form.is_valid():
            comment = Comments()
            comment.author_id = auth.get_user(request)
            comment.email = comment_form.cleaned_data['email']
            comment.body = comment_form.cleaned_data['body']
            comment.post = post
            comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'blog/post_detail.html',
                 {'post': post,
                  'comments': comments,				 
                  'comment_form': comment_form})
				

def about(request):
    return render(request, 'blog/about.html')
    
def patient(request):
    return render(request, 'blog/patient.html')

def contactform(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		
		if form.is_valid():
			subject = form.cleaned_data['subject']
			sender = form.cleaned_data['sender']
			message = form.cleaned_data['message']
			copy = form.cleaned_data['copy']
			contact = Contact(subject=subject, sender=sender, message=message, copy=copy)
			contact.save()
			
			
			return render(request, 'blog/thanks.html')
	else:
		
		form = ContactForm()
	
	return render(request, 'blog/contact.html', {'form': form})

"""def reseptionform(request):
	if request.method == 'POST':
		reception_form = ReceptionForm(request.POST)
		
		if form.is_valid():
			subject = form.cleaned_data['subject']
			sender = form.cleaned_data['sender']
			message = form.cleaned_data['message']
			copy = form.cleaned_data['copy']
			contact = Contact(subject=subject, sender=sender, message=message, copy=copy)
			contact.save()
			
			
			return render(request, 'blog/thanks.html')
	else:
		
		form = ContactForm()
	
	return render(request, 'blog/contact.html', {'form': form})"""

class SpecializationList(ListView):
    model = Specialization
    template_name = 'blog/spec.html'
    context_object_name = 'specializations'

class DoctorList(ListView):
    model = Doctor
    template_name = 'blog/vrach.html'
    context_object_name = 'doctors'
    
def doctorsList(request, specialization):
    doctors = Doctor.objects.filter(specialization=specialization)
    return render(request, 'blog/vrach.html', {'doctors': doctors})

class AjaxDoctorView(generic.View):

    def ajax_get_doctor(self, request, *args, **kwargs):
        specialization = get_object_or_404(Specialization, pk=request.GET.get('specialization_id', ''))
        doctor_results = Doctor.objects.filter(k_value=specialization.k_value)
        return HttpResponse(serializers.serialize('json', doctor_results, fields=('id')), content_type='application/json')

class ReceptionView(FormView):
    form_class = ReceptionForm
    template_name = 'blog/reception.html'
    
    def get(self, request, *args, **kwargs):
        curr_specialization=Specialization.objects.get(id= self.kwargs['specialization'])
        curr_doctor=Doctor.objects.get(id= self.kwargs['doctor'])
        form = self.form_class(initial=self.initial)
        form.initial['specialization'] = self.kwargs['specialization']
        form.initial['doctor'] = self.kwargs['doctor']
        return render(request, self.template_name, {'form': form, "specialization":curr_specialization, "doctor":curr_doctor, })

    def post(self, request, *args, **kwargs):
        form = ReceptionForm(request.POST)
        if form.is_valid():
            return self.form_valid(form)

        curr_specialization=Specialization.objects.get(id= self.kwargs['specialization'])
        curr_doctor=Doctor.objects.get(id= self.kwargs['doctor'])
        return render(request, self.template_name, {'form': form, "specialization":curr_specialization, "doctor":curr_doctor, })

    def form_valid(self, form):
        fcd = form.cleaned_data
        curr_specialization=Specialization.objects.get(id= self.kwargs['specialization'])
        curr_doctor=Doctor.objects.get(id= self.kwargs['doctor'])
        response_dict={"form":form,
                       "specialization":curr_specialization,
                       "doctor":curr_doctor,
                       "isCreated": True,
                       "curr_date":fcd['date'],
                       "curr_time":fcd['time']}
        # условие для предотвращения записи на один и тот же день у данного врача
        if Reception.objects.filter(date=fcd['date'],time=fcd['time'],doctor=curr_doctor).count()==0:
            Reception.objects.create(date=fcd['date'],time=fcd['time'],
                                     patient_name=fcd['patient_name'],
                                     patient_info=fcd['patient_info'],
                                     doctor=curr_doctor,
                                     specialization=curr_specialization)
            return render_to_response('blog/reception.html',response_dict,
                                      context_instance=RequestContext(self.request))
        else:
            response_dict["isCreated"]=False
            response_dict["message"]="Вы уже зарегистрированы на это время"
            return render_to_response('blog/reception.html',response_dict,
                          context_instance=RequestContext(self.request))

    def get_context_data(self, **kwargs):
        context = super(ReceptionView, self).get_context_data(**kwargs)
        
        return context        


def date_from_ajax (request):
    if request.method == "POST" and request.is_ajax():
        doctor=Doctor.objects.get(id= request.POST.get("doctor_id"))
        reception_set=doctor.reception_set.filter(date=request.POST.get("date_from_ajax"))
        time_list=[]
        for reception in reception_set:
            time_list.append(reception.time)
        return JsonResponse({'time_list':time_list})


def thanks(reguest):
    thanks = 'thanks'
    return render(reguest, 'blog/thanks.html', {'thanks': thanks})
    
def specializationsSelectHandler(request):
   specialization = request.GET["specialization"]
   return HttpResponse(simplejson.dumps({"success" : "true" }, mimetype = "application/json"))
