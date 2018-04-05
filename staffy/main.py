""" Connects all the methods in the sdb rest api with a simple class """
import requests
import json


class Wrapper(object):
    def __init__(self, ip, port):
        self.url = "http://{}:{}/".format(ip, port)
    
    def check_request_helper(self, r):
        if r.status_code != 200:
            return False

        x = r.json()
        if x["result"]:
            x = x["data"] if x["data"] else  x["result"]
            return  x
        return False

    def args_helper(self, kwargs):
        args = {}
        if kwargs:
            for key, value in kwargs.items():
                args[key] = value
        return args

    def get_profile(self, **kwargs):
        args = self.args_helper(kwargs)
        if args:
            r = requests.get(self.url + "profile", params=args)
            return self.check_request_helper(r)
        return False
    
    def patch_profile(self, **kwargs):
        args = self.args_helper(kwargs)
        if args:
            r = requests.patch(self.url + "profile", data=args)
            return self.check_request_helper(r)
        return False

    def get_document(self, **kwargs):
        args = self.args_helper(kwargs)
        if args:
            r = requests.get(self.url + "document", params=args)
            return self.check_request_helper(r)
        return False

    def put_document(self, **kwargs):
        args = self.args_helper(kwargs)
        if args:
            r = requests.put(self.url + "document", data=args)
            return self.check_request_helper(r)
        return False

    def patch_document(self, **kwargs):
        args = self.args_helper(kwargs)
        if args:
            r = requests.patch(self.url + "document", data=args)
            return self.check_request_helper(r)
        return False

    def delete_document(self, **kwargs):
        args = self.args_helper(kwargs)
        if args:
            args["confirmation"] = True
            r = requests.delete(self.url + "document", data=args)
            return self.check_request_helper(r)
        return False
