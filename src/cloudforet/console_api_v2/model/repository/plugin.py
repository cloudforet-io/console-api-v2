from pydantic import BaseModel, Field
from typing import Union
from datetime import datetime


# Base Model

class Plugin(BaseModel):
    plugin_id: Union[str, None] = Field(None)
    name: Union[str, None] = Field(None)
    state: Union[str, None] = Field(None)
    image: Union[str, None] = Field(None)
    register_type: Union[str, None] = Field(None)
    registry_url: Union[str, None] = Field(None)
    registry_config: Union[dict, None] = Field(None)
    service_type: Union[str, None] = Field(None)
    provider: Union[str, None] = Field(None)
    capability: Union[dict, None] = Field(None)
    template: Union[dict, None] = Field(None)
    repository_info: Union[dict, None] = Field(None)
    domain_id: Union[str, None] = Field(None)
    project_id: Union[str, None] = Field(None)
    labels: Union[list, None] = Field(None)
    tags: Union[dict, None] = Field(None)
    created_at: Union[datetime, None] = Field(None)

# PluginInfo model
class PluginInfo(Plugin):
    class Register(BaseModel):
        name: str = Field(...)
        service_type: str = Field(...)
        image: str = Field(...)
        register_type: Union[str, None] = Field(None)
        registry_config: Union[dict, None] = Field(None)
        provider: Union[str, None] = Field(None)
        capability: Union[dict, None] = Field(None)
        template: Union[dict, None] = Field(None)
        project_id: Union[str, None] = Field(None)
        labels: Union[list, None] = Field(None)
        tags: Union[dict, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

    class Update(BaseModel):
        plugin_id: str = Field(...)
        name: Union[str, None] = Field(None)
        capability: Union[dict, None] = Field(None)
        labels: Union[list, None] = Field(None)
        tags: Union[dict, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

    class Enable(BaseModel):
        plugin_id: str = Field(...)
        domain_id: Union[str, None] = Field(None)

    class Disable(BaseModel):
        plugin_id: str = Field(...)
        domain_id: Union[str, None] = Field(None)

    class Deregister(BaseModel):
        plugin_id: str = Field(...)
        domain_id: Union[str, None] = Field(None)

    class GetVersions(BaseModel):
        plugin_id: str = Field(...)
        repository_id: Union[str, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

    class Get(BaseModel):
        plugin_id: str = Field(...)
        repository_id: Union[str, None] = Field(None)
        only: Union[list, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

    class List(BaseModel):
        repository_id: str = Field(...)
        plugin_id: Union[str, None] = Field(None)
        name: Union[str, None] = Field(None)
        state: Union[str, None] = Field(None)
        service_type: Union[str, None] = Field(None)
        provider: Union[str, None] = Field(None)
        project_id: Union[str, None] = Field(None)
        register_type: Union[str, None] = Field(None)
        labels: Union[list, None] = Field(None)
        query: Union[dict, None] = Field(None)
        domain_id: Union[str, None] = Field(None)

    class Stat(BaseModel):
        repository_id: str = Field(...)
        query: dict = Field(...)
        domain_id: Union[str, None] = Field(None)
