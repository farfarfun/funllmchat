"""funllmchat 占位包的最小验证：能正常导入，且版本号与 pyproject.toml 一致。"""

from pathlib import Path

import tomllib

import funllmchat


def test_import():
    """包可以正常导入。"""
    assert funllmchat is not None


def test_version_matches_pyproject():
    """`__version__` 要和 pyproject.toml 里声明的版本号一致，避免发布时漏改。"""
    pyproject_path = Path(__file__).resolve().parent.parent / "pyproject.toml"
    with pyproject_path.open("rb") as f:
        data = tomllib.load(f)

    assert funllmchat.__version__ == data["project"]["version"]
