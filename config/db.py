from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:A123456789b@localhost:3306/login")
conn = engine.connect()
meta_data = MetaData()
