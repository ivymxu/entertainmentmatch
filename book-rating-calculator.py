
"""
This program reads the files books.txt and ratings.txt and then for each book, outputs to a file
named most-similar-books.txt the most similar book and the similarity score
Excerpt of example output: 
    People who liked The Hitchhiker's Guide To The Galaxy, also liked Ender's Game. (Score = 0.805)
    People who liked Watership Down, also liked The Summer Tree. (Score = 0.609)
    People who liked The Five People You Meet in Heaven, also liked Bone Series. (Score = 0.471)
    People who liked Speak, also liked My Sister's Keeper. (Score = 0.889)
"""

from recsys import *


def format_similar_message(source_book_title,
                           most_similar_title,
                           similarity_score):
    """Function to produce a properly formatted string for output of Problem1."""
    result = f'People who liked {source_book_title}, ' + \
             f'also liked {most_similar_title}. (Score = {similarity_score:.3f})'
    return result


def read_files():
    """Reads the files and stores each book and book rating in a list
    Excerpt of lists:
    book_list = ['The Hitchhiker's Guide To The Galaxy', 'Watership Down', ...]
    rating_list = [[5, 5, 5, ...], [0, 5, -5, ...], ...]
    """

    books_infile = open("books.txt", "r")
    ratings_infile = open("ratings.txt", "r")

    book_list = []
    rating_list = []

    # Adding the book title and creating lists within the rating list
    book_length = 53
    user_length = 32

    for i in range(book_length):
        read_book = books_infile.readline().strip()
        book_list.append(read_book)
        rating_list.append([])

    # Adding ratings for each book within each rating list
    for i in range(user_length):
        ratings_infile.readline()
        for j in range(book_length):
            read_rating = ratings_infile.readline().strip()
            rating_list[j].append(int(read_rating))

    books_infile.close()
    ratings_infile.close()

    return rating_list, book_list


def calculate_similarity(book_position, rating_list, book_list):
    """Determines the highest rating between two books using the similarity function
    Input: book placement in the book list, list of book ratings and books created in read_files()
    Output: most similar book, highest similarity score
    """
    highest_score, new_score = 0, 0
    most_similar_title = 0

    # Given a specific book, calculate the book with the most similar rating
    for i in range(len(book_list)):
        new_score = similarity(rating_list[book_position], rating_list[i])
        # Store highest score and return the book that is first listed in the file if there is a tie
        if new_score > highest_score and book_position != i:
            highest_score = new_score
            most_similar_title = book_list[i]

    return most_similar_title, highest_score


def main():
    """Using the above functions, prints the most similar books and their ratings"""
    outfile = open("most-similar-books.txt", "w")

    # Read the file
    rating_list, book_list = read_files()

    # Calculate the similarity between two books and print the results
    for i in range(len(book_list)):
        source_book_title = book_list[i]
        most_similar_title, similarity_score = calculate_similarity(
            i, rating_list, book_list)
        formatted_message = format_similar_message(
            source_book_title, most_similar_title, similarity_score)
        outfile.write(formatted_message + '\n')

    outfile.close()


if __name__ == "__main__":
    main()
