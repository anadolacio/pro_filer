from pro_filer.actions.main_actions import show_details  # NOQA
import pytest
import os
from datetime import date


def test_show_details(tmp_path, capsys):
    file_path = tmp_path / "test.pdf"
    with open(file_path, "w") as file:
        file.write("test_file")

    context = {"base_path": str(file_path)}
    expected_result = f"""File name: test.pdf
File size in bytes: {os.path.getsize(file_path)}
File type: file
File extension: .pdf
Last modified date: {date.fromtimestamp(os.path.getmtime(file_path))}\n"""

    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == expected_result


def test_show_details_no_extension(tmp_path, capsys):
    file_path = tmp_path / "test"
    with open(file_path, "w") as file:
        file.write("test_file")

    context = {"base_path": str(file_path)}
    expected_result = f"""File name: test
File size in bytes: {os.path.getsize(file_path)}
File type: file
File extension: [no extension]
Last modified date: {date.fromtimestamp(os.path.getmtime(file_path))}\n"""

    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == expected_result


@pytest.mark.parametrize(
    "context, expected_result",
    [
        #         (
        #             {"base_path": "/home/oem/Documentos/Trybe/package.json"},
        #             """File name: package.json
        # File size in bytes: 61
        # File type: file
        # File extension: .json
        # Last modified date: 2022-12-12\n""",
        #         ),
        #         (
        #             {"base_path": "/home/oem/Documentos/Trybe"},
        #             """File name: Trybe
        # File size in bytes: 4096
        # File type: directory
        # File extension: [no extension]
        # Last modified date: 2023-06-25\n""",
        #         ),
        ({"base_path": "/home/trybe/????"}, "File '????' does not exist\n"),
    ],
)
def test_show_details_file_nonexisting(context, expected_result, capsys):
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == expected_result


@pytest.mark.parametrize(
    "context, expected_result",
    [
        (
            {},
            KeyError,
        ),
        (
            {"base_path": 123},
            AttributeError,
        ),
    ],
)
def test_show_details_fails(context, expected_result):
    with pytest.raises(expected_result):
        show_details(context)
