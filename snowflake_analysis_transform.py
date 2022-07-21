import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Data transformation for hemo values in snowflake')
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
table_list = my_cur.execute("select IDPATIENTTREATMENT,\
                        ANALYSIS_TYPE,\
                        PRE_VALUE,\
                        POST_VALUE,\
                        TREATMENT_VOLUME_HARVESTED_ML,\
                        TOTAL_VOLUME_DELIVERED_FROM_INJECTION_SITES_ML,\
                        RECORD_OWNER from STITCH.STITCH2_INTEGRATION.GREYLEDGE_DATA_CLOUD__TREATMENT_HEMOANALYSIS_VALUES;").fetchall()
df=pd.DataFrame(table_list)
df.rename(columns={0:'id_patient_treatment',
                   1:'analysis_type',
                   2:'Pre',
                   3:'Post',
                   4:'volume_harvested',
                   5:'volume_injected',
                   6:'record_owner'},inplace=True)
streamlit.dataframe(df)

#analysis_data = my_cur.fetchall()
#df=streamlit.dataframe(analysis_data)
#streamlit.text(df.columns)
#streamlit.text(df.columns())
 
