#!/usr/bin/env python3
"""
List all documents in a collection
"""
import pymongo
from typing import List


def list_all(mongo_collection: pymongo) -> List:
    """List all document in collection"""
    new_list = []
    for item in mongo_collection.find():
        new_list.append(item)
    if len(new_list) == 0:
        return []
    return new_list
