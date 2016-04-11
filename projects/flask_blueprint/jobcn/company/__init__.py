from flask import Blueprint

company = Blueprint(
    'company',
    __name__,
    template_folder='company_templates'
)

from . import views
