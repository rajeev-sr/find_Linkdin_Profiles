import pandas as pd

def com_list(file):
    df=pd.read_excel(file)
    df.columns = df.columns.str.lower()
    df.dropna(subset=['company'],inplace=True)
    
    list = df['company'].tolist()

    return list