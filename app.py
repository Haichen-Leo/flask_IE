from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Init app
app = Flask(__name__)
# Database
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@127.0.0.1:3306/forheart?charset=utf8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# init db
db = SQLAlchemy(app)
# init ma
ma = Marshmallow(app)


# model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))

    def __init__(self, content):
        self.content = content


# schema
class FeedbackSchema(ma.Schema):
    class Meta:
        fields = ('id', 'content')


# init schema
feedback_schema = FeedbackSchema()
feedbacks_schema = FeedbackSchema(many=True)


# feedback
@app.route('/feedback', methods=['POST'])
def new_feedback():
    content = request.json['feedback']
    new_feedback = Feedback(content)

    db.session.add(new_feedback)
    db.session.commit()
    return jsonify({'msg': 'ok'})


# get all
@app.route('/feedback', methods=['GET'])
def all_feedback():
    all_feedback = Feedback.query.all()
    result = feedbacks_schema.dump(all_feedback)
    return jsonify(result)


# Run Server
if __name__ == "__main__":
    app.run(debug=True)
