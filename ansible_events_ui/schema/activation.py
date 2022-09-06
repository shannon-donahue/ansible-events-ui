from datetime import datetime
from typing import Optional

from pydantic import BaseModel, StrictStr

from ansible_events_ui.schema.extra_vars import ExtravarsRef
from ansible_events_ui.schema.inventory import InventoryRef
from ansible_events_ui.schema.playbook import PlaybookRef
from ansible_events_ui.schema.rulebook import RulebookRef


class RestartPolicy(BaseModel):
    id: int
    name: StrictStr


class Activation(BaseModel):
    id: Optional[int]
    name: StrictStr
    description: Optional[StrictStr]
    execution_env_id: int
    rulebook_id: int
    inventory_id: int
    restart_policy_id: int
    playbook_id: int
    activation_enabled: bool
    extra_var_id: int


class ActivationCreate(BaseModel):
    name: StrictStr
    description: Optional[StrictStr]
    rulebook_id: int
    inventory_id: int
    restart_policy_id: int
    playbook_id: int
    activation_enabled: bool
    extra_var_id: int
    working_directory: StrictStr
    execution_environment: StrictStr


class ActivationBaseRead(ActivationCreate):
    id: int


class ActivationRead(BaseModel):
    id: int
    name: StrictStr
    description: Optional[StrictStr]
    status: Optional[StrictStr]
    is_enabled: bool
    working_directory: StrictStr
    execution_environment: StrictStr
    rulebook: RulebookRef
    inventory: InventoryRef
    extra_var: ExtravarsRef
    playbook: PlaybookRef
    restart_policy: RestartPolicy
    restarted_at: Optional[datetime]
    restart_count: int
    created_at: datetime
    modified_at: datetime


class ActivationUpdate(BaseModel):
    name: StrictStr
    description: Optional[StrictStr]
    activation_enabled: bool


class ActivationInstance(BaseModel):
    id: Optional[int]
    name: StrictStr
    rulebook_id: int
    inventory_id: int
    extra_var_id: int
    working_directory: StrictStr
    execution_environment: StrictStr


class ActivationLog(BaseModel):
    activation_instance_id: int
    log: StrictStr
    id: Optional[int]
