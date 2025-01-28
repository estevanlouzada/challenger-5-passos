import pandas as pd
from utils import config

def load_data(filename):
    try:
      
      file_path = 'data/PEDE_PASSOS_DATASET_FIAP.csv'
      pd.set_option('display.max_columns', None)
      df = pd.read_csv(file_path, delimiter=';')
      return df
    
    except FileNotFoundError:
      return None
    
def load_data_ideb(filename):
    try:
      
      file_path = 'data/idepeducacaosp.csv'
      pd.set_option('display.max_columns', None)
      df = pd.read_csv(file_path, delimiter=',')
      return df
    
    except FileNotFoundError:
      return None
    
# funcoes que realiza tratamento dos dados...