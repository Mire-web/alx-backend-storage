#!/usr/bin/env python3
"""
Insert a new school in a collection
"""
import pymongo


def insert_school(collection, **kwargs):
    """Merge keywords and insert new object"""
    return collection.insert(kwargs)
