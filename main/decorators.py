from functools import wraps

from django.shortcuts import redirect


def group_required(group_name):
    def _check_group(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            print(request.user)
            if request.user.is_anonymous:
                return redirect('main:home')
            if (not (request.user.groups.filter(name=group_name).exists())
                | request.user.is_superuser):
                return redirect('main:home')
            return view_func(request, *args, **kwargs)
        return wrapper
    return _check_group