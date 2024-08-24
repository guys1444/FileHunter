import PyPDF2
import base64
import re
import urllib.parse
import binascii

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extract_text()
        return text

def find_base64_encoded(text):
    base64_pattern = re.compile(r'([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?')
    matches = base64_pattern.findall(text)
    encoded_scripts = [match[0] for match in matches if match[0]]
    
    decoded_scripts = []
    for script in encoded_scripts:
        try:
            decoded_script = base64.b64decode(script).decode('utf-8')
            decoded_scripts.append(decoded_script)
        except Exception as e:
            print(f"Error decoding Base64 script: {e}")
    
    return decoded_scripts

def find_hex_encoded(text):
    hex_pattern = re.compile(r'([0-9a-fA-F]{2})+')
    matches = hex_pattern.findall(text)
    decoded_scripts = []
    for match in matches:
        try:
            decoded_script = bytes.fromhex(match).decode('utf-8')
            decoded_scripts.append(decoded_script)
        except Exception as e:
            print(f"Error decoding hex script: {e}")
    
    return decoded_scripts

def find_url_encoded(text):
    url_pattern = re.compile(r'%[0-9a-fA-F]{2}')
    matches = url_pattern.findall(text)
    decoded_scripts = []
    for match in matches:
        try:
            decoded_script = urllib.parse.unquote(match)
            decoded_scripts.append(decoded_script)
        except Exception as e:
            print(f"Error decoding URL script: {e}")
    
    return decoded_scripts

def find_html_encoded(text):
    html_pattern = re.compile(r'&[a-zA-Z]+;')
    matches = html_pattern.findall(text)
    decoded_scripts = []
    for match in matches:
        try:
            decoded_script = html.unescape(match)
            decoded_scripts.append(decoded_script)
        except Exception as e:
            print(f"Error decoding HTML script: {e}")
    
    return decoded_scripts

def find_rot13_encoded(text):
    rot13_pattern = re.compile(r'[A-Za-z]')
    matches = rot13_pattern.findall(text)
    decoded_scripts = []
    for match in matches:
        try:
            decoded_script = codecs.decode(match, 'rot_13')
            decoded_scripts.append(decoded_script)
        except Exception as e:
            print(f"Error decoding ROT13 script: {e}")
    
    return decoded_scripts

def find_binary_encoded(text):
    binary_pattern = re.compile(r'[01]{8}')
    matches = binary_pattern.findall(text)
    decoded_scripts = []
    for match in matches:
        try:
            decoded_script = ''.join(chr(int(match[i:i+8], 2)) for i in range(0, len(match), 8))
            decoded_scripts.append(decoded_script)
        except Exception as e:
            print(f"Error decoding binary script: {e}")
    
    return decoded_scripts

def find_quoted_printable_encoded(text):
    qp_pattern = re.compile(r'=[0-9A-F]{2}')
    matches = qp_pattern.findall(text)
    decoded_scripts = []
    for match in matches:
        try:
            decoded_script = quopri.decodestring(match).decode('utf-8')
            decoded_scripts.append(decoded_script)
        except Exception as e:
            print(f"Error decoding quoted-printable script: {e}")
    
    return decoded_scripts

def find_uuencoded(text):
    uu_pattern = re.compile(r'begin [0-7]{3} [^\n]+\n([^\n]+\n)+end')
    matches = uu_pattern.findall(text)
    decoded_scripts = []
    for match in matches:
        try:
            decoded_script = binascii.a2b_uu(match).decode('utf-8')
            decoded_scripts.append(decoded_script)
        except Exception as e:
            print(f"Error decoding UUencoded script: {e}")
    
    return decoded_scripts
