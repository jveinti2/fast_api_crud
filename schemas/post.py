
# post model
from datetime import datetime
from typing import Optional
from uuid import uuid4
from pydantic import BaseModel, Field


class Post(BaseModel):
    id: str = uuid4()
    title: str = Field(default='Nombre de la pelicula', min_length=5, max_length=15) 
    content: Optional[str]
    create_at: datetime = datetime.now()   
    