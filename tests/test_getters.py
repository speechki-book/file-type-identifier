from unittest.mock import patch, MagicMock, AsyncMock

import pytest

from fti import FileTypes, get_file_types, get_file_types_async


def test_get_file_types_wrong_url():
    input_url = ""

    with pytest.raises(ValueError):
        get_file_types(input_url)


def test_get_file_types_by_url():
    input_url = MagicMock()

    expected_result = {FileTypes._3G2}
    by_url_mock = MagicMock(return_value=expected_result)

    with patch("fti.getters.get_file_types_by_url", by_url_mock):
        result = get_file_types(input_url)

    assert result == expected_result


def test_get_file_types_by_content_disposition():
    input_url = MagicMock()

    by_url_mock = MagicMock(return_value=set())

    httpx_stream_mock = MagicMock()

    expected_result = {FileTypes._3G2}
    by_content_disposition_mock = MagicMock(return_value=expected_result)

    with patch("fti.getters.get_file_types_by_url", by_url_mock), patch(
        "fti.getters.httpx.stream", httpx_stream_mock
    ), patch("fti.getters.get_file_types_by_content_disposition", by_content_disposition_mock):

        result = get_file_types(input_url)

    assert result == expected_result


def test_get_file_types_by_content_type():
    input_url = MagicMock()

    by_url_mock = MagicMock(return_value=set())

    httpx_stream_mock = MagicMock()

    by_content_disposition_mock = MagicMock(return_value=set())

    expected_result = {FileTypes._3G2}
    by_mime_mock = MagicMock(return_value=expected_result)

    with patch("fti.getters.get_file_types_by_url", by_url_mock), patch(
        "fti.getters.httpx.stream", httpx_stream_mock
    ), patch("fti.getters.get_file_types_by_content_disposition", by_content_disposition_mock), patch(
        "fti.getters.get_file_types_by_mime", by_mime_mock
    ):

        result = get_file_types(input_url)

    assert result == expected_result


def test_get_file_type_by_content():
    input_url = MagicMock()

    by_url_mock = MagicMock(return_value=set())

    httpx_stream_mock = MagicMock()

    by_content_disposition_mock = MagicMock(return_value=set())

    by_mime_mock = MagicMock(return_value=set())

    expected_result = {FileTypes._3G2}
    by_content_mock = MagicMock(return_value=expected_result)

    with patch("fti.getters.get_file_types_by_url", by_url_mock), patch(
        "fti.getters.httpx.stream", httpx_stream_mock
    ), patch("fti.getters.get_file_types_by_content_disposition", by_content_disposition_mock), patch(
        "fti.getters.get_file_types_by_mime", by_mime_mock
    ), patch(
        "fti.getters.get_file_types_by_content", by_content_mock
    ):

        result = get_file_types(input_url)

    assert result == expected_result


def test_get_file_type_no_result():
    input_url = MagicMock()

    by_url_mock = MagicMock(return_value=set())

    httpx_stream_mock = MagicMock()

    by_content_disposition_mock = MagicMock(return_value=set())

    by_mime_mock = MagicMock(return_value=set())

    by_content_mock = MagicMock(return_value=set())

    with patch("fti.getters.get_file_types_by_url", by_url_mock), patch(
        "fti.getters.httpx.stream", httpx_stream_mock
    ), patch("fti.getters.get_file_types_by_content_disposition", by_content_disposition_mock), patch(
        "fti.getters.get_file_types_by_mime", by_mime_mock
    ), patch(
        "fti.getters.get_file_types_by_content", by_content_mock
    ):

        result = get_file_types(input_url)

    assert result == set()


@pytest.mark.asyncio
async def test_async_get_file_types_wrong_url():
    input_url = ""

    with pytest.raises(ValueError):
        await get_file_types_async(input_url)


