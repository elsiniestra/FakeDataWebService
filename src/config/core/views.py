from django.http import HttpResponseRedirect
from django.shortcuts import redirect


def handler404(request, *args, **kwargs) -> HttpResponseRedirect:
    return redirect(to='home')
