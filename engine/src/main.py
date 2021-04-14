from engine.src.utils.generate_excel import GenerateExcel
import os

SCHEMA_NAME = os.environ['SCHEMA_NAME'].split('=')[1]
TABLE_NAME = os.environ['TABLE_NAME'].split('=')[1]

def run():
    genexcel = GenerateExcel()
    genexcel.gen_single_file(SCHEMA_NAME,TABLE_NAME)
    return True

if __name__=='__main__':
    run()
