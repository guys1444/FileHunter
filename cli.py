import typer
from .pdf_scanner import (
    extract_text_from_pdf,
    find_base64_encoded,
    find_hex_encoded,
    find_url_encoded,
    find_html_encoded,
    find_rot13_encoded,
    find_binary_encoded,
    find_quoted_printable_encoded,
    find_uuencoded
)

app = typer.Typer()

@app.command()
def scan(pdf_path: str, encoding: str):
    text = extract_text_from_pdf(pdf_path)
    if encoding == "base64":
        encoded_scripts = find_base64_encoded(text)
    elif encoding == "hex":
        encoded_scripts = find_hex_encoded(text)
    elif encoding == "url":
        encoded_scripts = find_url_encoded(text)
    elif encoding == "html":
        encoded_scripts = find_html_encoded(text)
    elif encoding == "rot13":
        encoded_scripts = find_rot13_encoded(text)
    elif encoding == "binary":
        encoded_scripts = find_binary_encoded(text)
    elif encoding == "quoted-printable":
        encoded_scripts = find_quoted_printable_encoded(text)
    elif encoding == "uuencode":
        encoded_scripts = find_uuencoded(text)
    else:
        print("Unsupported encoding type.")
        return

    if encoded_scripts:
        print(f"Encoded scripts found ({encoding}):")
        for script in encoded_scripts:
            print(script)
    else:
        print(f"No encoded scripts found for {encoding}.")

@app.command()
def scan_all(pdf_path: str):
    text = extract_text_from_pdf(pdf_path)
    encodings = {
        "base64": find_base64_encoded,
        "hex": find_hex_encoded,
        "url": find_url_encoded,
        "html": find_html_encoded,
        "rot13": find_rot13_encoded,
        "binary": find_binary_encoded,
        "quoted-printable": find_quoted_printable_encoded,
        "uuencode": find_uuencoded
    }

    for encoding, find_function in encodings.items():
        encoded_scripts = find_function(text)
        if encoded_scripts:
            print(f"Encoded scripts found ({encoding}):")
            for script in encoded_scripts:
                print(script)
        else:
            print(f"No encoded scripts found for {encoding}.")

if __name__ == "__main__":
    app()
