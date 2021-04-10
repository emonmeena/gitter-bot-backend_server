from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('q')

introduction={'study', 'undergraduate', 'fresher', 'year', 'university', 'new', 'contributer', 'sophomore', 'open-source.', 'open source', 'open-source', 'want to contribute', 'how to start', 'start', 'advice', 'guide', 'scorelab', 'score-lab', 'projects on', 'projects based on', 'how should i start', 'how to begin', 'how can i start', 'how should i start', 'how should i proceed', 'how should i start?', 'how to begin?', 'how can i start?', 'how should i start?', 'how should i proceed?'}

skills={'css', 'html', 'javascript', 'python', 'react', 'django', 'flask', 'mongodb', 'sql', 'mysql', 'shell', 'go', 'css,', 'html,', 'javascript,', 'python,', 'react,', 'django,', 'flask,', 'mongodb,', 'sql,', 'mysql,', 'shell,', 'go,'}

user_skills=[]

class GitterBot(Resource):
    def get(self):
        args = parser.parse_args()
        query = args['q']
        query = query.lower()
        count = 0
        for x in introduction:
            if x in query:
                count +=1
                
        if count>2:
            for x in skills:
                if x in query:
                    user_skills.append(x)    
            return {'res': 'Welcome to scorelab and your skillset includes {} with matching set of {}'.format(user_skills, count)}        
        return {'res': 'could not get that'}

    # def put(self, todo_id):
    #     todos[todo_id] = request.form['data']
    #     return {'res':'data'}

api.add_resource(GitterBot, '/client_message')

if __name__ == '__main__':
    app.run(debug=True)