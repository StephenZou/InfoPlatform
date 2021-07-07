
class ViewModel:
    def __init__(self, diseases, drugs, indications, compounds, targets):
        self.diseases = diseases
        self.drugs = drugs
        self.indications = indications
        self.compounds = compounds
        self.targets = targets
        if diseases is not None:
            self.num_diseases = len(diseases)
        else:
            self.num_diseases = 0
        if drugs is not None:
            self.num_drugs = len(drugs)
        else:
            self.num_drugs = 0
        if indications is not None:
            self.num_indications = len(indications)
        else:
            self.num_indications = 0
        if compounds is not None:
            self.num_compounds = len(compounds)
        else:
            self.num_compounds = 0
        if targets is not None:
            self.num_targets = len(targets)
        else:
            self.num_targets = 0