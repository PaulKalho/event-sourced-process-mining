from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SERVICES_HOST: str = "localhost"
    TASKS_PORT: int = 3004
    PROPERTY_PORT: int = 3005

    EVENTSTORE_HOST: str = "localhost"
    EVENTSTORE_PORT: int = 2113
    PROJECTION_NAME: str = "getAllEventsByPatientWithPatient"
    OC_PROJECTION_NAME: str = "getObjectCentricEventLog"
    OC_ENHANCED_PROJECTION_NAME: str = "getObjectCentricEventLogEnhanced"

    PROJECTIONS_OUTPUT_DIR: str = "output/projections"
    EVENT_LOG_OUTPUT_DIR: str = "output/event_logs"

    LOG_LEVEL: str = "DEBUG"


ENV = Settings(_env_file=".env", _env_file_encoding="utf-8")
