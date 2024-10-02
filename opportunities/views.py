from django.shortcuts import render, redirect
from .forms import OpportunityForm
from django.contrib.auth.decorators import login_required
from .models import Opportunity
from django.shortcuts import get_object_or_404
from .models import Application
from django.http import HttpResponse
from .models import Donation
from .models import Organization, Donation
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages




def search_organizations(request):
    user_profile=request.user.userprofile
    query = request.GET.get('q')
    organizations = Organization.objects.filter(name__icontains=query) | Organization.objects.filter(description__icontains=query)| Organization.objects.filter(location__icontains=query)  # Case-insensitive search
    amounts = [10, 20, 25, 40, 50, 75, 100, 150, 200] 

    return render(request, 'opportunities/search_results.html', {'user_profile':user_profile, 'organizations': organizations,'amounts':amounts, 'query': query})


@login_required
def donate(request, organization_id=None):
    user_profile=request.user.userprofile
    if organization_id:
        # Specific organization donation
        organization = get_object_or_404(Organization, pk=organization_id)
        if request.method == 'POST':
            amount = request.POST.get('amount')
            privacy = request.POST.get('privacy')

            # Process the donation
            Donation.objects.create(
                organization=organization,
                amount=amount,
                privacy=privacy,
                user=request.user.userprofile
            )

            return redirect('donate', organization_id=organization_id)

        return render(request, 'opportunities/search_results.html', {'organization': organization, 'user_profile':user_profile})
    else:
        # General donation page with search
        organizations = Organization.objects.all()  # Fetch all organizations for display
        return render(request, 'opportunities/donate.html', {'organizations': organizations})



def donation_success(request):
    # Render the donation success page
    return render(request, 'donation_success.html', {
        'message': "Thank you for your donation!"
    })

def process_donation(request):
    if request.method == 'POST':
        # Get the amount and privacy option from the form
        amount = request.POST.get('amount')
        privacy = request.POST.get('privacy')
        
        # Validate that the amount is present and valid
        if not amount or float(amount) <= 0:
            return HttpResponse("Please enter a valid amount.", status=400)

        # Create the Donation record in the database
        donation = Donation.objects.create(
            amount=amount,
            privacy=privacy,
            # Add more fields here if needed (e.g., user information)
        )
        
        # Redirect to the success page after successful donation
        return redirect('donation_success')

    # If it's not a POST request, return an error response
    return HttpResponse("Invalid request.", status=405)




@login_required
def urgent_cause(request):
    user_profile=request.user.userprofile
    opportunities = Opportunity.objects.all()
    context={
        'opportunities':opportunities,
        'user_profile':user_profile
        }
    return render(request, 'opportunities/urgent_cause.html', context)



@login_required

def create_opportunity(request):
    user_profile=request.user.userprofile
    """View to handle the form submission for opportunity creation."""
    if request.method == 'POST':
        form = OpportunityForm(request.POST)
        if form.is_valid():
            opportunity = form.save(commit=False)
            
            # Check if the user has an associated organization
            if request.user.userprofile.organization is not None:
                opportunity.organization = request.user.userprofile.organization
                opportunity.save()
                return redirect('opportunity:opportunity_list')
            else:
                messages.error(request, "You need to have an organization set up to create an opportunity.")
                return redirect('opportunity:create_opportunity')  # Redirect to profile setup page or relevant page
    else:
        form = OpportunityForm()
    return render(request, 'opportunities/create_opportunity.html', {'form': form, 'user_profile':user_profile})


@login_required
def opportunity_list(request):
    user_profile=request.user.userprofile
    """Add a simple search filter to the list view to filter by location or title"""
    query = request.GET.get('q', '')
    if query:
        opportunities = Opportunity.objects.filter(title__icontains=query) | Opportunity.objects.filter(location__icontains=query)| Opportunity.objects.filter(description__icontains=query)
    else:
        opportunities = Opportunity.objects.all()
    return render(request, 'opportunities/opportunity_list.html', {'opportunities': opportunities,'user_profile':user_profile, 'query': query})


@login_required
def opportunity_detail(request, pk):
    user_profile=request.user.userprofile

    """Allow users to view detailed information about the opportunity and apply for it."""
    opportunity = get_object_or_404(Opportunity, pk=pk)
    return render(request, 'opportunities/opportunity_detail.html', {'opportunity': opportunity, 'user_profile':user_profile})



@login_required
def apply_for_opportunity(request, pk):
    """Add an application button that allows volunteers to apply for the opportunity."""
    opportunity = get_object_or_404(Opportunity, pk=pk)
    application, created = Application.objects.get_or_create(user_profile=request.user.userprofile, opportunity=opportunity)
    if created:
        application.status = 'PEN'
        application.save()
    return redirect('opportunity:opportunity_detail', pk=pk)

