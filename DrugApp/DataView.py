from flask import (Blueprint, render_template)

dv = Blueprint('data', __name__, url_prefix='/data')


@dv.route('/view', methods=('GET','POST'))
def view_data():
    return render_template('common/base.html')
