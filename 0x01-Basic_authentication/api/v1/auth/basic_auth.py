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
            self, base64_auth_header: str) -> str:
        """ Returns decoded value of Base64 str """
        if base64_auth_header and isinstance(
                base64_auth_header, str):
            try:
                encoded = base64_auth_header.encode('utf-8')
                base = base64.b64decode(encoded)
                return base.decode('utf-8')
            except binascii.Error:
                return None
