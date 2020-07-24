from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpResponseRedirect
# from .forms import CategoryForm, SubCategoryForm, SubSubCategoryForm, AdForm
from . import models

# Create your views here.


class AdListView(ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'school_list'

    # Example of making your own:
    # context_object_name = 'schools'
    context_object_name = 'ad_list'
    model = models.Ad
    template_name = 'ads/ad_list.html'


class AdDetailView(DetailView):
    template_name = 'ads/ad_detail.html'
    context_object_name = 'ad_details'
    model = models.Ad


class AdCreateView(LoginRequiredMixin, CreateView):
    model = models.Ad
    # fields = ['category', 'ad_type', 'for_sale_by', 'ad_title', 'description', 'images',
    #          'youtube_video_link', 'website_url_link', 'city', 'price','price_options', 'phone_num',
    #          'email',]

    fields = '__all__'
    template_name = 'ads/ad_create.html'

    # before the form is submitted the authenticated user is assigned as the author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AdCreateView, self).form_valid(form)
"""

def ad_create_form_name(request):
    if request.method == 'POST':

        category_form = CategoryForm(request.POST)
        sub_category_form = SubCategoryForm(request.POST)
        sub_sub_category_form = SubSubCategoryForm(request.POST)
        ad_form = AdForm(request.POST)

        if category_form.is_valid() and sub_category_form.is_valid() and sub_sub_category_form.is_valid() and ad_form.is_valid():

            category_form.save()
            sub_category_form.save()
            sub_sub_category_form.save()
            ad_form.save()
            return HttpResponseRedirect('/success')

        else:
            context = {
                'category_form': category_form,
                'sub_category_form': sub_category_form,
                'sub_sub_category_form': sub_sub_category_form,
                'ad_form': ad_form,
            }

    else:
        context = {
            'category_form': CategoryForm(),
            'sub_category_form': SubCategoryForm(),
            'sub_sub_category_form': SubSubCategoryForm(),
            'ad_form': AdForm(),
        }

    return TemplateResponse(request, 'ads/ad_create.html', context)
"""


class AdUpdateView(UpdateView):
    model = models.Ad
    # fields = ['ad_type', 'for_sale_by', 'ad_title', 'description', 'images',
    #          'youtube_video_link', 'website_url_link', 'city', 'price', 'phone_num',
    #          'email',]
    fields = '__all__'
    template_name = 'ads/ad_update.html'

    success_url = reverse_lazy('list')


class AdDeleteView(DeleteView):
    model = models.Ad
    template_name = 'ads/ad_delete.html'
    context_object_name = 'ad_delete'
    success_url = reverse_lazy('user_ad')


# this is the ordinary search that a user will do on the ad list page
class AdSearchResultsView(ListView):
    """
    Display a Blog List page filtered by the search query.
    """
    model = models.Ad
    template_name = 'ads/ad_search_results.html'
    context_object_name = 'ad_search_results'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = models.Ad.objects.annotate(search=SearchVector('ad_title', 'description'),).filter(search=query)

        return object_list


# this is the user profile page that is loaded when the user
# clicks on my ads

@login_required # (login_url='/accounts/login/')
def userprofile(request):
    user = request.user
    user_ad = models.Ad.objects.filter(author=request.user).order_by('-created_date')
    template = 'ads/user_ad.html'

    return render(request, template, {'user_ad': user_ad, 'user': user})

# add a redirect url if user is not logged in
