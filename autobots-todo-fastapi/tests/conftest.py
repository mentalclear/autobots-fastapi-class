import pytest
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import Session
from app import models
from app.database import get_db
from app.main import app
from fastapi.testclient import TestClient



@pytest.fixture(name='session')
def session_fixture():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False},
    poolclass=StaticPool     
    )
    models.Base.metadata.create_all(bind=engine)
    with Session(engine) as session:
        yield session

@pytest.fixture(name="client")        
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_db] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()    
