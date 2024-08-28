#!/usr/bin/env python3
"""
Change all topics in specified school
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """Update all Topics in a school document"""
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
