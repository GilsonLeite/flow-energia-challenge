import os
import json
import mysql.connector
from mysql.connector import Error
from django.views.generic import TemplateView


class ForecastDetailView(TemplateView):
    template_name = 'forecast/analysis_result.html'


class ForecastLoadDatabaseView(TemplateView):
    template_name = 'forecast/analysis_result.html'

    def get_context_data(self, **kwargs):

        try:
            connection = mysql.connector.connect(
                host='testeflow.c3u0viwxwdgw.us-east-1.rds.amazonaws.com',
                database='teste_admin',
                user='teste_user',
                password='teste_devFullStack',
                port='3306',
            )
            if connection.is_connected():
                cursor = connection.cursor(dictionary=True)

            sql_select_Query = "SELECT * FROM example_table\
                WHERE VarID=1\
                AND AreaType='System'\
                AND ForecastDate BETWEEN '2020-02-15' AND '2020-03-25'\
                AND AreaID BETWEEN '1' AND '4'\
                AND ScenarioName IN ('EC-P25', 'EC-P50', 'EC-P75')"

            cursor.execute(sql_select_Query)
            result_filter = cursor.fetchall()

            # Selecting the data of interest
            data_for_analysis = [
                item for item in result_filter if item['TargetLabel'] == '2020-W14']

            _path = os.path.dirname(__file__)
            with open(_path+'/data_for_analysis_db.json', 'w', encoding='utf-8') as f:
                json.dump(data_for_analysis, f,
                          ensure_ascii=False, default=str)

        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
        return {'data': 'data'}
