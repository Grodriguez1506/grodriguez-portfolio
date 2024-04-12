from .models import Project

def get_projects(request):

    projects = Project.objects.values_list('title', 'url' )

    return {
        'projects': projects
    }