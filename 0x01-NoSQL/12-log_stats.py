#!/usr/bin/env python3
"""
Provide stats about nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def nginx_stats():
    with MongoClient() as client:
        db = client.logs
        get
