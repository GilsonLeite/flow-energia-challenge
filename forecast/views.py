import os
import json
import mysql.connector
from mysql.connector import Error
from django.views.generic import TemplateView


class ForecastDetailView(TemplateView):
    template_name = 'forecast/analysis_result.html'


class ForecastLoadDetailView(TemplateView):
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
                sql_select_Query = \
                    "SELECT * FROM example_table WHERE VarID=1 AND \
                        ForecastDate BETWEEN '2020-02-15' AND '2020-03-25'"

                cursor.execute(sql_select_Query)
                result_filter = cursor.fetchall()

                _path = os.path.dirname(__file__)
                with open(_path+'/load_db.json', 'w', encoding='utf-8') as f:
                    json.dump(result_filter, f, ensure_ascii=False,
                              indent=4, default=str)

        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
        return {'data': 'data'}
