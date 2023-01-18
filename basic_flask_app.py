from flask import Flask, render_template

# Alustetaan ohjelma flask-aplikaatioks
app = Flask("__name__") # __name__ = main(tiedoston nimen 1.osa)

                # sama kuin localhost:5000
@app.route("/") # 127.0.0.1:5000
def hello_world():
    return "<b> Hello World!</b>"

@app.route("/about")
def about():
    return "<b> About</b>"

if __name__ == '__main__':
    app.run(host='localhost', port=9999)