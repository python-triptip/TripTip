import trip
from flask import Flask
from flask import render_template
from flask import make_response, url_for
from flask_restful import Resource, Api, request, abort

app = Flask(__name__, static_url_path='/static')
api = Api(app)


class TripRecommand(Resource):
    def get(self):
        """problem5

        Arguments:

        Returns:
            dict -- returns the journal_db
        """
        city = request.args.get("city")
        budget = 0
        try:
            budget = float(request.args.get("budget"))
        except:
            budget = 0
        type = request.args.get("type")
        print(city, budget, type)

        if city == None:
            city = ''
        if type == None:
            type = ''

        tourCheck = ''
        restCheck = ''
        infoList = []
        if type == 'restaurant':
            infoList = trip.restaurant_based_on_budget(city, budget)
            restCheck = 'checked'
        if type == 'tourism':
            infoList = trip.tourism_based_on_budget(city, budget)
            tourCheck = 'checked'

        headers = {'Content-Type': 'text/html'}
        if len(infoList) == 0:
            tempInfo = trip.TripInfo(['', '', '', '', '', ''], '')
            tempInfo.name = "Input is not correct, or there is no matched result in our database."
            infoList.append(tempInfo)

        return make_response(render_template('index.html', infoList=infoList, city=city, budget=str(budget),
                                             restCheck=restCheck, tourCheck=tourCheck), 200, headers)

    def post(self):
        """problem6
        creates a new journal entry in the database using create_journal_entry
        and returns 201 on success

        HINT: you have to decode the data to UTF-8

        Returns:
            tuple -- returns the newly created entry and 201
        """

        return "test2"

api.add_resource(TripRecommand, '/trip')


if __name__ == '__main__':
    app.run(debug=True)