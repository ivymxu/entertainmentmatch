# Entertainment Similarity Algorithm

This program implements an algorithm to find the most similar entertainment item (book, film, music) based on user ratings from a given list. The similarity is determined by analyzing user-submitted ratings and comparing them to identify the most closely related item.

**How It Works**
1. The program reads two files:
  * `media.txt` contains the list of entertainment items.
  * `ratings.txt` contains user ratings for each item.
2. The ratings are processed to find the item that is most similar to a given one based on user preferences.
3. The results are outputted to a file named `most-similar-media.txt`, showing the number of ratings for each score.
