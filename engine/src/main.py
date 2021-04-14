from engine.src.utils.generate_excel import GenerateExcel
import os

SCHEMA_NAME = os.environ['SCHEMA_NAME']
TABLE_NAME = os.environ['TABLE_NAME']

def run():
    genexcel = GenerateExcel()
    genexcel.gen_single_file(SCHEMA_NAME,TABLE_NAME)
    return True

if __name__=='__main__':
    run()
