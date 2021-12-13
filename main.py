from google.cloud import bigquery

import pgsql
import sql                              # necessary imports


if __name__ == '__main__':

    # pgsql.query(sql.create_schema)  # creating the schema

    pgsql.query(sql.create_tables)

    client = bigquery.Client()
    query = client.query(
        """
    
        SELECT geo_id, sub_region_1 AS State, sub_region_2 AS County, AVG(retail_and_recreation_percent_change_from_baseline) AS Sales_Vector 

        FROM  `bigquery-public-data.census_bureau_acs.county_2017_1yr`              

        JOIN `bigquery-public-data.covid19_google_mobility.mobility_report` 
        ON geo_id || '.0' = census_fips_code

        GROUP BY geo_id, sub_region_2, sub_region_1, median_age, median_rent

        HAVING AVG(retail_and_recreation_percent_change_from_baseline) > -15 
        AND median_age <30 AND median_rent < 2000

        ORDER BY Sales_Vector DESC; 
        """
    )
    for row in query.result():
        pgsql.query(sql.insert_county, [int(row[0]), row[1], row[2], int(row[3])])  # inserting each row into the db


