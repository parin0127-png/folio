import pandas as p 
import os 
from io import StringIO

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def write_excel(data , filename = "output.xlsx"):
    """create and write data, tables, or spreadsheet content to an excel file"""

    path = os.path.join(BASE_DIR, "..", "..", "outputs" , filename)
    os.makedirs(os.path.dirname(path) , exist_ok = True)

    try:
        df = p.read_csv(StringIO(data))
    except:
        df = p.DataFrame({"Content": data.splitlines()})
        
    df.to_excel(path, index = False)
    return f"> Saved to {path}"
