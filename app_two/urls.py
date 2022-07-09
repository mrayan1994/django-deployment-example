"""app_two URL Configuration

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app_two import views

app_name = 'app_two'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('relative_url_templates', views.relative_url_templates_view, name='relative_url_templates'),  # noqa E501
]
