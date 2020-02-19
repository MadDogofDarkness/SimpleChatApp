from flask import Flask, request
app = Flask(__name__)

Zeposts = []

def construct_reply(list_of_posts):
    posts = ""
    for post in list_of_posts:
        posts += f"({post[0]} : {post[1]}) \n"
    return posts

@app.route('/', methods=["POST"])
def post_result():
    print('post')
    try:
        Zeposts.append((str(request.form['username']), str(request.form['message'])))
        if len(Zeposts) > 25:
            rip = Zeposts.pop(0)
    except Exception:
        return '404'
    return 'Recieved...'

@app.route('/', methods=["GET"])
def get_result():
    print("get")
    if len(Zeposts) <= 0:
        return 'no messages'
    else:
        return construct_reply(Zeposts)

app.run(host='0.0.0.0', port=<--port-->)