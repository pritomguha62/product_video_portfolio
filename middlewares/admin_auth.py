from django.shortcuts import redirect

def admin_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request, *args, **kwargs):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if not request.session.get('is_admin'):
            return redirect('admin_panel.signin')

        response = get_response(request, *args, **kwargs)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware

