from flask import (Blueprint, render_template)
from DrugApp.model import ViewModel

dv = Blueprint('data', __name__, url_prefix='/data')


@dv.route('/view', methods=('GET', 'POST'))
def view_data():
    diseases = ['disease1', 'disease2', 'disease3', 'disease4', 'disease5', 'disease6', 'disease7', 'disease8']
    drugs = ['drug1', 'drug2', 'drug3', 'drug4', 'drug5', 'drug6', 'drug7', 'drug8', 'drug9', 'drug10', 'drug11']
    indications = []
    compounds = []
    targets = []
    vm = ViewModel.ViewModel(diseases, drugs, indications, compounds, targets)
    return render_template('home.html', vm=vm)
