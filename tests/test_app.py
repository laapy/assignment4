import sys
from pathlib import Path

# 把项目根目录加到 Python 路径里
sys.path.append(str(Path(__file__).resolve().parents[1]))

import app


def test_app_writes_file(tmp_path):
    app.USERNAME = "testuser"
    app.DATA_DIR = str(tmp_path)

    app.main()

    files = list(tmp_path.glob("testuser_assignment4_*.txt"))
    assert len(files) == 1

    content = files[0].read_text(encoding="utf-8")
    assert "username=testuser" in content
    assert "status=ok" in content