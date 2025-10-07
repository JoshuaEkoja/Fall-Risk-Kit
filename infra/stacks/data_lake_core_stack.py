from aws_cdk import aws_s3 as s3
from constructs import Construct
from .base import BaseStack


class DataLakeCoreStack(BaseStack):
    """Governed data lake core (zones and storage).

    Key components (AWS): S3 buckets for raw, clean, curated. (Glue/Lake Formation later.)
    Purpose: Multi-zone data lake architecture for all incoming data.
    """

    def __init__(self, scope: Construct, construct_id: str, *, bucket_prefix: str = "frk", **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.template_options.description = (
            "Data lake core: S3 zones (raw, clean, curated) with encryption and versioning"
        )
        # Buckets with S3-managed encryption and versioning as a secure default
        self.raw_bucket = s3.Bucket(
            self,
            "RawBucket",
            bucket_name=f"{bucket_prefix}-raw",
            encryption=s3.BucketEncryption.S3_MANAGED,
            versioned=True,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            enforce_ssl=True,
            object_ownership=s3.ObjectOwnership.BUCKET_OWNER_ENFORCED,
        )
        self.clean_bucket = s3.Bucket(
            self,
            "CleanBucket",
            bucket_name=f"{bucket_prefix}-clean",
            encryption=s3.BucketEncryption.S3_MANAGED,
            versioned=True,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            enforce_ssl=True,
            object_ownership=s3.ObjectOwnership.BUCKET_OWNER_ENFORCED,
        )
        self.curated_bucket = s3.Bucket(
            self,
            "CuratedBucket",
            bucket_name=f"{bucket_prefix}-curated",
            encryption=s3.BucketEncryption.S3_MANAGED,
            versioned=True,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            enforce_ssl=True,
            object_ownership=s3.ObjectOwnership.BUCKET_OWNER_ENFORCED,
        )
        # TODO: Add Glue databases/crawlers and Lake Formation governance.
