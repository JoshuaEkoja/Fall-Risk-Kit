import os
from aws_cdk import App, Environment
from stacks import (
    CoreFoundationStack,
    NetworkBaselineStack,
    KmsSecretsSsmStack,
    ComplianceGuardrailsStack,
    ObservabilityStack,
    CostGovernanceStack,
    BackupDrStack,
    BudgetGuardrailsStack,
    IotCoreFleetStack,
    IotIngestionRulesStack,
    StreamProcessingStack,
    TimeseriesDbStack,
    DataLakeCoreStack,
    EtlOrchestrationStack,
    FhirHealthlakeStack,
    FhirTransformGatewayStack,
    InteropApisStack,
    EmbeddingsAndRagStack,
    FeatureStoreMlopsStack,
    AnalyticsWarehouseStack,
    QuicksightDashboardsStack,
    AppServicesStack,
    EventsBusStack,
    WorkflowsStack,
    NotificationsStack,
    CognitoAuthStack,
    PartnerAccessStack,
    FrontendEdgeStack,
    DocsPortalStack,
    CicdPipelineStack,
    EcrRepositoriesStack,
    ArtifactsBucketStack,
    GovernedDatasetsStack,
    MetadataConfigStack,
    VeevaAuthenticateStack,
    VeevaIntegrationStack,
    EgressControlsStack,
    DeviceSimulatorStack,
    SandboxDataStack,
)


app = App()
# Default environment: region us-east-1 per project preference
env = Environment(
    account=os.environ.get("CDK_DEFAULT_ACCOUNT"),
    region=os.environ.get("CDK_DEFAULT_REGION") or "us-east-1",
)

# Prioritized stacks with minimal resources
events_bus = EventsBusStack(app, "EventsBusStack", env=env, bus_name="frk-bus")

# S3 data lake buckets with prefix
lake = DataLakeCoreStack(app, "DataLakeCoreStack", env=env, bucket_prefix="frk")

# Step Functions placeholder
etl = EtlOrchestrationStack(app, "EtlOrchestrationStack", env=env, state_machine_name="frk-etl")

# Observability basics
obs = ObservabilityStack(app, "ObservabilityStack", env=env, log_group_name="/frk/app")

# Remaining stack skeletons
core = CoreFoundationStack(app, "CoreFoundationStack", env=env)
net = NetworkBaselineStack(app, "NetworkBaselineStack", env=env)
secrets = KmsSecretsSsmStack(app, "KmsSecretsSsmStack", env=env)
comp = ComplianceGuardrailsStack(app, "ComplianceGuardrailsStack", env=env)
cost = CostGovernanceStack(app, "CostGovernanceStack", env=env)
backup = BackupDrStack(app, "BackupDrStack", env=env)
budget = BudgetGuardrailsStack(app, "BudgetGuardrailsStack", env=env)
iot_fleet = IotCoreFleetStack(app, "IotCoreFleetStack", env=env)
iot_rules = IotIngestionRulesStack(app, "IotIngestionRulesStack", env=env)
stream = StreamProcessingStack(app, "StreamProcessingStack", env=env)

timestream = TimeseriesDbStack(app, "TimeseriesDbStack", env=env)
fhir_store = FhirHealthlakeStack(app, "FhirHealthlakeStack", env=env)
fhir_gw = FhirTransformGatewayStack(app, "FhirTransformGatewayStack", env=env)
interop = InteropApisStack(app, "InteropApisStack", env=env)
emb = EmbeddingsAndRagStack(app, "EmbeddingsAndRagStack", env=env)
features = FeatureStoreMlopsStack(app, "FeatureStoreMlopsStack", env=env)
warehouse = AnalyticsWarehouseStack(app, "AnalyticsWarehouseStack", env=env)
qs = QuicksightDashboardsStack(app, "QuicksightDashboardsStack", env=env)
apps = AppServicesStack(app, "AppServicesStack", env=env)
flows = WorkflowsStack(app, "WorkflowsStack", env=env)
notify = NotificationsStack(app, "NotificationsStack", env=env)
cognito = CognitoAuthStack(app, "CognitoAuthStack", env=env)
partners = PartnerAccessStack(app, "PartnerAccessStack", env=env)
edge = FrontendEdgeStack(app, "FrontendEdgeStack", env=env)
docs = DocsPortalStack(app, "DocsPortalStack", env=env)
ci = CicdPipelineStack(app, "CicdPipelineStack", env=env)
ecr = EcrRepositoriesStack(app, "EcrRepositoriesStack", env=env)
artifacts = ArtifactsBucketStack(app, "ArtifactsBucketStack", env=env)
governed = GovernedDatasetsStack(app, "GovernedDatasetsStack", env=env)
meta = MetadataConfigStack(app, "MetadataConfigStack", env=env)
veeva_auth = VeevaAuthenticateStack(app, "VeevaAuthenticateStack", env=env)
veeva_int = VeevaIntegrationStack(app, "VeevaIntegrationStack", env=env)
egress = EgressControlsStack(app, "EgressControlsStack", env=env)
sim = DeviceSimulatorStack(app, "DeviceSimulatorStack", env=env)
sandbox = SandboxDataStack(app, "SandboxDataStack", env=env)

app.synth()
