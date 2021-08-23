#!/usr/bin/env python3
"""
API authentication module
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if API routes require authentication """
        return False

    def authorization_header(self, request=None) -> str:
        """ Checks if Authorization request header is present
        & contains values """
        return None
        
    def current_user(self, request=None) -> TypeVar('User'):
        """ placeholder """
        return None