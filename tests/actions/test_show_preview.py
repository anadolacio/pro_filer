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
        (
            {
                "all_files": [
                    "src",
                    "app.py",
                    "app2.py",
                    "app3.py",
                    "app4.py",
                    "src/app5.py",
                ],
                "all_dirs": ["src", "src/utils"],
            },
            """Found 6 files and 2 directories
First 5 files: ['src', 'app.py', 'app2.py', 'app3.py', 'app4.py']
First 5 directories: ['src', 'src/utils']\n""",
        ),
    ],
)
def test_show_preview(context, expected_result, capsys):
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expected_result


@pytest.mark.parametrize(
    "context, expected_result",
    [
        ({"all_dirs": []}, KeyError),
        ({"all_files": []}, KeyError),
        ({}, KeyError),
    ],
)
def test_show_preview_response_fail(context, expected_result):
    with pytest.raises(expected_result):
        show_preview(context)
