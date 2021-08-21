from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import datetime
from django.utils.timezone import utc

# Create your views here.
results = [
      {'name': 'Fatima Lopez', 'email': 'f.lopez@email.com', 'submission_time': 'Dec. 31, 1999, 11:59 p.m.'},
      {'name': 'Gary Johnston', 'email': 'g.johnston@email.com', 'submission_time': 'Dec. 31, 1999, 11:59 p.m.'}
    ]

def index(request):
  if request.POST:
    context = {
      'name': request.POST['name'],
      'email': request.POST['email'],
    }
    if context['name'] == '' or context['email'] == '':
        return HttpResponseBadRequest('<meta name="viewport" content="width=device-width, initial-scale=1"><h1>Name or email field is empty. Please try again.</h1>')
    try:
      validate_email(context['email'])
    except ValidationError as error:
        return HttpResponseBadRequest('<meta name="viewport" content="width=device-width, initial-scale=1"><h1>Invalid email. Please try again.</h1>')
    else:
      results.append({'name': request.POST['name'], 'email': request.POST['email'], 'submission_time': datetime.datetime.now().replace(tzinfo=utc)})
      return render(request, 'thanks.html', context)
  context = {
    'results': results
  }
  return render(request, 'index.html', context)