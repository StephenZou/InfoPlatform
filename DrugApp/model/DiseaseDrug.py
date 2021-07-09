from sqlalchemy import Column, String
from DrugApp.core.database import Base


class DiseaseDrug(Base):
    __tablename__ = 'disease_drug'
    disease_id = Column(String(128), primary_key=True)
    disease_name = Column(String(512))
    drug_inchikey = Column(String(512))
    drug_name = Column(String(512))

    def __init__(self, disease_name=None, drug_inchikey=None, drug_name=None):
        self.disease_name = disease_name
        self.drug_inchikey = drug_inchikey
        self.drug_name = drug_name
