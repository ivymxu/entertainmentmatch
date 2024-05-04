"""
This program takes two vectors as parameters and calculates the cosine similarity
Example input: vector1 = [5, 4, 5], vector2 = [0, 4, -5]
Example output: -0.17301
"""

import math


def similarity(vector1, vector2):
    """
    Returns the cosine similarity between two vectors.  The vectors 
    must have the same length.  If either vector is all zeros, then the 
    similarity is defined to be zero.  Vectors are assumed to be lists that
    contain numbers (ints and floats).
    """
    if len(vector1) != len(vector2):
        raise ValueError("vectors must be same length")

    if vector1 == vector2:
        return 1.0

    dot_product = 0
    vector1_squared_sum = 0
    vector2_squared_sum = 0

    for i in range(len(vector1)):
        dot_product = dot_product + (vector1[i] * vector2[i])
        vector1_squared_sum = vector1_squared_sum + vector1[i] * vector1[i]
        vector2_squared_sum = vector2_squared_sum + vector2[i] * vector2[i]

    if dot_product == 0 or vector1_squared_sum == 0 or vector2_squared_sum == 0:
        return 0.0
    else:
        cosine_similarity = dot_product / \
            (math.sqrt(vector1_squared_sum) * math.sqrt(vector2_squared_sum))
        return cosine_similarity
