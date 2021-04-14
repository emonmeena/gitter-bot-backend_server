from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('q')
parser.add_argument('username')


introduction = {'study', 'undergraduate', 'fresher', 'year', 'university', 'new', 'contributer', 'sophomore', 'open-source.', 'open source', 'open-source', 'want to contribute', 'how to start',
                'start', 'advice', 'guide', 'scorelab', 'score-lab', 'projects on', 'projects based on', 'how should i start', 'how to begin', 'how can i start', 'how should i start', 'how should i proceed'}

skills = {'css', 'html', 'javascript', 'python', 'react',
          'django', 'flask', 'mongodb', 'sql', 'mysql', 'shell'}


class Project:
    def __init__(self, programming_lang, name, github_repo, gitter):
        self.programming_lang = programming_lang
        self.name = name
        self.github_repo = github_repo
        self.gitter = gitter


p1 = Project(["javascript", "python", "flask"], "ChatBot",
             "https://www.github.com", "https://www.gitter.com")
demonstartion_data = {p1}

about_community = "The SCoRe Lab has conducted research covering various aspects of sensor networks, embeded systems, digital forensic, information security, mobile applications, cloud, blockchain and software tools. The goal of our research is to generate computing solutions through identifying low cost methodologies and strategies that lead to sustainability."
community_website_link="https://scorelab.org/"
community_github_link = "https://github.com/scorelab"

class GitterBot(Resource):
    def get(self):
        args = parser.parse_args()
        query = args['q']
        username = args['username']
        query = query.lower()
        user_skills = []
        count = 0
        for x in introduction:
            if x in query:
                count += 1

        if count > 2:
            for x in skills:
                if x in query:
                    user_skills.append(x)
            if len(user_skills) != 0:
                for y in demonstartion_data:
                    if user_skills[0] in y.programming_lang:
                        return {'res': '**testbot**- Welcome @{} to scorelab community!\nI have found some projects which might interest you.\n- {} [Github]({}) [Gitter]({})'.format(username, y.name, y.github_repo, y.gitter)}
            return {'res': '**testbot**- Welcome @{} to scorelab!\nI am ChatBot and I am here to answer your queries. \n**type `@bot -help` to learn more about me.**'.format(username)}
        return {'res': 0}

class ExistingUser(Resource):
    def get(self):
        args = parser.parse_args()
        query = args['q']
        username = args['username']
        y = p1
        return {'res': '**testbot**- @{} I have found some projects.\n- {} [Github]({}) [Gitter]({})'.format(username, y.name, y.github_repo, y.gitter)}
        # return {'res': 0}


api.add_resource(GitterBot, '/client_message')
api.add_resource(ExistingUser, '/existing_user')

if __name__ == '__main__':
    app.run(debug=True)
