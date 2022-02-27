from fti.file_type_getters.get_by_content_header import get_file_types_by_content
from fti.file_types import FileTypes


def test_get_file_types_by_content():
    input_bytes = b"\x66\x74\x79\x70\x33\x67"
    expected_result = {FileTypes._3G2, FileTypes._3GP}

    result = get_file_types_by_content(input_bytes)

    assert result == expected_result


def test_get_file_types_by_content_2():
    input_bytes = b"\x00\x01"
    expected_result = {FileTypes.PIC, FileTypes.PIF, FileTypes.SEA, FileTypes.YTR}

    result = get_file_types_by_content(input_bytes)

    assert result == expected_result
