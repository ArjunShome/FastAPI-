from fastapi import FastAPI

app = FastAPI()


# Health check API
@app.get("/")
def health_check():
    """_summary_
        Health check API to check run.
    Returns:
        json:Health check message
    """
    return {"message": "Hello World!! I am Alive!! :)"}


# Path Pass and Parse API example
@app.get("/Item/{item}")
def get_user_item(item: int):
    """_summary_
        Check path parse value
    Args:
        item (int): the item number to pass

    Returns:
        json:The item number
    """
    return {"item":item}

