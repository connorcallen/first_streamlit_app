import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Data transformation for hemo values in snowflake')
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from GREYLEDGE_DATA_CLOUD__TREATMENT_HEMOANALYSIS_VALUES")
analysis_data = my_cur.fetchall()
df=streamlit.dataframe(analysis_data)
streamlit.text(df.columns)
streamlit.text(df.columns())
 
