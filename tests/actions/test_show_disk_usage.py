from pro_filer.actions.main_actions import show_disk_usage  # NOQA
import pytest


@pytest.fixture
def context(tmp_path):
    path1 = tmp_path / "test1.txt"
    path1.write_text("Test one")

    path2 = tmp_path / "test2.txt"
    path2.write_text("Test two")

    path3 = tmp_path / "test3.txt"
    path3.write_text("Test three")
    return {"all_files": [str(path1), str(path2), str(path3)]}


def test_show_usage(context, capsys):
    show_disk_usage(context)
    captured = capsys.readouterr()
    expected_result = captured.out.strip().split("\n")

    assert "test3.txt" in expected_result[0]
    assert "test1.txt" in expected_result[1]
    assert "test2.txt" in expected_result[2]
    assert "Total size: 26" in expected_result[3]
    assert len(expected_result) == 4


@pytest.mark.parametrize(
    "context, expected_result",
    [
        ({"all_files": []}, "Total size: 0\n"),
    ],
)
def test_show_details_file_nonexisting(context, expected_result, capsys):
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert captured.out == expected_result
