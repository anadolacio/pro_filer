from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest
import os


@pytest.fixture
def context(tmp_path):
    path1 = tmp_path / "test1.txt"
    path1.write_text("Test one")

    path2 = tmp_path / "test2.txt"
    path2.write_text("Test two")

    path3 = tmp_path / "test3.txt"
    path3.write_text("Test three")

    path4 = tmp_path / "test3.txt"
    path4.write_text("Test one")

    path5 = tmp_path / "test3.txt"
    path5.write_text("Test two")
    return {
        "all_files": [
            str(path1),
            str(path2),
            str(path3),
            str(path4),
            str(path5),
        ]
    }


def test_show_usage(context):
    all_files_result = find_duplicate_files(context)
    duplicate_result = [
        (os.path.basename(path1), os.path.basename(path2))
        for path1, path2 in all_files_result
    ]
    expected_result = [
        ("test2.txt", "test3.txt"),
        ("test2.txt", "test3.txt"),
        ("test2.txt", "test3.txt"),
        ("test3.txt", "test3.txt"),
        ("test3.txt", "test3.txt"),
        ("test3.txt", "test3.txt"),
    ]
    assert duplicate_result == expected_result


@pytest.mark.parametrize(
    "context, expected_result",
    [
        (
            {
                "all_files": [
                    ".gitignore",
                    "src/app.py",
                    "src/utils/__init__.py",
                ]
            },
            ValueError,
        ),
    ],
)
def test_show_details_file_nonexisting(context, expected_result):
    with pytest.raises(expected_result):
        find_duplicate_files(context)
