from flask import (Blueprint, render_template)

dv = Blueprint('data', __name__, url_prefix='/data')

# https://www.cnblogs.com/daniel-niu/p/10344828.html
@dv.route('/view', methods=('GET','POST'))
def view_data():
    return render_template('common/base.html')
