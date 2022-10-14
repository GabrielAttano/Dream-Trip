from pydantic import BaseModel

class PackagesSchema(BaseModel):
    start_date: str
    stay_time: int
    destinations: list
    start_destination: str
    user_id: str

class PackageDTO(BaseModel):
    start_date: str
    stay_time: int
    destinations: list
    start_destination: str
    user_id: str
    package_id: str