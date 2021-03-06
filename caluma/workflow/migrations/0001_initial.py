# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-12 12:43
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import localized_fields.fields.field
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [("form", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Case",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by_user",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "created_by_group",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            (
                                "running",
                                "Case is running and work items need to be completed.",
                            ),
                            ("completed", "Case is done."),
                            ("canceled", "Case is cancelled."),
                        ],
                        db_index=True,
                        max_length=50,
                    ),
                ),
                ("meta", django.contrib.postgres.fields.jsonb.JSONField(default={})),
                (
                    "document",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="cases",
                        to="form.Document",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="Flow",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by_user",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "created_by_group",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("next", models.TextField()),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by_user",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "created_by_group",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                ("slug", models.SlugField(primary_key=True, serialize=False)),
                ("name", localized_fields.fields.field.LocalizedField(required=[])),
                (
                    "description",
                    localized_fields.fields.field.LocalizedField(
                        blank=True, null=True, required=[]
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("simple", "Task which can only be marked as completed.")
                        ],
                        max_length=50,
                    ),
                ),
                ("meta", django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ("is_archived", models.BooleanField(default=False)),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="TaskFlow",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by_user",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "created_by_group",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "flow",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="task_flows",
                        to="workflow.Flow",
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="task_flows",
                        to="workflow.Task",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Workflow",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by_user",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "created_by_group",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                ("slug", models.SlugField(primary_key=True, serialize=False)),
                ("name", localized_fields.fields.field.LocalizedField(required=[])),
                (
                    "description",
                    localized_fields.fields.field.LocalizedField(
                        blank=True, null=True, required=[]
                    ),
                ),
                ("meta", django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ("is_published", models.BooleanField(default=False)),
                ("is_archived", models.BooleanField(default=False)),
                (
                    "form",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="workflows",
                        to="form.Form",
                    ),
                ),
                (
                    "start",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="workflow.Task",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="WorkItem",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by_user",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "created_by_group",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("ready", "Task is ready to be processed."),
                            ("completed", "Task is done."),
                            ("canceled", "Task is cancelled."),
                        ],
                        db_index=True,
                        max_length=50,
                    ),
                ),
                ("meta", django.contrib.postgres.fields.jsonb.JSONField(default={})),
                (
                    "case",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="work_items",
                        to="workflow.Case",
                    ),
                ),
                (
                    "child_case",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="parent_work_item",
                        to="workflow.Case",
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="work_items",
                        to="workflow.Task",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.AddField(
            model_name="taskflow",
            name="workflow",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="task_flows",
                to="workflow.Workflow",
            ),
        ),
        migrations.AddField(
            model_name="case",
            name="workflow",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="cases",
                to="workflow.Workflow",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="taskflow", unique_together=set([("workflow", "task")])
        ),
    ]
