from pro_filer.actions.main_actions import show_details  # NOQA
import pytest


@pytest.mark.parametrize(
    "context, expected_result",
    [
        (
            {"base_path": "/home/trybe/Downloads/Trybe.png"},
            """File name: Trybe.png
File size in bytes: 22438
File type: file
File extension: .png
Last modified date: 2023-06-13\n""",
        ),
        (
            {"base_path": "/home/trybe/????"},
            "File '????' does not exist\n",
        ),
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
