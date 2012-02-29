# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django import forms
from django.contrib.auth.forms import UserCreationForm

#def index(request):
 #   return HttpResponse("user; login");

from django.contrib import auth

def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/portal/")
    else:
        # Show an error page
        return HttpResponseRedirect("/")

def register(request):
    #if request.user.is_authenticated():
        # They already have an account; don't let them register again
     #   return render_to_response('register.html', {'has_account': True})
   # manipulator = RegistrationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/portal/")
        else:
            form = UserCreationForm()
            return render_to_response("login/register.html", {'form': form,})
    else:
        return HttpResponseRedirect("/login/")

'''
new_data = request.POST.copy()
        errors = manipulator.get_validation_errors(new_data)
        if not errors:
            # Save the user                                                                                                                                                 
            manipulator.do_html2python(new_data)
            new_user = manipulator.save(new_data)
            
            # Build the activation key for their account                                                                                                                    
            salt = sha.new(str(random.random())).hexdigest()[:5]
            activation_key = sha.new(salt+new_user.username).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            
            # Create and save their profile                                                                                                                                 
            new_profile = UserProfile(user=new_user,
                                      activation_key=activation_key,
                                      key_expires=key_expires)
            new_profile.save()
            
            # Send an email with the confirmation link                                                                                                                      
            email_subject = 'Your new Cilantro account confirmation'
            email_body = "Hello, %s, and thanks for signing up for a Cilantro account!\n\nTo activate your account, click this link within 48 hours:\n\nhttp://example.com/accounts/confirm/%s" % (
                new_user.username,
                new_profile.activation_key)
            send_mail(email_subject,
                      email_body,
                      'registration@cilantro.bloat.org',
                      [new_user.email])
            
            return render_to_response('register.html', {'created': True})
    else:
        errors = new_data = {}
    form = forms.FormWrapper(manipulator, new_data, errors)
    return render_to_response('register.html', {'form': form})

def confirm(request, activation_key):
    if request.user.is_authenticated():
        return render_to_response('confirm.html', {'has_account': True})
    user_profile = get_object_or_404(UserProfile,
                                     activation_key=activation_key)
    if user_profile.key_expires < datetime.datetime.today():
        return render_to_response('confirm.html', {'expired': True})
    user_account = user_profile.user
    user_account.is_active = True
    user_account.save()
    return render_to_response('confirm.html', {'success': True}) 
'''
