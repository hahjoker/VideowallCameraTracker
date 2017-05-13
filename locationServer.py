#USAGE
#sudo python locationServer.py
#curl --noproxy GET http://127.0.0.1:5000/location

import os
from flask import Flask, session,request,url_for, json, jsonify
app = Flask(__name__)

def readfile():
    f = open('location.txt')
    fmistake=[]
    for line in f:
        fmistake.append(line)
    f.close()
    count=0
    for e in fmistake: #removing the new line
        if(count<2):
            fmistake[count]=fmistake[count][:-1]
            count+=1
    return fmistake

def check(loc):
    fsavedloc = open('savedlocation.txt')
    fmistake=[]
    for line in fsavedloc:
        fmistake.append(line)
    fsavedloc.close()
    truthcheck=0
    count=0
    for x in loc:
        print x
        print fmistake[count]
        #forgiveness of x
        forgive=0.05
        if (float(x)<(float(fmistake[count])+forgive) and float(x)>(float(fmistake[count])-forgive)):
            truthcheck+=1
        count+=1
    print truthcheck
    if (truthcheck==3):
        return True
    return False


@app.route('/location', methods = ['GET']) #flask server
def api_echo():
    if request.method == 'GET':
        location=readfile()
        if check(location):
            print 'same loc'
        else:
            print 'Error! Locations are not the same!'
        x = location[0]
        y = location[1]
        z = location[2]
        data = {'x' : x , 'y' : y ,'z' : z }

        resp = jsonify(data)
        resp.status_code = 200
        return resp

if __name__ == '__main__':
    app.run(threaded=True)
