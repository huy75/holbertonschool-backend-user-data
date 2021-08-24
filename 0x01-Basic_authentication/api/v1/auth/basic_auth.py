#!/usr/bin/env python3
"""
Basic API authentication module
"""

from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ Basic Authentication """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Returns Base64 part of Authorization header """
        if authorization_header and isinstance(
                authorization_header,
                str) and authorization_header.startswith("Basic "):
            return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Returns decoded value of base64_authorization_header"""
        if base64_authorization_header is None:
            return None
        elif not isinstance(base64_authorization_header, str):
            return None
        try:
            if b64encode(
                    b64decode(base64_authorization_header)
            ) == base64_authorization_header:
                pass
        except Exception:
            return None
        decoded_string = b64decode(base64_authorization_header)
        return decoded_string.decode('utf-8')
