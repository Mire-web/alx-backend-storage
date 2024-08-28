#!/usr/bin/env python3
"""
Return list of school having a specific topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """Filter schools by topic offered and return given topic"""
    return mongo_collection.find({"topics": topic})
