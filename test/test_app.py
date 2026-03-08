import os
import tempfile
import importlib

def test_app_writes_file(tmp_path):
 
    import app
    app.USERNAME = "testuser"
    app.DATA_DIR = str(tmp_path)

    app.main()

    files = list(tmp_path.glob("testuser_assignment4_*.txt"))
    assert len(files) == 1

    content = files[0].read_text(encoding="utf-8")
    assert "username=testuser" in content
    assert "status=ok" in content