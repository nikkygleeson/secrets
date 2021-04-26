from typer.testing import CliRunner

# Import not working
from ..secrets.cli import app

runner = CliRunner()


def test_app():
    # Not sure how to call runner.invoke with custom command names - couldn't find any doco on this?
    result = runner.invoke(app, ["hex", "encode"], ["helloworld"])
    assert result.exit_code == 0
    assert "0x680x650x6c0x6c0x6f0x770x6f0x720x6c0x64" in result.stdout

    result = runner.invoke(
        app, ["hex", "decode"], ["0x680x650x6c0x6c0x6f0x770x6f0x720x6c0x64"]
    )
    assert result.exit_code == 0
    assert "helloworld" in result.stdout

    result = runner.invoke(app, ["atbash", "encode"], ["helloworld"])
    assert result.exit_code == 0
    assert "svooldliow" in result.stdout

    result = runner.invoke(app, ["atbash", "decode"], ["svooldliow"])
    assert result.exit_code == 0
    assert "helloworld" in result.stdout

    result = runner.invoke(app, ["caeser", "encode"], [3, "helloworld"])
    assert result.exit_code == 0
    assert "mjqqtbtwqi" in result.stdout

    result = runner.invoke(app, ["caeser", "decode"], [3, "mjqqtbtwqi"])
    assert result.exit_code == 0
    assert "helloworld" in result.stdout

    result = runner.invoke(app, ["keyword", "encode"], ["bye", "helloworld"])
    assert result.exit_code == 0
    assert "gckknvnqka" in result.stdout

    result = runner.invoke(app, ["keyword", "decode"], ["bye", "gckknvnqka"])
    assert result.exit_code == 0
    assert "helloworld" in result.stdout

    result = runner.invoke(app, ["vigenere", "encode"], ["bye", "helloworld"])
    assert result.exit_code == 0
    assert "icpmmapppe" in result.stdout

    result = runner.invoke(app, ["vigenere", "decode"], ["bye", "icpmmapppe"])
    assert result.exit_code == 0
    assert "helloworld" in result.stdout
