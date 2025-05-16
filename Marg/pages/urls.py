from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name = 'home'),
    path('about/the_marg/' , views.about , name = 'about'),

    path('explore/historic_routes' , views.explore_historic_routes , name = 'explore_historic_routes'),
    path('explore/cultural_routes' , views.explore_cultural_routes , name = 'explore_cultural_routes'),
    path('explore/railway_routes' , views.explore_railway_routes , name = 'explore_railway_routes'),
    path('explore/cultural_elements' , views.explore_cultural_elements , name = 'explore_cultural_elements'),

    path('identification_documentation/our_methodology' , views.identification_documentation_methodology , name = 'identification_documentation_methodology'),
    path('identification_documentation/classification_of_historic_roads' , views.identification_documentation_classification , name = 'identification_documentation_classification'),
    path('identification_documentation/bhotiya_trade_routes' , views.identification_documentation_bhotiya , name = 'identification_documentation_bhotiya'),
    path('identification_documentation/our_methodology/routes_at_risk' , views.identification_documentation_risk , name = 'identification_documentation_risk'),

    path('conservation/preservation' , views.conservation_preservation , name = 'conservation_preservation'),
    path('conservation/rehabilitation' , views.conservation_rehabilitation , name = 'conservation_rehabilitation'),
    path('conservation/restoration' , views.conservation_restoration , name = 'conservation_restoration'),
    path('conservation/reconstruction' , views.conservation_reconstruction , name = 'conservation_reconstruction'),
    
    path('management/safety' , views.management_safety , name = 'management_safety'),
    path('management/liability' , views.management_liability , name = 'management_liability'),
    path('management/policy' , views.management_policy , name = 'management_policy'),
    path('management/heritage_bylaws' , views.management_heritage_bylaws , name = 'management_heritage_bylaws'),
    path('management/stakeholders' , views.management_stakeholders , name = 'management_stakeholders'),
]