from django.views import View
from apps.auth.models import UserModel
from django.shortcuts import render
from django.core.paginator import Paginator
from utils.helper.pagination import get_paginated_response
# from faker import Faker
# import random

class UsersView(View):
    def get(self, request):
        # Get all users excluding the deleted ones
        users = UserModel.objects.all().exclude(is_deleted=True)

        count = request.GET.get('count', 5)
        page_number = request.GET.get('page', 1)
        page_obj = get_paginated_response(users, count, page_number)

        return render(request, 'user_mgmt/users.html', {'page_obj': page_obj})

    

        #faker = Faker()
        # for _ in range(500):
        #     # Generate fake data for each user
        #     username = faker.user_name()
        #     email = faker.email()
        #     password = 'password123'  # You can set any default password or hash it
        #     is_staff = random.choice([True, False])
        #     is_superuser = random.choice([True, False])
            
        #     # Create and save the fake user
        #     UserModel.objects.create(
        #         username=username,
        #         email=email,
        #         password=password,
        #         is_staff=is_staff,
        #         is_superuser=is_superuser
        #     )



# @method_decorator(login_required, name="dispatch")
# class Loan_Application_Management(View):
#     @staticmethod
#     def convert_to_float(value):
#         try:
#             return float(value)
#         except (ValueError, TypeError):
#             return None

#     def filter_loan_applications(self, request, all_loan_application, search_query):
#         try:
#             status_filters = {
#                 "created": Q(application_status__icontains="1") & Q(is_withdrawal=False),
#                 "following up": Q(application_status__icontains="2") & Q(is_withdrawal=False),
#                 "contract draft": Q(application_status__icontains="3") & Q(is_withdrawal=False),
#                 "approved": Q(application_status__icontains="4") & Q(is_withdrawal=False),
#                 "rejected": Q(application_status__icontains="5") & Q(is_withdrawal=False),
#                 "cancelled": Q(application_status__icontains="6") & Q(is_withdrawal=False),
#                 "remove application": Q(application_status__icontains="7") & Q(is_withdrawal=False),
#                 "rj": Q(application_status__icontains="8") & Q(is_withdrawal=False),
#                 "given up": Q(application_status__icontains="9") & Q(is_withdrawal=False),
#                 "oca": Q(application_status__icontains="10") & Q(is_withdrawal=False)               
#             }

#             lower_search_query = search_query.lower()
#             if lower_search_query in status_filters:
#                 return all_loan_application.filter(status_filters[lower_search_query])

#             return all_loan_application.filter(
#                 Q(loan_amount__exact=self.convert_to_float(search_query)) |
#                 Q(user__companyinformation__salary_amount__exact=self.convert_to_float(search_query)) |
#                 Q(user__companyinformation__salary_type__icontains=self.convert_to_float(search_query)) |
#                 Q(user__phone_number__icontains=search_query) |
#                 Q(id__icontains=search_query) 
#                 # Add more fields as needed
#             )
#         except ValueError:
#             return all_loan_application.filter(
#                 Q(user__english_name__icontains=search_query) |
#                 Q(user__chinese_name__icontains=search_query) |
#                 Q(user__userprofile__hk_id_number__icontains=search_query) |
#                 Q(application_status__icontains=search_query)
#                 # Add more fields as needed
#             )

#     def get_paginated_response(self, request, all_loan_application, page_length=None):
#         if page_length is None or page_length <= 0:
#             page_length = 25  # Set a default value if page_length is zero or negative

#         paginator = Paginator(all_loan_application, page_length)
#         page_number = request.GET.get("page")
#         page_obj = paginator.get_page(page_number)
#         return page_obj

#     @method_decorator(login_required, name="dispatch")
#     def get(self, request):
#         search_query = request.GET.get("search", "")
#         all_loan_application = LoanManagement.objects.prefetch_related(
#             'user__companyinformation_set', 'user__userprofile_set').order_by("-id")

#         if search_query:
#             filtered_applications = self.filter_loan_applications(request, all_loan_application, search_query)
#             page_obj = self.get_paginated_response(request, filtered_applications, page_length=filtered_applications.count())
#         else:
#             page_obj = self.get_paginated_response(request, all_loan_application)

#         return render(request, "loan_application_management.html",
#                       {'all_loan_application': all_loan_application, 'page_obj': page_obj, "search_query": search_query})