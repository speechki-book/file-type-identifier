import httpx

from file_type_getters import (
    get_file_types_by_content,
    get_file_types_by_content_disposition,
    get_file_types_by_mime,
    get_file_types_by_url,
)
from file_types import FileTypes


def get_file_types(url: str) -> set[FileTypes]:
    if result := get_file_types_by_url(url):
        return result

    with httpx.stream("GET", url) as response:
        content_disposition = response.headers.get("content-disposition")
        if content_disposition and (result := get_file_types_by_content_disposition(content_disposition)):
            return result

        content_type = response.headers.get("content-type")
        if content_type and (result := get_file_types_by_mime(content_type)):
            return result

        content = next(response.iter_bytes(64))

        if result := get_file_types_by_content(content):
            return result

    return set()


async def get_file_types_async(url: str) -> set[FileTypes]:
    if result := get_file_types_by_url(url):
        return result

    client = httpx.AsyncClient()
    async with client.stream("GET", url) as response:
        content_disposition = response.headers.get("content-disposition")
        if content_disposition and (result := get_file_types_by_content_disposition(content_disposition)):
            return result

        content_type = response.headers.get("content-type")
        if content_type and (result := get_file_types_by_mime(content_type)):
            return result

        content = await response.aiter_bytes(64).__anext__()

        if result := get_file_types_by_content(content):
            return result

    return set()
