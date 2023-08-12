import os
from urllib.parse import unquote, urlsplit


def get_extension_from_url(url: str) -> str | None:
    """
    >>> get_extension_from_url('https://example.com/txt/hello%20world.txt?v=9#python')
    '.txt'
    >>> get_extension_from_url('https://example.com/txt/hello.png')
    '.png'
    >>> get_extension_from_url('/txt/hello.png')
    '.png'
    >>> get_extension_from_url('https://example.com/txt/hello') is None
    True
    """
    uri_path_unquoted = unquote(urlsplit(url).path)
    _, filename = os.path.split(uri_path_unquoted)
    _, ext = os.path.splitext(filename)
    return ext if ext != '' else None
