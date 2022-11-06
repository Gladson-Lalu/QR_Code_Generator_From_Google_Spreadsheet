import qrcode
import os
import core.service.spreadsheet_service as spreadsheet_service


def generate_qr_code(url, file_name):
    img = qrcode.make(url)
    img.save(file_name)


def main(spreadsheet_id, worksheet_name, colName, base_url='', output_dir='output'):
    print('Generating QR codes...')
    spreadsheet = spreadsheet_service.Spreadsheet(spreadsheet_id)
    urls = spreadsheet.get_route_urls(worksheet_name, colName)
    urls.remove(colName)
    for index, url in enumerate(urls):
        if url != '':
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            file_name = os.path.join(output_dir, f'{index}.png')
            generate_qr_code(base_url + '/' + url, file_name)
            print('QR code generated for ' + url)
