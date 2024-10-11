from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from opportunities.models import Organization
from .forms import OrganizationForm
from django.contrib import messages
from .models import OrganizationFollow

# def manage_organization(request):
#     user_profile=request.user.userprofile
#     """List all suggested organizations along with organizations created by the user and followed organizations"""
#     organizations = Organization.objects.all()
#     """Get organizations created by the user"""
#     user_created_organizations = Organization.objects.filter(user_profile=request.user.userprofile)
#     """Get followed organizations by the current user using the property defined in UserProfile"""
#     followed_organizations = request.user.userprofile.followed_organizations

#     """View to handle organization creation for the logged-in user."""
#     if request.method == 'POST':
#         form = OrganizationForm(request.POST)
#         if form.is_valid():
#             organization = form.save(commit=False)
#             organization.user_profile = request.user.userprofile  # Associate with the user's profile
#             organization.save()
#             messages.success(request, "Organization created successfully!")
#             return redirect('dashboard:manage_organization')  # Redirect to the organization list page or another page
#     else:
#         form = OrganizationForm()

#     """Prepare the context data"""
#     context = {
#         'organizations': list(organizations.values()),  """Convert queryset to list of dicts"""
#         'followed_organizations': list(followed_organizations.values()),  """Convert followed organizations to list of dicts"""
#         """Convert user-created organizations to list of dicts"""
#         'user_created_organizations': list(user_created_organizations.values()),
#         'form':form,
#         'user_profile':user_profile
#         }
#     return render(request, 'dashboard/manage_organization.html', context)

@login_required
def manage_organization(request):
    user_profile = request.user.userprofile

    # Get all organizations
    organizations = Organization.objects.all()

    # Get organizations created by the user
    user_created_organizations = Organization.objects.filter(user_profile=user_profile)

    # Get followed organizations using the property
    followed_organizations = request.user.userprofile.followed_organizations

    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            organization = form.save(commit=False)
            organization.user_profile = user_profile  # Associate with the user's profile
            organization.save()
            messages.success(request, "Organization created successfully!")
            return redirect('dashboard:manage_organization')
    else:
        form = OrganizationForm()

    context = {
        'organizations': organizations,  # Pass queryset directly
        'followed_organizations': followed_organizations,  # Pass queryset directly
        'user_created_organizations': user_created_organizations,  # Pass queryset directly
        'form': form,
        'user_profile': user_profile
    }
    return render(request, 'dashboard/manage_organization.html', context)



@login_required
def follow_organization(request, organization_id):
    if request.method == "POST":
        organization = get_object_or_404(Organization, id=organization_id)
        if not OrganizationFollow.objects.filter(user=request.user, organization=organization).exists():
            OrganizationFollow.objects.create(user=request.user, organization=organization)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@login_required
def unfollow_organization(request, organization_id):
    if request.method == "POST":
        organization = get_object_or_404(Organization, id=organization_id)
        follow = OrganizationFollow.objects.filter(user=request.user, organization=organization)
        if follow.exists():
            follow.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@login_required
def organization_list(request):
    user_profile=request.user.userprofile
    organizations = Organization.objects.all()
    followed_organizations = OrganizationFollow.objects.filter(user=request.user).values_list('organization_id', flat=True)

    return render(request, 'dashboard/organization_list.html', {
        'user_profile':user_profile,
        'organizations': organizations,
        'followed_organizations': followed_organizations,
    })






