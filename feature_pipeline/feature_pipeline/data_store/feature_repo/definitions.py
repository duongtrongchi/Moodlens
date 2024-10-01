from feast import FeatureStore, Entity, FeatureView, FeatureService, FileSource, Field
from feast.types import Float32, String


# Define entity (the unique identifier for the feature)
entity = Entity(
    name="employees_reviews", 
    join_keys=["id"]  
)


# Define data source
job_details_data_source = FileSource(
    path="/teamspace/studios/this_studio/nlp-hr-feedback/feature_pipeline/feature_pipeline/data_store/feature_repo/data/job_details.parquet",
    event_timestamp_column="event_timestamp"  
)

# Define the feature view
job_details_feature_view = FeatureView(
    name="job_details",
    entities=[entity],  # Fix: pass the Entity object, not the string "id"
    ttl=None,  # Optionally set a time-to-live (TTL) value if needed
    schema=[
        Field(name="Title", dtype=String),
        Field(name="Place", dtype=String),
        Field(name="Job_type", dtype=String),
        Field(name="Department", dtype=String),
    ],
    online=True,
    source=job_details_data_source
)


job_evaluation_data_source = FileSource(
    path="/teamspace/studios/this_studio/nlp-hr-feedback/feature_pipeline/feature_pipeline/data_store/feature_repo/data/job_evaluation.parquet",
    event_timestamp_column="event_timestamp"
)

job_evaluation_feature_view = FeatureView(
    name="job_evaluation",
    entities=[entity],  # Fix: pass the Entity object, not the string "id"
    ttl=None,  # Optionally set a time-to-live (TTL) value if needed
    schema=[
        Field(name="Overall_rating", dtype=Float32),
        Field(name="work_satisfaction", dtype=Float32),
        Field(name="Likes", dtype=String),
        Field(name="Dislikes", dtype=String),
    ],
    online=True,
    source=job_evaluation_data_source
)


work_life_data_source = FileSource(
    path="/teamspace/studios/this_studio/nlp-hr-feedback/feature_pipeline/feature_pipeline/data_store/feature_repo/data/work_life.parquet",
    event_timestamp_column="event_timestamp"
)

work_life_feature_view = FeatureView(
    name="work_life",
    entities=[entity],  # Fix: pass the Entity object, not the string "id"
    ttl=None,  # Optionally set a time-to-live (TTL) value if needed
    schema=[
        Field(name="work_life_balance", dtype=Float32),
        Field(name="career_growth", dtype=Float32),
    ],
    online=True,
    source=work_life_data_source
)


financial_aspects_data_source = FileSource(
    path="/teamspace/studios/this_studio/nlp-hr-feedback/feature_pipeline/feature_pipeline/data_store/feature_repo/data/financial_aspects.parquet",
    event_timestamp_column="event_timestamp"
)

financial_aspects_feature_view = FeatureView(
    name="financial_aspects",
    entities=[entity],  # Fix: pass the Entity object, not the string "id"
    ttl=None,  # Optionally set a time-to-live (TTL) value if needed
    schema=[
        Field(name="skill_development", dtype=Float32),
        Field(name="salary_and_benefits", dtype=Float32),
        Field(name="job_security", dtype=Float32),
    ],
    online=True,
    source=financial_aspects_data_source
)


moodlens = FeatureService(
    name="moodlens_features",
    features=[job_evaluation_feature_view, financial_aspects_feature_view]
)


store = FeatureStore(repo_path=".")