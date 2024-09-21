from django.urls import path
from .views import create_opportunity, opportunity_detail, apply_for_opportunity, opportunity_list, donate, urgent_cause, process_donation, donation_success, search_organizations

urlpatterns = [
  path('create/',create_opportunity, name="create_opportunity" ),
  path('detail/<int:pk>/',opportunity_detail, name="opportunity_detail" ),
  path('apply/<int:pk>',apply_for_opportunity, name="apply_for_opportunity" ),
  path('list/',opportunity_list, name="opportunity_list" ),
  path('donate/<int:organization_id>/',donate, name="donate" ),
  path('urgent/',urgent_cause, name="urgent_cause" ),
  path('process-donation/', process_donation, name='process_donation'),
  path('donation-success/', donation_success, name='donation_success'),
  path('search/', search_organizations, name='search_organizations'),
]