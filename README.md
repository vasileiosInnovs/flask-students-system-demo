# SQLAlchemy Database Relationships Demo
This project demostrates creating databases relationships using sqlalchem and data serialization with sqlalchemy_serializer

## Setup
Run the following commands to setup modules
```pipenv install && pipenv shell```

- Create a .env at the root of the project with the following content
```
FLASK_APP = app.py
FLASK_DEBUG = True
FLASK_RUN_PORT = 5555
FLASK_SQLALCHEMY_DATABASE_URI=postgresql://username:password@localhost:5433/db
FLASH_HASHSECRET = ALDSFJLKSAJDFLJASDLFJWERJLjowieofjsd
```

Change the connection string to suit your need# student-management-system-api
