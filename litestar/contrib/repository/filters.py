"""Collection filter datastructures."""
from __future__ import annotations

from collections import abc  # noqa: TCH003
from dataclasses import dataclass
from datetime import datetime  # noqa: TCH003
from typing import Generic, Literal, TypeVar

T = TypeVar("T")

__all__ = ["BeforeAfter", "CollectionFilter", "LimitOffset", "OrderBy", "SearchFilter"]


@dataclass
class BeforeAfter:
    """Data required to filter a query on a ``datetime`` column."""

    field_name: str
    """Name of the model attribute to filter on."""
    before: datetime | None
    """Filter results where field earlier than this."""
    after: datetime | None
    """Filter results where field later than this."""


@dataclass
class CollectionFilter(Generic[T]):
    """Data required to construct a ``WHERE ... IN (...)`` clause."""

    field_name: str
    """Name of the model attribute to filter on."""
    values: abc.Collection[T]
    """Values for ``IN`` clause."""


@dataclass
class LimitOffset:
    """Data required to add limit/offset filtering to a query."""

    limit: int
    """Value for ``LIMIT`` clause of query."""
    offset: int
    """Value for ``OFFSET`` clause of query."""


@dataclass
class OrderBy:
    """Data required to construct a ``ORDER BY ...`` clause."""

    field_name: str
    """Name of the model attribute to sort on."""
    sort_order: Literal["asc", "desc"] = "asc"
    """Sort ascending or descending"""


@dataclass
class SearchFilter:
    """Data required to construct a ``WHERE field_name LIKE '%' || :value || '%'`` clause."""

    field_name: str
    """Name of the model attribute to sort on."""
    value: str
    """Values for ``LIKE`` clause."""
    ignore_case: bool | None = False
    """Should the search be case insensitive."""
