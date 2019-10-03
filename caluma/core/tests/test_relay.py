# SPDX-FileCopyrightText: 2019 Adfinis SyGroup AG
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import pytest

from ..relay import extract_global_id


@pytest.mark.parametrize(
    "id,expected",
    [
        ("slug", "slug"),
        ("V29ya2Zsb3dTcGVjaWZpY2F0aW9uOmxpc3RlbmVpbnRyYWc=", "listeneintrag"),
    ],
)
def test_extract_global_id(id, expected):
    assert extract_global_id(id) == expected
