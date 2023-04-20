from fastapi import FastAPI
from enum import Enum

import uvicorn
from models import User

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


if __name__ == "__main__":
    uvicorn.run("run:my_app", reload=True) #type: ignore
