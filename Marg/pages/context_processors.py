# your_app/context_processors.py

def secondary_nav(request):
    path = request.path
    secondary_nav_items = []

    if path.startswith('/about/'):
        secondary_nav_items = [
            {'name': 'The MARG', 'url_name': 'about'},
            {'name': 'ICOMOS Charter On Cultural Routes', 'url_name': 'https://admin.icomos.org/wp-content/uploads/2023/01/culturalroutes_e.pdf' , 'type': 'external'},
        ]

    elif path.startswith('/explore/'):
        secondary_nav_items = [
            {'name': 'Historic Routes', 'url_name': 'explore_historic_routes'},
            {'name': 'Cultural Routes', 'url_name': 'explore_cultural_routes'},
            {'name': 'Railway Routes', 'url_name': 'explore_railway_routes'},
            {'name': 'Cultural Elements', 'url_name': 'explore_cultural_elements'},
        ]

    elif path.startswith('/identification_documentation/'):
        secondary_nav_items = [
            {'name': 'Our Methodology', 'url_name': 'identification_documentation_methodology'},
            {'name': 'Classification of Historic Roads', 'url_name': 'identification_documentation_classification'},
            {'name': 'Bhotiya Trade Routes', 'url_name': 'identification_documentation_bhotiya'},
            {'name': 'Routes at Risk', 'url_name': 'identification_documentation_risk'},
        ]

    elif path.startswith('/conservation/'):
        secondary_nav_items = [
            {'name': 'Preservation', 'url_name': 'conservation_preservation'},
            {'name': 'Rehabilitation', 'url_name': 'conservation_rehabilitation'},
            {'name': 'Restoration', 'url_name': 'conservation_restoration'},
            {'name': 'Reconstruction', 'url_name': 'conservation_reconstruction'},
        ]

    elif path.startswith('/management/'):
        secondary_nav_items = [
            {'name': 'Safety', 'url_name': 'management_safety'},
            {'name': 'Liability', 'url_name': 'management_liability'},
            {'name': 'Policy', 'url_name': 'management_policy'},
            {'name': 'Heritage Bylaws', 'url_name': 'management_heritage_bylaws'},
            {'name': 'Key Stakeholders / Custodians', 'url_name': 'management_stakeholders'},
        ]

    return {'secondary_nav_items': secondary_nav_items}
