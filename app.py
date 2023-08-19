from bardapi import Bard



from flask import Flask, request,jsonify,json
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


token = "aAjW3souphQ7tT0Rf8rviWsBBOH30ZuLtHVK3at4V-O9-K2IraoxcP_mEq6JG15KgK0EHA."



# questionString = str(questionsData)

@app.route('/bot', methods=['GET'])
def search():

    try:

        args = request.args
        prompt = args.get("question", default="", type=str)
        prompt = "warning!! only answer the question which is requested and do not give any other texts in the response! i am giving you this json with keys as some questions and the values as answer to the respective question, i will tell you what is the question and you will answer me by finding that question in the json as key and tell me the answer according to the value of that key, the json is {'hi' :'hello','how are you?':'i am good','hello':'hii'} and the question is '"+question+"' , wrap the answer in ]"

        bard = Bard(token=token)

        result = bard.get_answer(prompt)

        

        return result['content']

    except:
        return "there is an error"

print(search())

if __name__ == '__main__':
    app.run(debug=False)
    
