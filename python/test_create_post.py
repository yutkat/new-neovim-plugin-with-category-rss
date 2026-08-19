import pathlib
import subprocess
import sys

SCRIPT = pathlib.Path(__file__).parent / "create_post.py"


def run(cwd: pathlib.Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "foo/bar.nvim", "Cat > Sub"],
        cwd=cwd,
        capture_output=True,
        text=True,
    )


def test_creates_post_for_new_repo(tmp_path: pathlib.Path) -> None:
    (tmp_path / "_posts").mkdir()

    result = run(tmp_path)

    assert result.returncode == 0
    assert "Add: foo/bar.nvim" in result.stdout
    assert list((tmp_path / "_posts").glob("????-??-??-foo--bar.nvim.html"))


def test_skips_existing_post_with_exit_code_zero(tmp_path: pathlib.Path) -> None:
    posts = tmp_path / "_posts"
    posts.mkdir()
    (posts / "2024-09-16-foo--bar.nvim.html").write_text("existing")

    result = run(tmp_path)

    assert result.returncode == 0
    assert "Skip: foo/bar.nvim" in result.stdout
    assert (posts / "2024-09-16-foo--bar.nvim.html").read_text() == "existing"
