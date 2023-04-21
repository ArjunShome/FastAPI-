from pydantic import BaseModel, Field


class User(BaseModel):
    id: int = Field(title="ID of the User", ge=2)
    name: str = Field("BLA BLA", description="The USer's Name", max_length=5)
    address: str
    adhar_number: int
    mobile_number: int
    pan_number: int
    is_adult: bool


class Product_type(BaseModel):
    type_id: int = Field(title="ID of the Product Type", ge=2)
    type_category: str


class Product(BaseModel):
    product_id: int = Field(title="ID of the Product", ge=2)
    product_type: Product_type
    product_name: str = Field(title="Name of the PRoduct", max_length=100)
    users: list[User]

    class Config:
        schema_extra = {
            "example": {
                "product_id": 2,
                "product_type": {"type_id": 2, "type_category": "Automobile"},
                "product_name": "Hyundai Creta",
                "users": {
                    "id": 2,
                    "name": "Arjun",
                    "address": "Kolkata",
                    "aadhar_number": 111,
                    "pan_number": 132,
                    "is_adult": "True",
                },
            },
        }
