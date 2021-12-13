create_schema = ('''

    CREATE SCHEMA IF NOT EXISTS petl3
    '''
)

create_tables = ('''

    DROP TABLE IF EXISTS petl3.viable_counties;

    CREATE TABLE IF NOT EXISTS petl3.viable_counties (
        geo_id int,
        state TEXT,
        county TEXT,
        sales_vector int 
    );
''')


insert_county = ('''  
  INSERT INTO petl3.viable_counties (geo_id, state, county, sales_vector)
  VALUES(%s, %s, %s, %s);
''')

