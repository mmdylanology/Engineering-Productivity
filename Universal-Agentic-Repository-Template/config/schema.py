from pydantic import BaseModel, Field

class SystemConfig(BaseModel):
    max_retry_attempts: int = Field(ge=1, le=10)
    timeout_seconds: int = Field(ge=1, le=300)
    rate_limit_per_second: int = Field(ge=1, le=100)

class BusinessConfig(BaseModel):
    default_discount_rate: float = Field(ge=0.0, le=1.0)
    standard_tax_rate: float = Field(ge=0.0, le=0.6)

class RootConfig(BaseModel):
    schema_version: int
    system: SystemConfig
    business: BusinessConfig
