import sys
import json
import os

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask import request, jsonify
import base64
import subprocess


app = Flask(__name__)
api = Api(app)



parser = reqparse.RequestParser()

def cmd_exec(cmdStr):
        try:
                output = subprocess.check_output(["bash","-c", cmdStr]).strip()
        except Exception as e:
                print e
                output = ""
        return output


# shows a list of all todos, and lets you POST to add new tasks
class GetUserId(Resource):
        def get(self):
                parser.add_argument('userName')
                args = parser.parse_args()
                ret = {}

                if args["userName"] is not None and len(args["userName"].strip()) > 0:

                        corpDomains = ['REDMOND','FAREAST','EUROPE','NORTHAMERICA']
                        ret["uid"] = ""

                        for corpDomain in corpDomains:
                                if len(ret["uid"].strip())==0:
                                        userName = str(args["userName"]).strip().split("@")[0]
                                        uid = cmd_exec("id -u %s.%s" % (corpDomain,userName))
                                        gid = cmd_exec("id -g %s.%s" % (corpDomain,userName))
                                        groups = cmd_exec("id -G %s.%s" % (corpDomain,userName)).split(" ")

                                        ret["uid"] = uid
                                        ret["gid"] = gid
                                        ret["groups"] = groups


                resp = jsonify(ret)
                resp.headers["Access-Control-Allow-Origin"] = "*"
                resp.headers["dataType"] = "json"


                return resp

##
## Actually setup the Api resource routing here
##
api.add_resource(GetUserId, '/GetUserId')





class VerifyUserinGroup(Resource):
        def get(self):
                parser.add_argument('userName')
                parser.add_argument('gid')
                args = parser.parse_args()
                ret = {}
                ret["authorized"] = False
                if args["userName"] is not None and len(args["userName"].strip()) > 0:
                        userName = str(args["userName"]).strip().split("@")[0]
                        uid = cmd_exec("id -u REDMOND.%s" % userName)
                        gid = cmd_exec("id -g REDMOND.%s" % userName)
                        groups = cmd_exec("id -G REDMOND.%s" % userName).split(" ")

                        ret["uid"] = uid
                        ret["gid"] = gid
                        ret["groups"] = groups
                        ret["authorized"] = args['gid'] in groups

                resp = jsonify(ret)
                resp.headers["Access-Control-Allow-Origin"] = "*"
                resp.headers["dataType"] = "json"

                return resp
##
## Actually setup the Api resource routing here
##
api.add_resource(VerifyUserinGroup, '/VerifyUserinGroup')





if __name__ == '__main__':
        app.run(debug=False,host="0.0.0.0",threaded=True)
