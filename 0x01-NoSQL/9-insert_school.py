#!/usr/bin/env python3
"""
Insert a new school in a collection
"""
import pymongo


def insert_school(mongo_collection: pymongo, **kwargs: dict):
    """Merge keywords and insert new object"""
    new_school_obj = {}
    for key, value in **kwargs:
        new_school_obj[key] = value
    _id = mongo_collection.insert_one(new_school_obj)
    return _id
