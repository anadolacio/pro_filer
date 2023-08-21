from pro_filer.actions.main_actions import show_details  # NOQA
import pytest


@pytest.mark.parametrize(
    "context, expected_result",
    [
        (
            {"base_path": "/home/oem/Documentos/Trybe/package.json"},
            """File name: package.json
File size in bytes: 61
File type: file
File extension: .json
Last modified date: 2022-12-12\n""",
        ),
        ({"base_path": "/home/trybe/????"}, "File '????' does not exist\n"),
    ],
)
def test_show_details(context, expected_result, capsys):
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
