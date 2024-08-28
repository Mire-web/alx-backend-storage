#!/usr/bin/env python3
"""
Change all topics in specified school
"""
import pymongo


def update_topics(collection, name, topics):
    """Update Topics in school"""
    collection.update({name: name}, {topics: topics})
