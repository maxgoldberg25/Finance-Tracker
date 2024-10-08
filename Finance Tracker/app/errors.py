from flask import render_template, Blueprint

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def error_404(error):
    return render_template('404.html'), 404

@errors.app_errorhandler(500)
def error_500(error):
    return render_template('500.html'), 500