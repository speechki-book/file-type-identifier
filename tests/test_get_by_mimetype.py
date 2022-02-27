from fti.file_type_getters.get_by_mimetype import get_file_types_by_mime
from fti.file_types import FileTypes


def test_get_file_types_by_mime():
    input_mime = "audio/x-aiff"
    expected_result = {FileTypes.AIF, FileTypes.AIFC, FileTypes.AIFF}

    result = get_file_types_by_mime(input_mime)

    assert result == expected_result
