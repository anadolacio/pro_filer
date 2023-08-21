from pro_filer.actions.main_actions import show_preview  # NOQA
import pytest


@pytest.mark.parametrize(
    "context, expected_result",
    [
        (
            {
                "all_files": [
                    "src/__init__.py",
                    "src/app.py",
                    "src/utils/__init__.py",
                ],
                "all_dirs": ["src", "src/utils"],
            },
            """Found 3 files and 2 directories
First 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']
First 5 directories: ['src', 'src/utils']\n""",
        ),
        (
            {"all_files": [], "all_dirs": []},
            "Found 0 files and 0 directories\n",
        ),
    ],
)
def test_show_preview(context, expected_result, capsys):
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expected_result
