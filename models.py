from pydantic import BaseModel
from datetime import datetime

# Implement a Pydantic model for notes
class Note(BaseModel):
    title: str
    content: str
    created_at: datetime = datetime.now()
