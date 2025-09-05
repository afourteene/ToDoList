from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional,List
from core.entities.assignee import Assignee


@dataclass
class Task:
    id: int
    subject: str
    desc: Optional[str] = ''
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    status: List[str] = field(default_factory=list)
    assignee: Optional[Assignee] = None 


