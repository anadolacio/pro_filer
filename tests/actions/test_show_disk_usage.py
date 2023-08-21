from pro_filer.actions.main_actions import show_disk_usage  # NOQA
import pytest


@pytest.mark.parametrize(
    "context, expected_result",
    [
        (
            {
                "all_files": [
                    "src/app.py",
                    "src/__init__.py",
                ]
            },
            """'src/app.py': 2849 (100%)
'src/__init__.py': 0 (0%)
Total size: 2849\n""",
        ),
        (
            {"all_files": []},
            "Total size: 0\n",
        ),
    ],
)
def test_show_disk_usage(
    monkeypatch, temp_path, context, expected_result, capsys
):
    mock = temp_path / "test.txt"
    monkeypatch.setattr("pro_filer/actions/main_actions.py", mock)
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert captured.out == expected_result
