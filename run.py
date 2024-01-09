from app.routes import app 

match __name__:
    case "__main__":
        app.run(host="localhost", port=8080, debug=True)
