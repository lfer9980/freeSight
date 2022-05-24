from flask import Blueprint

error_bp = Blueprint(name = 'error',
                     import_name = __name__)

from . import routes