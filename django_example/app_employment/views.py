from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from app_employment.models import Vacancy
from django.contrib.auth.decorators import permission_required
# Create your views here.
# def vacancy_list(request): #1 Вариант( в лоб)
#     if request.user.has_perm('app_employment.view_vacancy'):#<app>.<action>_<object_name>
#         vacancies = Vacancy.objects.all()
#         return render(request, 'employment/vacancy_list.html', context={'vacancy_list': vacancies})
#     else:
#         raise PermissionDenied()

# def vacancy_list(request): # 2 Вариант( по изящнее)
#     if not request.user.has_perm('app_employment.view_vacancy'):#<app>.<action>_<object_name>
#         raise PermissionDenied()
#     vacancies = Vacancy.objects.all()
#     return render(request, 'employment/vacancy_list.html', context={'vacancy_list': vacancies})

@permission_required('app_employment.view_vacancy')
def vacancy_list(request): # Вариант через декораторы
    vacancies = Vacancy.objects.all()
    return render(request, 'employment/vacancy_list.html', context={'vacancy_list': vacancies})

