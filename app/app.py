from flask import Flask, render_template,request,jsonify
from crud import *

app = Flask(__name__)

@app.route("/add")
def add():
    item = request.args.get("item")
    date = request.args.get("date")
    weight = request.args.get("weight")
    transtype = request.args.get("transtype")
    remark = request.args.get("remark")
    try:
        insert_value(item,date,weight,transtype,remark)
    except:
        return jsonify("pls enter transaction type as 'purchase' or 'sale")

    return jsonify("added {},{},{},{},{} to the db".format(item,date,weight,transtype,remark))

@app.route("/delete")
def delete():
    item = request.args.get("item")
    delete_value(item)
    return jsonify("deleted {} from the db".format(request.args.get("item")))

@app.route("/update")
def update():
    item = request.args.get("item")
    date = request.args.get("date")
    weight = request.args.get("weight")
    transtype = request.args.get("transtype")
    remark = request.args.get("remark")
    try:
        update_value(item,date,weight,transtype,remark)
    except:
        return jsonify("pls enter transaction type as 'purchase' or 'sale")
    
    return jsonify("updated {},{},{},{},{} in the db".format(item,date,weight,transtype,remark))

@app.route("/get")
def get():
    item = request.args.get("item")
    out = get_value(item)
    return jsonify(out)

@app.route("/getall")
def getall():
    out = get_all_values()
    return jsonify(out)



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)