@pytest.mark.asyncio
async def test_async_get_file_types_by_url():
    input_url = MagicMock()

    expected_result = {FileTypes._3G2}
    by_url_mock = MagicMock(return_value=expected_result)

    with patch("fti.getters.get_file_types_by_url", by_url_mock):
        result = await get_file_types_async(input_url)

    assert result == expected_result


@pytest.mark.asyncio
async def test_async_get_file_types_by_content_disposition():
    input_url = MagicMock()

    by_url_mock = MagicMock(return_value=set())

    httpx_client_mock = MagicMock()

    expected_result = {FileTypes._3G2}
    by_content_disposition_mock = MagicMock(return_value=expected_result)

    with patch("fti.getters.get_file_types_by_url", by_url_mock), patch(
        "fti.getters.httpx.AsyncClient", httpx_client_mock
    ), patch("fti.getters.get_file_types_by_content_disposition", by_content_disposition_mock):

        result = await get_file_types_async(input_url)

    assert result == expected_result


@pytest.mark.asyncio
async def test_async_get_file_types_by_content_type():
    input_url = MagicMock()

    by_url_mock = MagicMock(return_value=set())

    httpx_client_mock = MagicMock()

    by_content_disposition_mock = MagicMock(return_value=set())

    expected_result = {FileTypes._3G2}
    by_mime_mock = MagicMock(return_value=expected_result)

    with patch("fti.getters.get_file_types_by_url", by_url_mock), patch(
        "fti.getters.httpx.AsyncClient", httpx_client_mock
    ), patch("fti.getters.get_file_types_by_content_disposition", by_content_disposition_mock), patch(
        "fti.getters.get_file_types_by_mime", by_mime_mock
    ):

        result = await get_file_types_async(input_url)

    assert result == expected_result


@pytest.mark.asyncio
async def test_async_get_file_type_by_content():
    input_url = MagicMock()

    by_url_mock = MagicMock(return_value=set())

    response_mock = MagicMock()
    stream_mock = MagicMock()
    stream_mock.__aenter__ = AsyncMock(return_value=response_mock)
    client_stream_mock = MagicMock()
    client_stream_mock.stream = MagicMock(return_value=stream_mock)
    httpx_client_mock = MagicMock(return_value=client_stream_mock)

    by_content_disposition_mock = MagicMock(return_value=set())

    by_mime_mock = MagicMock(return_value=set())

    expected_result = {FileTypes._3G2}
    by_content_mock = MagicMock(return_value=expected_result)

    with patch("fti.getters.get_file_types_by_url", by_url_mock), patch(
        "fti.getters.httpx.AsyncClient", httpx_client_mock
    ), patch("fti.getters.get_file_types_by_content_disposition", by_content_disposition_mock), patch(
        "fti.getters.get_file_types_by_mime", by_mime_mock
    ), patch(
        "fti.getters.get_file_types_by_content", by_content_mock
    ):

        result = await get_file_types_async(input_url)

    assert result == expected_result


@pytest.mark.asyncio
async def test_async_get_file_type_no_result():
    input_url = MagicMock()

    by_url_mock = MagicMock(return_value=set())

    response_mock = MagicMock()
    stream_mock = MagicMock()
    stream_mock.__aenter__ = AsyncMock(return_value=response_mock)
    client_stream_mock = MagicMock()
    client_stream_mock.stream = MagicMock(return_value=stream_mock)
    httpx_client_mock = MagicMock(return_value=client_stream_mock)

    by_content_disposition_mock = MagicMock(return_value=set())

    by_mime_mock = MagicMock(return_value=set())

    by_content_mock = MagicMock(return_value=set())

    with patch("fti.getters.get_file_types_by_url", by_url_mock), patch(
        "fti.getters.httpx.AsyncClient", httpx_client_mock
    ), patch("fti.getters.get_file_types_by_content_disposition", by_content_disposition_mock), patch(
        "fti.getters.get_file_types_by_mime", by_mime_mock
    ), patch(
        "fti.getters.get_file_types_by_content", by_content_mock
    ):

        result = await get_file_types_async(input_url)

    assert result == set()
