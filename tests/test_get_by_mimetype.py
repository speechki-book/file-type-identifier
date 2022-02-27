from fti import FileTypes
from fti.file_type_getters import get_file_types_by_mime


def test_get_file_types_by_mime():
    input_mime = "audio/x-aiff"
    expected_result = {FileTypes.AIF, FileTypes.AIFC, FileTypes.AIFF}

    result = get_file_types_by_mime(input_mime)

    assert result == expected_result
