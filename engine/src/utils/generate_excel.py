import json
import pandas as pd
import os

"""PPM_ID = C4
Project Code = C5
Interface Name = C6
File Name = C8
Markets = C9
Sandbox = C10
Input file type MFS= C11
Mode= C12
Compressed File = C13
Character Set = C14
Newline Delimiter = C15
Source Layout delimiter= C16
Source Layout char= E16
Source Layout Template = C17
DDL Template bool= C18
DDL Template location= E18
Header = C19
Footer = C20
Expected Volume = C21
Number of Files sent on daily basis = C22
C23,E23
Execution Type = C24"""

class GenerateExcel(object):

    def __init__(self):
        self.CUR_DIR = os.getcwd()
        print(self.CUR_DIR)
        print(os.environ)
        self.SANDBOX = os.environ['SANDBOX']
        self.WORK_TABLE_NAME = os.environ['WORK_TABLE_NAME']
        self.DATA_RETENTION = os.environ['DATA_RETENTION']
        self.DATE_FIELD_DRIVING_HISTORIZATION = os.environ['DATE_FIELD_DRIVING_HISTORIZATION']
        self.IGNORE_FIELD_CDC = os.environ['IGNORE_FIELD_CDC']
        self.TRANSCODE_FIELD_NAME = os.environ['TRANSCODE_FIELD_NAME']
        self.DELETE_INFO = os.environ['DELETE_INFO']
        self.SOURCE_FILE_PATH = os.environ['SOURCE_FILE_PATH']
        self.ARCHIVE_DEL_FLAG = os.environ['ARCHIVE_DEL_FLAG']
        self.JOB_NAME = os.environ['JOB_NAME']
        self.SCHEDULE_NAME = os.environ['SCHEDULE_NAME']
        self.SCHEMA_NAME = os.environ['SCHEMA_NAME']
        self.TABLE_NAME = os.environ['TABLE_NAME']

    # def get_json_file_list(self):
    #     files_list = list()
    #     source_path = CUR_DIR+'/engine/sources/15. Source Inventory/SOURCE INTERFACE 02.05.000/'
    #     source_interface_schemas = os.listdir(source_path)
    #     for schema in source_interface_schemas:
    #         if '.DS_Store'== schema:
    #             pass
    #         else:
    #             json_files = os.listdir(source_path+schema)
    #             for json_file in json_files:
    #                 print(schema)
    #                 if json_file == '.DS_Store':
    #                     pass
    #                 else:
    #                     files_list.append(f"{source_path}{schema}/{json_file}")
    #     return files_list
    #
    #
    def read_json_file(self, source_path):
        with open(source_path) as json_f:
            data = json.load(json_f)
            return data
    #
    #
    #
    #
    # def gen_all_tables(self):
    #
    #     for file_path in get_json_file_list():
    #         table_name = file_path.split('/')[-1].replace('.json','')
    #         schema_name = file_path.split('/')[-2]
    #         try:
    #             os.mkdir(f'targets/{schema_name}')
    #         except:
    #             pass
    #         # print(schema_name, table_name)
    #
    #         with pd.ExcelFile('template/template_oto_loader.xlsx') as reader:
    #             sheet_summary = pd.read_excel(reader, sheet_name='Summary')
    #             sheet_interface = pd.read_excel(reader, sheet_name='Interface Layout')
    #
    #             data = read_json_file(file_path)
    #             print( schema_name,table_name)
    #             col_ref = 'Unnamed: 2'
    #             col_ref_e = 'Unnamed: 2'
    #
    #             try:
    #                 sheet_summary.at[2,col_ref]=data['ppm id']
    #                 # try:
    #                 #     sheet_summary.at[2,col_ref]=data['ppm id']
    #                 # except:
    #                 #     sheet_summary.at[2,col_ref]=""
    #                 sheet_summary.at[3,col_ref]=data['project code']
    #                 sheet_summary.at[4,col_ref]=data['name']
    #                 sheet_summary.at[6,col_ref]=data['file name']
    #                 sheet_summary.at[7,col_ref]=data['markets']
    #                 sheet_summary.at[8,col_ref]=SANDBOX
    #                 sheet_summary.at[9,col_ref]=data['input file type mfs']
    #                 sheet_summary.at[10,col_ref]=data['mode']
    #                 sheet_summary.at[11,col_ref]=data['compressed file']
    #                 sheet_summary.at[12,col_ref]=data['characterset']
    #                 sheet_summary.at[13,col_ref]=data['newline delimiter']
    #                 sheet_summary.at[14,col_ref_e]=data['delimiter']
    #                 sheet_summary.at[14,col_ref]=data['source file type']
    #                 sheet_summary.at[15,col_ref]='True'
    #                 sheet_summary.at[16,col_ref]=data['ddl template']
    #                 sheet_summary.at[17,col_ref]=data['header']
    #                 sheet_summary.at[18,col_ref]=data['footer']
    #                 sheet_summary.at[19,col_ref]=data['expected volume']
    #                 sheet_summary.at[20,col_ref]=data['number of files sent on daily basis']
    #                 sheet_summary.at[21,col_ref]=data['execution frequency']
    #                 sheet_summary.at[22,col_ref]=data['execution type']
    #                 sheet_summary.at[23,col_ref]=data['archival cfm']
    #                 sheet_summary.at[23,col_ref_e]=data['archival sa']
    #                 # sheet_summary.at[24,col_ref]=data['File Name']
    #                 sheet_summary.at[25,col_ref]=data['reference database name [database name] ']
    #                 sheet_summary.at[26,col_ref]=data['target table name']
    #                 # sheet_summary.at[27,col_ref]=data['File Name']
    #                 # sheet_summary.at[28,col_ref]=data['File Name']
    #                 # sheet_summary.at[29,col_ref]=data['File Name']
    #                 sheet_summary.at[30,col_ref]=data['historization']
    #                 sheet_summary.at[31,col_ref]=data['historization type']
    #                 sheet_summary.at[32,col_ref]=','.join(data['primary key']['columns'])
    #                 # sheet_summary.at[33,col_ref]=data['File Name']
    #                 # sheet_summary.at[34,col_ref]=data['File Name']
    #                 # sheet_summary.at[34,col_ref]=data['File Name']
    #                 # sheet_summary.at[36,col_ref]=data['File Name']
    #                 # sheet_summary.at[37,col_ref]=data['File Name']
    #                 # sheet_summary.at[38,col_ref]=data['File Name']
    #                 # sheet_summary.at[39,col_ref]=data['File Name']
    #                 # sheet_summary.at[40,col_ref]=data['File Name']
    #                 # sheet_summary.at[41,col_ref]=data['File Name']
    #                 # sheet_summary.at[42,col_ref]=data['File Name']
    #                 # sheet_summary.at[43,col_ref]=data['File Name']
    #
    #                 sheet_summary.head(50)
    #
    #                 sheet_interface.columns
    #
    #                 from numpy import where
    #                 for idx,column in enumerate(data['column']):
    #
    #                     sheet_interface.at[idx,'Interface Name'] = data['name']
    #                     sheet_interface.at[idx,'Interface Field Name'] = column['name']
    #                     sheet_interface.at[idx,'Data Type'] = column['conformed data type']
    #                     sheet_interface.at[idx,'Length'] = where(column['conformed data type'] == 'datetime,',column['format'],column['fixed field length'])
    #                     sheet_interface.at[idx,'Nullable'] = column['nullable']
    #                     sheet_interface.at[idx,'Primary Key'] = column['primary']
    #                     sheet_interface.at[idx,'Source_Col_Order \n(LOS)'] = int(idx+1)
    #                     sheet_interface.at[idx,'Source_Target_Flag\n(LOS)'] = 'S'
    #                     sheet_interface.at[idx,'Comment (Optional)'] = ''
    #
    #
    #
    #             except:
    #                 print(schema_name, table_name)
    #                 print('not saved')
    #
    #         writer = pd.ExcelWriter(f'targets/{schema_name}/{table_name}.xlsx', engine='xlsxwriter')
    #         sheet_summary.to_excel(writer, sheet_name='Summary', index=False)
    #         workbook = writer.book
    #         sheet_summary = writer.sheets['Summary']
    #         merge_format = workbook.add_format({
    #             'bold': 1,
    #             'border': 1,
    #             'align': 'center',
    #             'valign': 'vcenter',
    #             'fg_color': 'orange'})
    #
    #         # sheet_summary.add_format({'align': 'center', 'valign': 'vcenter', 'border': 2})
    #
    #         sheet_summary.merge_range('A4:A6', 'Project', merge_format)
    #         sheet_summary.merge_range('A8:A25', 'Source', merge_format)
    #         sheet_summary.merge_range('A27:A30', 'Target', merge_format)
    #         sheet_summary.merge_range('A32:A43', 'Operational', merge_format)
    #         # sheet_summary.add_format({'align': 'center', 'valign': 'vcenter', 'border': 2})
    #
    #
    #         # merge_format = workbook.add_format({'align': 'center', 'valign': 'vcenter', 'border': 2})
    #
    #
    #
    #         sheet_interface.to_excel(writer, sheet_name='Interface Layout')
    #
    #         writer.save()


    def gen_single_file(self, schema_name, table_name):

        file_path = self.CUR_DIR +'/engine/sources/15. Source Inventory/SOURCE INTERFACE 02.05.000/'
        file_path = file_path + '{schema}/{table}'.format(schema=schema_name, table=table_name)+'.json'
        folder = self.CUR_DIR+"/engine/targets/"+schema_name
        try:
            os.mkdir(folder)
        except:
            pass

        with pd.ExcelFile(self.CUR_DIR+'/engine/template/template_oto_loader.xlsx') as reader:
            sheet_summary = pd.read_excel(reader, sheet_name='Summary')
            sheet_interface = pd.read_excel(reader, sheet_name='Interface Layout')

            data = self.read_json_file(file_path)
            print( schema_name,table_name)
            col_ref = 'Unnamed: 2'
            col_ref_e = 'Unnamed: 2'

            try:
                sheet_summary.at[2,col_ref]=data['ppm id']
                sheet_summary.at[3,col_ref]=data['project code']
                sheet_summary.at[4,col_ref]=data['name']
                sheet_summary.at[6,col_ref]=data['file name']
                sheet_summary.at[7,col_ref]=data['markets']
                sheet_summary.at[8,col_ref]=self.SANDBOX
                sheet_summary.at[9,col_ref]=data['input file type mfs']
                sheet_summary.at[10,col_ref]=data['mode']
                sheet_summary.at[11,col_ref]=data['compressed file']
                sheet_summary.at[12,col_ref]=data['characterset']
                sheet_summary.at[13,col_ref]=data['newline delimiter']
                sheet_summary.at[14,col_ref_e]=data['delimiter']
                sheet_summary.at[14,col_ref]=data['source file type']
                sheet_summary.at[15,col_ref]='True'
                sheet_summary.at[16,col_ref]=data['ddl template']
                sheet_summary.at[17,col_ref]=data['header']
                sheet_summary.at[18,col_ref]=data['footer']
                sheet_summary.at[19,col_ref]=data['expected volume']
                sheet_summary.at[20,col_ref]=data['number of files sent on daily basis']
                sheet_summary.at[21,col_ref]=data['execution frequency']
                sheet_summary.at[22,col_ref]=data['execution type']
                sheet_summary.at[23,col_ref]=data['archival cfm']
                sheet_summary.at[23,col_ref_e]=data['archival sa']
                # sheet_summary.at[24,col_ref]=data['File Name']
                sheet_summary.at[25,col_ref]=data['reference database name [database name] ']
                sheet_summary.at[26,col_ref]=data['target table name']
                # sheet_summary.at[27,col_ref]=data['File Name']
                # sheet_summary.at[28,col_ref]=data['File Name']
                # sheet_summary.at[29,col_ref]=data['File Name']
                sheet_summary.at[30,col_ref]=data['historization']
                sheet_summary.at[31,col_ref]=data['historization type']
                sheet_summary.at[32,col_ref]=','.join(data['primary key']['columns'])
                # sheet_summary.at[33,col_ref]=data['File Name']
                # sheet_summary.at[34,col_ref]=data['File Name']
                # sheet_summary.at[34,col_ref]=data['File Name']
                # sheet_summary.at[36,col_ref]=data['File Name']
                # sheet_summary.at[37,col_ref]=data['File Name']
                # sheet_summary.at[38,col_ref]=data['File Name']
                # sheet_summary.at[39,col_ref]=data['File Name']
                # sheet_summary.at[40,col_ref]=data['File Name']
                # sheet_summary.at[41,col_ref]=data['File Name']
                # sheet_summary.at[42,col_ref]=data['File Name']
                # sheet_summary.at[43,col_ref]=data['File Name']

                sheet_summary.head(50)

                sheet_interface.columns

                from numpy import where
                for idx,column in enumerate(data['column']):

                    sheet_interface.at[idx,'Interface Name'] = data['name']
                    sheet_interface.at[idx,'Interface Field Name'] = column['name']
                    sheet_interface.at[idx,'Data Type'] = column['conformed data type']
                    sheet_interface.at[idx,'Length'] = where(column['conformed data type'] == 'datetime,',column['format'],column['fixed field length'])
                    sheet_interface.at[idx,'Nullable'] = column['nullable']
                    sheet_interface.at[idx,'Primary Key'] = column['primary']
                    sheet_interface.at[idx,'Source_Col_Order \n(LOS)'] = int(idx+1)
                    sheet_interface.at[idx,'Source_Target_Flag\n(LOS)'] = 'S'
                    sheet_interface.at[idx,'Comment (Optional)'] = ''



            except:
                print(schema_name, table_name)
                print('not saved')

        writer = pd.ExcelWriter(self.CUR_DIR+'engine/targets/'+schema_name+'/'+table_name+'.xlsx', engine='xlsxwriter')
        sheet_summary.to_excel(writer, sheet_name='Summary', index=False)
        workbook = writer.book
        sheet_summary = writer.sheets['Summary']
        merge_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': 'orange'})

        sheet_summary.merge_range('A4:A6', 'Project', merge_format)
        sheet_summary.merge_range('A8:A25', 'Source', merge_format)
        sheet_summary.merge_range('A27:A30', 'Target', merge_format)
        sheet_summary.merge_range('A32:A43', 'Operational', merge_format)
        sheet_interface.to_excel(writer, sheet_name='Interface Layout')

        writer.save()
