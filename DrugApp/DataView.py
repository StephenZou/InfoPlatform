from flask import (Blueprint, render_template, request)
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


@dv.route('/compounds', methods=['GET'])
def get_compounds():
    disease = str(request.args.get('disease'))
    if disease == 'disease1':
        data = [20, 30, 40, 50, 60]
    else:
        data = [60, 50, 40, 30, 20]
    return {'data': data}


@dv.route('/detail', methods=['GET'])
def get_detail():
    # disease = str(request.args.get('disease'))
    # print(disease)
    page_size = request.args.get('pageSize')
    page_number = request.args.get('pageNumber')

    print(request.args.get('rows'))
    print(request.args.get('page'))
    print(request.args.get('disease'))
    data = {'total': 16, 'rows': [{'disease_id': '1', 'disease_name': '2', 'drug_inchikey': '3',
                                  'drug_name': '4', 'com_inchikey': '5', 'tar_over_rate': '6',
                                  'tc': '7', 'target_overlap_rate': '8'},
                                 {'disease_id': '1', 'disease_name': '2', 'drug_inchikey': '3',
                                  'drug_name': '4', 'com_inchikey': '5', 'tar_over_rate': '6',
                                  'tc': '7', 'target_overlap_rate': '8'},
                                 {'disease_id': '1', 'disease_name': '2', 'drug_inchikey': '3',
                                  'drug_name': '4', 'com_inchikey': '5', 'tar_over_rate': '6',
                                  'tc': '7', 'target_overlap_rate': '8'},
                                 {'disease_id': '1', 'disease_name': '2', 'drug_inchikey': '3',
                                  'drug_name': '4', 'com_inchikey': '5', 'tar_over_rate': '6',
                                  'tc': '7', 'target_overlap_rate': '8'},
                                 {'disease_id': '1', 'disease_name': '2', 'drug_inchikey': '3',
                                  'drug_name': '4', 'com_inchikey': '5', 'tar_over_rate': '6',
                                  'tc': '7', 'target_overlap_rate': '8'},
                                 {'disease_id': '1', 'disease_name': '2', 'drug_inchikey': '3',
                                  'drug_name': '4', 'com_inchikey': '5', 'tar_over_rate': '6',
                                  'tc': '7', 'target_overlap_rate': '8'},
                                 {'disease_id': '1', 'disease_name': '2', 'drug_inchikey': '3',
                                  'drug_name': '4', 'com_inchikey': '5', 'tar_over_rate': '6',
                                  'tc': '7', 'target_overlap_rate': '8'},
                                 {'disease_id': '1', 'disease_name': '2', 'drug_inchikey': '3',
                                  'drug_name': '4', 'com_inchikey': '5', 'tar_over_rate': '6',
                                  'tc': '7', 'target_overlap_rate': '8'},
                                 {'disease_id': '1', 'disease_name': '2', 'drug_inchikey': '3',
                                  'drug_name': '4', 'com_inchikey': '5', 'tar_over_rate': '6',
                                  'tc': '7', 'target_overlap_rate': '8'},
                                 {'disease_id': '1', 'disease_name': '2', 'drug_inchikey': '3',
                                  'drug_name': '4', 'com_inchikey': '5', 'tar_over_rate': '6',
                                  'tc': '7', 'target_overlap_rate': '8'},
                                 {'disease_id': '1', 'disease_name': '2', 'drug_inchikey': '3',
                                  'drug_name': '4', 'com_inchikey': '5', 'tar_over_rate': '6',
                                  'tc': '7', 'target_overlap_rate': '8'},
                                 {'disease_id': '1', 'disease_name': '2', 'drug_inchikey': '3',
                                  'drug_name': '4', 'com_inchikey': '5', 'tar_over_rate': '6',
                                  'tc': '7', 'target_overlap_rate': '8'},
                                 {'disease_id': '1', 'disease_name': '2', 'drug_inchikey': '3',
                                  'drug_name': '4', 'com_inchikey': '5', 'tar_over_rate': '6',
                                  'tc': '7', 'target_overlap_rate': '8'},
                                 {'disease_id': '1', 'disease_name': '2', 'drug_inchikey': '3',
                                  'drug_name': '4', 'com_inchikey': '5', 'tar_over_rate': '6',
                                  'tc': '7', 'target_overlap_rate': '8'},
                                 {'disease_id': '1', 'disease_name': '2', 'drug_inchikey': '3',
                                  'drug_name': '4', 'com_inchikey': '5', 'tar_over_rate': '6',
                                  'tc': '7', 'target_overlap_rate': '8'},
                                 {'disease_id': '1', 'disease_name': '2', 'drug_inchikey': '3',
                                  'drug_name': '4', 'com_inchikey': '5', 'tar_over_rate': '6',
                                  'tc': '7', 'target_overlap_rate': '8'}]}
    return data
