import typer

from .secrets import (
    hex_cipher_encryptor,
    hex_cipher_decryptor,
    atbash_cipher_encryptor_decryptor,
    caesar_cipher_encryptor,
    caesar_cipher_decryptor,
    keyword_cipher_encryptor,
    keyword_cipher_decryptor,
    vigenere_cipher_encryptor,
    vigenere_cipher_decryptor,
)


def get_hex_app():

    app = typer.Typer()

    @app.command("encode")
    def app_encode(message: str) -> str:
        print(hex_cipher_encryptor(message))

    @app.command("decode")
    def app_decode(encrypted_message: str) -> str:
        print(hex_cipher_decryptor(encrypted_message))

    return app


def get_atbash_app():

    app = typer.Typer()

    @app.command("encode")
    def app_encode(message: str) -> str:
        print(atbash_cipher_encryptor_decryptor(message))

    @app.command("decode")
    def app_decode(message: str) -> str:
        print(atbash_cipher_encryptor_decryptor(message))

    return app


def get_caesar_app():

    app = typer.Typer()

    @app.command("encode")
    def app_encode(key: int, message: str) -> str:
        print(caesar_cipher_encryptor(key, message))

    @app.command("decode")
    def app_decode(key: int, encrypted_message: str) -> str:
        print(caesar_cipher_decryptor(key, encrypted_message))

    return app


def get_keyword_app():

    app = typer.Typer()

    @app.command("encode")
    def app_encode(key: str, message: str) -> str:
        print(keyword_cipher_encryptor(key, message))

    @app.command("decode")
    def app_decode(key: str, encrypted_message: str) -> str:
        print(keyword_cipher_decryptor(key, encrypted_message))

    return app


def get_vigenere_app():

    app = typer.Typer()

    @app.command("encode")
    def app_encode(key: str, message: str) -> str:
        print(vigenere_cipher_encryptor(key, message))

    @app.command("decode")
    def app_decode(key: str, encrypted_message: str) -> str:
        print(vigenere_cipher_decryptor(key, encrypted_message))

    return app


def app():

    app = typer.Typer()

    app.add_typer(get_hex_app(), name="hex")
    app.add_typer(get_atbash_app(), name="atbash")
    app.add_typer(get_caesar_app(), name="caesar")
    app.add_typer(get_keyword_app(), name="keyword")
    app.add_typer(get_vigenere_app(), name="vigenere")

    return app
