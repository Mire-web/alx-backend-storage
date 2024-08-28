#!/usr/bin/env python3
"""
Provide stats about nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def nginx_stats():
    """Show the stats about nginx logs stored in mongoDB"""
    with MongoClient() as client:
        db = client.logs
        count = db.nginx.count()
        print("{} logs".format(count))
        print("Methods:")
        get_count = db.nginx.count({"method": "GET"})
        post_count = db.nginx.count({"method": "POST"})
        put_count = db.nginx.count({"method": "PUT"})
        patch_count = db.nginx.count({"method": "PATCH"})
        delete_count = db.nginx.count({"method": "DELETE"})
        print("\tmethod GET: {}".format(get_count))
        print("\tmethod POST: {}".format(post_count))
        print("\tmethod PUT: {}".format(put_count))
        print("\tmethod PATCH: {}".format(patch_count))
        print("\tmethod DELETE: {}".format(delete_count))
        get_status_count = db.nginx.count({"method": "GET",
                                                     "path": "/status"})
        print("{} status check".format(get_status_count))


if __name__ == '__main__':
    nginx_stats()
