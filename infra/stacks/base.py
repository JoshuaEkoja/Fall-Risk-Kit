from __future__ import annotations
import os
from typing import Dict
from aws_cdk import (
    Stack,
    Tags,
)
from constructs import Construct


def default_tags() -> Dict[str, str]:
    """Derive default tags from environment variables with sensible fallbacks.

    Recognized env vars:
    - PROJECT_NAME (default: FallRiskKit)
    - ENV (default: dev)
    - OWNER (default: unknown)
    - OWNER_EMAIL (optional)
    - INSTITUTION (optional)
    - COST_CENTER (optional)
    """
    tags = {
        "Project": os.environ.get("PROJECT_NAME", "FallRiskKit"),
        "Environment": os.environ.get("ENV", "dev"),
        "Owner": os.environ.get("OWNER", "unknown"),
    }
    owner_email = os.environ.get("OWNER_EMAIL")
    if owner_email:
        tags["OwnerEmail"] = owner_email
    institution = os.environ.get("INSTITUTION")
    if institution:
        tags["Institution"] = institution
    cc = os.environ.get("COST_CENTER")
    if cc:
        tags["CostCenter"] = cc
    return tags


class BaseStack(Stack):
    """Base CDK Stack that applies org-wide tags and common options."""

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        for k, v in default_tags().items():
            Tags.of(self).add(k, v)
