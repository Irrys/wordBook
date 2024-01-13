from pydantic import BaseModel, validator
import datetime


class Words(BaseModel):
    word: str


class WordUpdate(BaseModel):
    level: int | None = None
    review_time: datetime.datetime | None = None

    @validator('level', always=True)
    def validate_level(cls, v):
        if v > 6 or v < 0:
            raise ValueError('level must between 0 to 6')
        return v

    @validator('review_time', always=True)
    def validate_review_time(cls, v):
        if not v:
            return v
        if not isinstance(v, datetime.datetime):
            raise ValueError('review time must be a datetime object')
        return v

    def to_dict(self):
        return {field: self.__dict__[field] for field in self.__fields_set__}
