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
        """ Returns decoded value of Base64 str """
         if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded = b64decode(
                base64_authorization_header, validate=True)
            return decoded.decode('utf-8')
        except base64.binascii.Error:
            return None
