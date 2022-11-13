if __name__ == "__main__":
    from app.app import app
    from decouple import config
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(config("PORT")))
