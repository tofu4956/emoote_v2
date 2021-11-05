from typing import Optional
import datetime

from pydantic import BaseModel, Field

class EntryBase(BaseModel):
  entry:str = Field(None, title="entry")
  