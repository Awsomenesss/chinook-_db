from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)
# executing the instractions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# creat variable for "Artist" table
artist_table = Table (
    "Artist", meta,
    Column("ArtistID",Integer,primary_key=True),
    Column("Name",String)
)
# create variable for "Album" table
album_table = Table(
    "Album",meta,
    Column("AlbumId",Integer,primary_key=True),
    Column("Title",String),
    Column("ArtistId",Integer,ForeignKey("artist_table.ArtistId"))
)
# making the connection 
with db.connect() as connection: