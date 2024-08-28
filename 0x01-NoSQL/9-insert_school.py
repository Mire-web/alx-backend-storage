#!/usr/bin/env python3
"""
Insert a new school in a collection
"""
import pymongo


def insert_school(collection, **kwargs):
    """Merge keywords and insert new object"""
    new_school_obj = {}
    for key, value in **kwargs:
        new_school_obj[key] = value
    _id = collection.insert_one(new_school_obj)
    return _id
