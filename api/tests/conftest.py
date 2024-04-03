# conftest.py
import pytest
import subprocess
import time
from sqlalchemy import create_engine, exc
from models import Base
import pandas as pd
import os

os.environ["JWT_SECRET_KEY"] = "oth42obgtwknbwl2ngl2np2non24ongtonh2gn2ngpwn"

@pytest.fixture(scope='session')
def postgres_db():
    # Start a new PostgreSQL instance in Docker
    container_id = subprocess.getoutput(
        "docker run -d -e POSTGRES_PASSWORD=secret -e POSTGRES_DB=test_db -p 5432:5432 postgres:13"
    )
    print(f"Started PostgreSQL container: {container_id}")

    # Initialize a connection engine
    engine = create_engine("postgresql://postgres:secret@localhost:5432/test_db")

    # Poll database to check if it's ready
    max_retries = 10
    retry_count = 0
    while retry_count < max_retries:
        try:
            # Attempt to connect to the database
            pd.read_sql("select 1", engine)
            print("Database is ready.")
            break  # Database is ready, break out of loop
        except exc.SQLAlchemyError:
            print("Database not ready yet. Retrying...")
            retry_count += 1
            time.sleep(2)  # Wait for 2 seconds before retrying

    if retry_count == max_retries:
        print("Max retries reached. Exiting.")
        raise Exception("Could not connect to database.")
    
    Base.metadata.create_all(bind=engine)

    yield engine  # Provides the database connection to the test

    # Teardown: Stop and remove the container
    subprocess.run(["docker", "container", "stop", container_id])
    subprocess.run(["docker", "container", "rm", container_id])
    print(f"Removed PostgreSQL container: {container_id}")