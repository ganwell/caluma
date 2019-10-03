# SPDX-FileCopyrightText: 2019 Adfinis SyGroup AG
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import os

import pytest
from django.conf import settings
from django.core.management import call_command
from django.utils import timezone
from minio import Minio
from simple_history.models import registered_models

from caluma.core.management.commands import cleanup_history

from ..models import Form


def test_create_bucket_command(mocker):
    mocker.patch.object(Minio, "make_bucket")
    call_command("create_bucket", stdout=open(os.devnull, "w"))
    Minio.make_bucket.assert_called_once_with(settings.MINIO_STORAGE_MEDIA_BUCKET_NAME)


@pytest.mark.parametrize("dry", [True, False])
@pytest.mark.parametrize("keep,kept", [("1 year", 2), ("1 day", 1), (None, 0)])
def test_cleanup_history_command(db, dry, keep, kept):
    # we need to override the registered models dict in order to get rid of the
    # fake models created in core tests
    cleanup_history.registered_models = {
        k: v for k, v in registered_models.items() if not k.startswith("core_")
    }
    args = []
    kwargs = {}
    if dry:
        args.append("--dry")
        kept = 3
    if keep:
        kwargs["keep"] = keep

    Form.objects.create(slug="form 1")

    f2 = Form.objects.create(slug="form 2")
    f2_hist = f2.history.first()
    f2_hist.history_date = f2_hist.history_date - timezone.timedelta(days=2)
    f2_hist.save()

    f3 = Form.objects.create(slug="form 3")
    f3_hist = f3.history.first()
    f3_hist.history_date = f3_hist.history_date - timezone.timedelta(days=730)
    f3_hist.save()

    call_command("cleanup_history", *args, **kwargs, stdout=open(os.devnull, "w"))

    assert Form.history.count() == kept
