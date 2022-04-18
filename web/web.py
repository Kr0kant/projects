from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def Go():
    if request.method == 'GET':
        name_param = request.args.get('name')

    if name_param is None:
        name_param = "Анонимус"

    return render_template(
        'mainpage.html',
        name=name_param,
        method=request.method
    )

@app.context_processor
def inject_globals():
    return {
        "videos": ["https://www.youtube.com/embed/jsBnFHdsSjc", "https://www.youtube.com/embed/zGhqZGAbIqY", "https://www.youtube.com/embed/vjWvHO6hZgA", "https://www.youtube.com/embed/lOgL9K0lpbc", "https://www.youtube.com/embed/drd3TIk-4QE", "https://www.youtube.com/embed/MinrxATiDGQ", "https://www.youtube.com/embed/eu4Z12knnPw", "https://www.youtube.com/embed/JBxwd7X2pRc", "https://www.youtube.com/embed/bT2QAyNw2qw", "https://www.youtube.com/embed/xyBM5c84g0Y", "https://www.youtube.com/embed/xhJ8BTfTZrs", "https://www.youtube.com/embed/ZKUaNQZKrUc"
        ]
    }

if __name__ == "__main__":
    app.run()