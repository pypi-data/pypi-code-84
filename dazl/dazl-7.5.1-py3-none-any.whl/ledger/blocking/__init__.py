# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
:mod:`dazl.ledger.blocking`
===========================

Thread-blocking protocols and base classes for connecting to a Daml ledger.

.. autoclass:: Connection()

.. autoclass:: QueryStream()
"""

import sys

from .. import Connection as _Connection, QueryStream as _QueryStream

if sys.version_info >= (3, 8):
    from typing import Protocol, runtime_checkable
else:
    from typing_extensions import Protocol, runtime_checkable


__all__ = ["Connection", "QueryStream"]


@runtime_checkable
class Connection(_Connection, Protocol):
    """
    Protocol that describes the interface for a blocking connection to a Daml ledger. The methods of
    an implementation should be thread-safe, with the exception of :meth:`open` and :meth:`close`.

    Since ``dazl`` activity is typically dominated by I/O, using a blocking :class:`Connection` with
    multiple threads is usually more expensive than using connections. You should consider
    using the asyncio variant of this API (:class:`dazl.ledger.aio.Connection`) instead.
    """

    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError


@runtime_checkable
class QueryStream(_QueryStream, Protocol):
    """
    A blocking stream of offsets and events from a Daml ledger.
    """

    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError
