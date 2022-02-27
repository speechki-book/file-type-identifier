from fti.file_type_getters.get_by_content_disposition import get_file_types_by_content_disposition
from fti.file_types import FileTypes


def test_get_file_types_by_content_disposition():
    input_mime = 'form-data; name="field1"'
    expected_result = set()

    result = get_file_types_by_content_disposition(input_mime)

    assert result == expected_result


def test_get_file_types_by_content_disposition_2():
    input_mime = 'form-data; name="field2"; filename="example.pdf"'
    expected_result = {FileTypes.PDF}

    result = get_file_types_by_content_disposition(input_mime)

    assert result == expected_result


def test_get_file_types_by_content_disposition_3():
    input_mime = 'form-data; name="field2"; filename="example"'
    expected_result = set()

    result = get_file_types_by_content_disposition(input_mime)

    assert result == expected_result


def test_get_file_types_by_content_disposition_4():
    input_mime = 'form-data; name="field2"; filename="example.unknown"'
    expected_result = set()

    result = get_file_types_by_content_disposition(input_mime)

    assert result == expected_result
