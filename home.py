
from flask import Flask
app=Flask(__name__)



@app.route('/')
def home():
    random = []
    dicty = {'hello':44, 'goodbye':77}
    for key, item in dicty.items():
        random.append(item)
    var = str(random)
    return var

if __name__ == "__main__":
    app.run()