template = {
    "swagger": "2.0",
    "info": {
        "title": "QuoteAPI",
        "description": "Api documantation for quote api. ",
        "contact": {
            "responsibleOrganization": "",
            "responsibleDeveloper": "",
            "email": "kontakt.pawelkwiatkowski@gmail.com",
            "url": "www.twitter.com/xkwiatuh",
        },
        "termsOfService": "www.twitter.com/xkwiatuh",
        "version": "BETA 1.0"
    },
    "basePath": "/api/v1",  # base bash for blueprint registration
    "schemes": [
        "http",
        "https"
    ]
    
}

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}