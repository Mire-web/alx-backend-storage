#!/usr/bin/env python3
"""
SOrt all students by average scores
"""
import pymongo


def top_students(collection):
    """ Return the list of students sorted by average score"""
    return collection.find().sort('score', pymongo.DESCENDING)
