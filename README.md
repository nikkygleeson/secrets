# Application - Encryption

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/ghandic/PyCap-TODO-CRUD)
![Coverage](https://img.shields.io/badge/coverage-100%25-green)

This commandline program is a basic implementation for an encryption application using Python 3.6+ that allows you to encrypt and decrypt basic strings of text using common ciphers (Hex Cipher, Atbash Cipher, Caesar Cipher, Keyword Cipher and Vigenere Cipher).

## Requirements

This program requires the following Python packages:

- [Typer](https://typer.tiangolo.com/)

## Usage

### Program options

| Operation                                            | Usage | Required |
|------------------------------------------------------|-------|----------|
| Encode a message using a Hex cipher | `python secrets.py hex encode "<MESSAGE>"` | TRUE |
| Decode a message using a Hex cipher | `python secrets.py hex decode "<ENCRYPTED-MESSAGE>"` | TRUE |
| Encode a message using an AtBash cipher | `python secrets.py atbash encode "<MESSAGE>"` | TRUE |
| Decode a message using an AtBash cipher | `python secrets.py atbash decode "<ENCRYPTED-MESSAGE>"` | TRUE |
| Encode a message using a Caesar cipher | `python secrets.py caesar encode <KEY> "<MESSAGE>"` | TRUE |
| Decode a message using a Caesar cipher | `python secrets.py caesar decode <KEY> "<ENCRYPTED-MESSAGE>"` | TRUE |
| Encode a message using a Keyword cipher | `python secrets.py keyword encode "<KEYWORD>" "<MESSAGE>"` | TRUE |
| Decode a message using a Keyword cipher | `python secrets.py keyword decode "<KEYWORD>" "<ENCRYPTED-MESSAGE>"` | TRUE |
| Encode a message using a Vigenère cipher | `python secrets.py vigenere encode "<KEYWORD>" "<MESSAGE>"` | TRUE |
| Decode a message using a Vigenère cipher | `python secrets.py vigenere decode "<KEYWORD>" "<ENCRYPTED-MESSAGE>"` | TRUE |

## Pros, cons and next steps

### Pros

- Very simple program to understand and build
- Very easy to port to another interactive medium such as a REST API

### Cons

- Very basic ciphers which are easy to crack using statistical analysis
- Currently only handles a small number of characters (a-z)

### Next steps

- Expand to more advanced 
- Expand to a greater number of characters (A-Z, spaces, special characters, etc.)

## License

This project is licensed under the terms of the MIT license.
