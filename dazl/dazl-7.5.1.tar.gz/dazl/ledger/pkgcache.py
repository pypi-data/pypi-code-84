# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from ..damlast.lookup import MultiPackageLookup

__all__ = ["SHARED_PACKAGE_DATABASE"]

SHARED_PACKAGE_DATABASE = MultiPackageLookup()
