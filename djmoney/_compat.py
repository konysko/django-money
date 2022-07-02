# flake8: noqa
"""
This module isolates code that has to do with compatibility issues between
different supported versions of Python or other dependencies.

This is quite important to keep the codebase clean.

Please do not catch ImportError exceptions other places than here :)
"""
import typing
from typing import Type, TypeVar


if typing.TYPE_CHECKING:
    from django.db import models

    T = TypeVar("T", bound=models.Model, covariant=True)


def setup_managers(sender: "Type[T]") -> None:
    from .models.managers import money_manager

    default_manager_name = sender._meta.default_manager_name or "objects"
    for manager in filter(lambda m: m.name == default_manager_name, sender._meta.local_managers):
        money_manager(manager)
