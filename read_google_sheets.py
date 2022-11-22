import pandas as pd
import glob
from google_api_connector import google_api
from fpdf import FPDF

class convert_sheet:

    def __init__(self, spreadsheet_id:str, spreadsheet_range:str, credentials:str):
  
        self.google_sheets = google_api(
            SAMPLE_SPREADSHEET_ID = spreadsheet_id,
            SAMPLE_RANGE_NAME     = spreadsheet_range,
            CREDENTIALS           = credentials
        )


    def generate_dataframe(self, api_response):
        df = pd.DataFrame(api_response)
        df = df.rename(columns=df.iloc[0]).drop(df.index[0]).replace({'--':None}).reset_index(drop=True)
        col_mapper = {}
        
        for col in df.columns.tolist():
            col_mapper[col] = col.replace(' ', '_').replace('.','').replace('%','').lower()
        
        return df.rename(columns=col_mapper)


    def pdf(self, texto, nome_arquivo):
        
        pdf = FPDF()    
        pdf.add_page()
        pdf.set_font("Arial", size = 12)
        
        for i, campo in zip(range(len(texto)), texto.keys()):
            # create a cell
            pdf.cell(200, 10, txt = f'{campo}: {texto[campo]}',
                    ln = i + 1, align = 'L')
        
        # save the pdf with name .pdf
        pdf.output(f"{nome_arquivo}.pdf")


    def to_pdf(self):
        lista_inscritos = self.generate_dataframe(self.google_sheets.get_sheet())

        lista_inscritos = lista_inscritos.reset_index(drop = True)

        for i in range(len(lista_inscritos)):
            texto = {}

            for campo in lista_inscritos.columns:
                valor = lista_inscritos.loc[i, campo]
                texto[campo] = valor

            self.pdf(
                texto = texto,
                nome_arquivo = f"{lista_inscritos.loc[i, 'nome']} - {lista_inscritos.loc[i, 'cpf']}"
            )
        
        print(f'Foram gerados {i+1} arquivos em PDF!\n')

        for file in glob.glob("*.pdf"):
            print(file)