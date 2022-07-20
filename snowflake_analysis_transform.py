import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Data transformation for hemo values in snowflake')


with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from STITCH.STITCH2_INTEGRATION.GREYLEDGE_DATA_CLOUD__TREATMENT_HEMOANALYSIS_VALUES")
    return my_cur.fetchall()

