"""app_one URL Configuration

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
from app_one import views

app_name = 'app_one'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('home', views.home_view, name='home'),
    path('user_login', views.user_login_view, name='user_login'),
    path('user_logout', views.user_logout_view, name='user_logout'),
    path('user_registration', views.user_registration_view, name='user_registration'),  # noqa E501
    # path('form_page', views.form_page_view, name='form_page'),
    path('access_records_page', views.records_page_view, name='access_records_page'),  # noqa E501
]
