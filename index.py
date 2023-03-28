from flask  import  Flask,render_template,request
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>曾信升python網頁</h1>"
    homepage += "<a href=/today>顯示目前時間</a><br>"
    homepage += "<a href=/welcome?ken=信升>傳送使用這暱稱</a><br>"
    return homepage
@app.route("/mis")
def course():
    return "<h1>歡迎光臨</h1>"
@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html",datetime=str(now))
@app.route("/welcome",methods=["GET","POST"])
def welcome():
    user = request.values.get("ken")
    return  render_template("welcome.html",name=user)
#if __name__ == "__main__":
    #app.run()
