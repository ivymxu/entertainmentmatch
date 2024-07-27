"""
Reads the files media.txt and ratings.txt and then for each media, outputs to a file
named most-similar-media.txt the most similar media and the similarity score
Excerpt of example output: 
    People who liked The Hitchhiker's Guide To The Galaxy, also liked Ender's Game. (Score = 0.805)
    People who liked Watership Down, also liked The Summer Tree. (Score = 0.609)
    People who liked The Five People You Meet in Heaven, also liked Bone Series. (Score = 0.471)
    People who liked Speak, also liked My Sister's Keeper. (Score = 0.889)
"""

from recsys import *


def format_similar_message(source_media_title,
                           most_similar_title,
                           similarity_score):
    """Function to produce a properly formatted string for output of Problem1."""
    result = f'People who liked {source_media_title}, ' + \
             f'also liked {most_similar_title}. (Score = {similarity_score:.3f})'
    return result


def read_files():
    """Reads the files and stores each media and rating in a list
    """

    media_infile = open("media.txt", "r")
    ratings_infile = open("ratings.txt", "r")

    media_list = []
    rating_list = []

    # Adding the media title and creating lists within the rating list
    media_length = len(media_infile.readlines())
    user_length = len(ratings_infile.readlines()) 

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
    """Determines the highest rating between two media using the similarity function
    """
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
    """Prints the most similar media and their ratings"""
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
