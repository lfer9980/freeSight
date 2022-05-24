from . import error_bp
from flask import render_template

@error_bp.app_errorhandler(Exception)
def handle_error(error):
    
    return render_template('error.html',
                           error = error.code)