from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
# Create your views here.

User = get_user_model()

class UserDetailView(DetailView):
    template_name = 'accounts/user_detail.html'
    queryset = User.objects.all()
    
    # slug_field='username'    
    # lookup_field = "username"
    # def get_slug_field(self):
        # return "username"
        # slug_url_kwarg='username' 
    
    def get_object(self):
        return get_object_or_404(User, username__iexact=self.kwargs.get("username"))