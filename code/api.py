from flask import Flask
from datetime import date
from flask_restful import Resource, Api
# import nse_bhav_download as nse_downloader
import weekly_csv
from pandas import DataFrame as df

app = Flask(__name__)
api = Api(app)

# class HelloWorld(Resource):
#     def get(self):
#         return {'data': 'Hello World!'}


# class HelloName(Resource):
#     def get(self, name):
#         return {'data': 'Hello, {}'.format(name)}

class Gain_Loss_Weekly(Resource):
    """
    Returns the Gain_Loss percentage ( [Last closing price of the end of the week - Opening price at start of week / opening price at start of week] * 100) of each listed company
    """
    def get(self, input_date):
        if (len(input_date) < 8):
            return "Invalid date"
        year = int( input_date[:4] )
        month = int( input_date[4:6] )
        day = int( input_date[6:] )     
        try:
            arg_date =  date(year,month,day)
        except Exception as E:
            return str(E) + " Invalid date"
        err_msg = "Error in fetching data"
        if (weekly_csv.view_Gain_loss_all_weekly(arg_date) == False):
            return err_msg
        return weekly_csv.view_Gain_loss_all_weekly(arg_date)
        # return {'year': '{}'.format(year), 'month' : '{}'.format(month), 'day' : '{}'.format(day)} 

class Company_CSV_weekly(Resource):
    """
    Retruns weekly data of the input company
    """
    def get(self,input_date,company_name):
        year = int( input_date[:4] )
        month = int( input_date[4:6] )
        day = int( input_date[6:] )                        
        arg_date =  date(year,month,day)
        file = weekly_csv.compose_weekly_csv(arg_date)
        err_msg1 = "Error in fetching data for the input week"
        err_msg2 = "Company not listed"
        err_msg3 = "file empty!"
        if (type(file) != df):
            if (file == None):
                return err_msg1
        if (file.empty):
            return err_msg3
        company_csv = weekly_csv.compose_company_file(file,company_name)
        if (company_csv.empty):
            return err_msg2
        return company_csv.to_json()
        # return {'input date' : '{}'.format(inputt_date)}

        


# api.add_resource(HelloWorld, '/helloworld')
# api.add_resource(HelloName, '/helloworld/<string:name>')
api.add_resource(Gain_Loss_Weekly, '/gain_loss_weekly/<string:input_date>')
api.add_resource(Company_CSV_weekly, '/company_csv_weekly/<string:input_date>/<string:company_name>')


if __name__ == "__main__":
    app.run(debug=True)
