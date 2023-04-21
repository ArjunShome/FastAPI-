from fastapi import FastAPI, Body
from enum import Enum

import uvicorn
from models import User, Product
from typing import Annotated

my_app = FastAPI()


class Nameenum(str, Enum):
    Ajoy = "Ajoy"
    Rama = "Rama"
    Ayan = "Ayan"
    Manjusa = "Manjusa"
    Arjun = "Arjun"
    Sanchita = "Sanchita"


# Health check API
@my_app.get("/")
def health_check():
    """_summary_
        Health check API to check run.
    Returns:
        json:Health check message
    """
    return {"message": "Hello World!! I am Alive!! :)"}


# Path Pass and Parse API example
@my_app.get("/Item/{item}")
def get_user_item(item: int):
    """_summary_
        Check path parse value
    Args:
        item (int): the item number to pass

    Returns:
        json:The item number
    """
    return {"item": item}


# Adding Enums to path API example
@my_app.get("/Names/{user_name}")
def get_user_name(user_name: Nameenum):
    if user_name is Nameenum.Ajoy:
        return {"Name": f"{user_name}", "message": "The Father in the house"}
    if user_name is Nameenum.Rama:
        return {"Name": f"{user_name}", "message": "The Mother in the house"}
    if user_name is Nameenum.Ayan:
        return {"Name": f"{user_name}", "message": "The elder son of the house"}
    if user_name is Nameenum.Manjusa:
        return {"Name": f"{user_name}", "message": "The wife of elder son in the house"}
    if user_name is Nameenum.Arjun:
        return {"Name": f"{user_name}", "message": "The younger son of the house"}
    if user_name is Nameenum.Sanchita:
        return {"Name": f"{user_name}", "message": "The wife of younder son in the house"}


# Pydentic Model
@my_app.post("/User/Create")
def create_user(user: User):
    incoming_user = user.dict()
    message = "Aadhar and Pan Mandatory" if user.is_adult else "User is a child"
    incoming_user.update({"usr_msg": message})
    return incoming_user
    

@my_app.post("/Product/Details")
def get_product_details(
    product_detail: Annotated[
        Product,
        Body(
            examples={
                "Valid Request": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
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
                },
                "Invalid Request": {
                    "summary": "An example with invalid product id",
                    "description": "invalid product id specified and also type id is expected minimum to be 2",
                    "value": {
                        "product_id": "ert",
                        "product_type": {"type_id": 1, "type_category": "Automobile"},
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
                },
            }
        ),
    ]
):
    dict_product_detail = product_detail.dict()
    message = (
        "Automobile"
        if product_detail.product_type.type_category == "Vehicle"
        else "Other"
    )
    dict_product_detail.update({"user_mesasge": message})
    return dict_product_detail


if __name__ == "__main__":
    uvicorn.run("run:my_app", reload=True)  # type: ignore
