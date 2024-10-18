from django.shortcuts import redirect

def admin_login_redirect(request):
    return redirect('/login/')