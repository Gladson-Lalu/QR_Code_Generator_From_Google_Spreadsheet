# QR Code Generator from Google Spreadsheet

This is a simple Python script that generates QR codes from Google Spreadsheet column URLs

## Requirements

* Python 2.7
* [qrcode](https://pypi.python.org/pypi/qrcode)
* [Pillow](https://pypi.python.org/pypi/Pillow)
* [gspread](https://pypi.python.org/pypi/gspread)


## Usage

1. Create a Google Spreadsheet with a column of URLs
2. Share the spreadsheet with the email address of the service account
3. Download the JSON key file for the service account
4. Place the JSON key file as app\core\service\credentials.json
5. Give arguments spreadsheet ID, Worksheet name and column name to main.py
* optional: give a path to save the QR codes
* optional: give a base url to prepend to the URLs

####  Syntax

    qrcode_gen.main(spreadsheet_id= <spreadsheet_id>, worksheet_name= <worksheet_name>,
                colName=<colName>, base_url=<base_url>, output_dir=<output_dir>)
6. Run main.py


## Example

    qrcode_gen.main(spreadsheet_id='1X2X3X4X5X6X7X8X9X0X1X2X3X4X5X6X7X8X9X0X', worksheet_name='Sheet1',
                colName='A', base_url='http://www.example.com', output_dir='C:\Users\example\Documents\QRcodes')

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details


## Acknowledgments

* [qrcode](https://pypi.python.org/pypi/qrcode)