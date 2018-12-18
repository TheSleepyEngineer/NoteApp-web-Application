from flask import Blueprint, render_template, request

bp = Blueprint(__name__, __name__,template_folder='../templates')

@bp.route('/createnote', methods=['POST', 'GET'])
def show():
    if request.method == 'POST':
        if request.form.get('createnote'):
                return 'Clicked'
    return render_template('createnote.html')