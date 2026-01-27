from sqlalchemy import Column, DateTime
from datetime import datetime

### Timepoint pattern ###
class TimePointMixin:
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

