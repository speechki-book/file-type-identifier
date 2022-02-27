from fti import FileTypes
from fti.file_type_getters import get_file_types_by_url


def test_get_file_types_by_url():
    input_url = "http://example.com/test_image.jpeg?size=400,300"
    expected_result = {FileTypes.JPEG}

    result = get_file_types_by_url(input_url)

    assert result == expected_result


def test_get_file_types_by_url_2():
    input_url = "http://example.com/"
    expected_result = set()

    result = get_file_types_by_url(input_url)

    assert result == expected_result


def test_get_file_types_by_url_3():
    input_url = "http://example.com/file.unknown"
    expected_result = set()

    result = get_file_types_by_url(input_url)

    assert result == expected_result
