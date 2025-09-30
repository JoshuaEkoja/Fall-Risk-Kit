from constructs import Construct
from .base import BaseStack


class EmbeddingsAndRagStack(BaseStack):
    """Search & retrieval augmented generation (RAG).

    Key components (AWS): Bedrock/SageMaker, OpenSearch.
    Purpose: Run embeddings jobs and index vectors for semantic search.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.template_options.description = "Embeddings + RAG: vector store and embedding pipelines (skeleton)"
        # TODO: Define vector index (OpenSearch), embedding jobs (Bedrock/SageMaker), ingestion pipelines.
