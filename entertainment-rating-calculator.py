"""
Reads the files media.txt and ratings.txt and then for each media, outputs to a file
named most-similar-media.txt the most similar media and the similarity score
"""

from vectorsimilarity import *


def format_similar_message(source_media_title, most_similar_title, similarity_score):
    result = f'People who liked {source_media_title}, ' + \
             f'also liked {most_similar_title} with a score of {similarity_score:.3f}.'
    return result


def read_files():
    media_infile = open("media.txt", "r")
    ratings_infile = open("ratings.txt", "r")

    media_list = []
    rating_list = []

    # Adding the media title and creating lists within the rating list
    media_length = len(media_infile.readlines())
    user_length = len(ratings_infile.readlines()) // media_length

    # Convert lengths to integers
    media_infile.seek(0)
    ratings_infile.seek(0)

    for i in range(media_length):
        read_media = media_infile.readline().strip()
        media_list.append(read_media)
        rating_list.append([])

    # Adding ratings for each media within each rating list
    for i in range(user_length):
        ratings_infile.readline()
        for j in range(media_length):
            read_rating = ratings_infile.readline().strip()
            rating_list[j].append(int(read_rating))

    media_infile.close()
    ratings_infile.close()

    return rating_list, media_list


def calculate_similarity(media_position, rating_list, media_list):
    highest_score, new_score = 0, 0
    most_similar_title = 0

    # Given a specific media, calculate the media with the most similar rating
    for i in range(len(media_list)):
        new_score = similarity(rating_list[media_position], rating_list[i])
        # Store highest score and return the media that is first listed in the file if there is a tie
        if new_score > highest_score and media_position != i:
            highest_score = new_score
            most_similar_title = media_list[i]

    return most_similar_title, highest_score


def main():
    outfile = open("most-similar-media.txt", "w")

    # Read the file
    rating_list, media_list = read_files()

    # Calculate the similarity between two media and print the results
    for i in range(len(media_list)):
        source_media_title = media_list[i]
        most_similar_title, similarity_score = calculate_similarity(
            i, rating_list, media_list)
        formatted_message = format_similar_message(
            source_media_title, most_similar_title, similarity_score)
        outfile.write(formatted_message + '\n')

    outfile.close()


if __name__ == "__main__":
    main()
