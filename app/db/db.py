from sqlalchemy import create_engine

def connect_to_database(db_host: str, db_port: str, db_name: str, db_user: str, db_password: str):
    engine = create_engine(
        f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )
    return engine