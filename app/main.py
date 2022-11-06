import core.qrcode_gen as qrcode_gen

# form dotenv
# import os
# from dotenv import load_dotenv
# load_dotenv()

# spreadsheet_id = os.getenv('SPREADSHEET_ID')
# worksheet_name = os.getenv('WORKSHEET_NAME')
# colName = os.getenv('COL_NAME')
# base_url = os.getenv('BASE_URL')
# output_dir = os.getenv('OUTPUT_DIR')


qrcode_gen.main(spreadsheet_id=spreadsheet_id, worksheet_name=worksheet_name,
                colName=colName, base_url=base_url, output_dir=output_dir)
