from typer.testing import CliRunner

from ..secrets.cli import app

app = app()

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["hex", "encode", "helloworld"])
    assert result.exit_code == 0
    assert "0x680x650x6c0x6c0x6f0x770x6f0x720x6c0x64" in result.stdout

    result = runner.invoke(app, ["hex", "decode", "0x680x650x6c0x6c0x6f0x770x6f0x720x6c0x64"])
    assert result.exit_code == 0
    assert "helloworld" in result.stdout

    result = runner.invoke(app, ["atbash", "encode", "helloworld"])
    assert result.exit_code == 0
    assert "svooldliow" in result.stdout

    result = runner.invoke(app, ["atbash", "decode", "svooldliow"])
    assert result.exit_code == 0
    assert "helloworld" in result.stdout

    result = runner.invoke(app, ["caesar", "encode", "3", "helloworld"])
    assert result.exit_code == 0
    assert "khoorzruog" in result.stdout

    result = runner.invoke(app, ["caesar", "decode", "3", "khoorzruog"])
    assert result.exit_code == 0
    assert "helloworld" in result.stdout

    result = runner.invoke(app, ["keyword", "encode", "bye", "helloworld"])
    assert result.exit_code == 0
    assert "gckknvnqka" in result.stdout

    result = runner.invoke(app, ["keyword", "decode", "bye", "gckknvnqka"])
    assert result.exit_code == 0
    assert "helloworld" in result.stdout

    result = runner.invoke(app, ["vigenere", "encode", "bye", "helloworld"])
    assert result.exit_code == 0
    assert "icpmmapppe" in result.stdout

    result = runner.invoke(app, ["vigenere", "decode", "bye", "icpmmapppe"])
    assert result.exit_code == 0
    assert "helloworld" in result.stdout
