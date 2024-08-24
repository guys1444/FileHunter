# FileHunter
FileHunter is a powerful CLI tool that hunts down hidden encoded scripts in files. Its advanced scanning features make it an indispensable tool for security researchers.


scan-pdf path/to/your/pdf/file.pdf --encoding base64
<br>
scan-pdf path/to/your/pdf/file.pdf --encoding hex
<br>
scan-pdf path/to/your/pdf/file.pdf --encoding url
<br>
scan-pdf path/to/your/pdf/file.pdf --encoding html
<br>
scan-pdf path/to/your/pdf/file.pdf --encoding rot13
<br>
scan-pdf path/to/your/pdf/file.pdf --encoding binary
<br>
scan-pdf path/to/your/pdf/file.pdf --encoding quoted-printable
<br>
scan-pdf path/to/your/pdf/file.pdf --encoding uuencode


Install Typer: If you haven’t already, you need to install the typer package. You can do this using pip:
pip install typer

Prepare Your PDF Scanner Module: Ensure that your pdf_scanner module is correctly implemented and available in the same directory as your script. This module should contain the functions extract_text_from_pdf, find_base64_encoded, find_hex_encoded, find_url_encoded, find_html_encoded, find_rot13_encoded, find_binary_encoded, find_quoted_printable_encoded, and find_uuencoded.
Save Your Script: Save your script in a Python file, for example, pdf_scan.py.
Run the Script: You can run the script from the command line. The script expects two arguments: the path to the PDF file and the encoding type you want to scan for. Here is an example command:
python pdf_scan.py scan path/to/your/file.pdf base64
Replace path/to/your/file.pdf with the actual path to your PDF file and base64 with the encoding type you want to scan for (e.g., hex, url, html, rot13, binary, quoted-printable, uuencode).
