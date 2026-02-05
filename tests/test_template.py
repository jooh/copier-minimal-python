"""Integration tests for the copier template."""

import subprocess
import tempfile
from pathlib import Path


def test_template_generates_with_defaults():
    """Test that the template generates successfully with default values."""
    template_dir = Path(__file__).parent.parent

    with tempfile.TemporaryDirectory() as tmpdir:
        dest = Path(tmpdir) / "test-project"

        result = subprocess.run(
            [
                "uv",
                "run",
                "copier",
                "copy",
                "--defaults",
                "--trust",
                "--data",
                "project_name=test-project",
                "--data",
                "description=A test project",
                "--data",
                "author_name=Test Author",
                "--data",
                "repo_owner=test-owner",
                str(template_dir),
                str(dest),
            ],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0, f"copier failed: {result.stderr}"
        assert dest.exists(), "Destination directory was not created"
        assert (dest / "pyproject.toml").exists(), "pyproject.toml was not generated"
        assert (dest / "src" / "test_project").exists(), "Package directory was not created"
