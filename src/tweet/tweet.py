from utils.convert import convert_tweet_string_to_date


class Tweet(object):
    """Class represents tweet from Twitter.

    Attributes:
        tweet_id: A unique identifier.
        created_at: A date-time, describing when the tweet was sent.
        text: A string, containing the message of the tweet.
        is_retweet: A boolean, stating whether it is a retweet.
        retweet_count: An integer, stating the number of retweets.
        favorite_count: An integer, stating the number of favorites.
    """

    def __init__(self, tweet_id, created_at, text, is_retweet, retweet_count, favorite_count):
        """Initializes tweet object with defined content."""
        self.tweet_id = tweet_id
        self.created_at = created_at
        self.text = text
        self.is_retweet = is_retweet
        self.retweet_count = retweet_count
        self.favorite_count = favorite_count

    def __str__(self):
        """Creates user-friendly string representation of tweet."""

        return "Tweet id: {}\nCreated at: {}\nIs retweet: {}\nRetweet count: {}\nFavorite count: {}\nText:\n{}".\
            format(self.tweet_id, self.created_at, self.is_retweet, self.retweet_count, self.favorite_count, self.text)

    def __eq__(self, other):
        """
        Determines if tweet is equal to other tweet.

        Compares the tweet_id value. Returns True if tweet_ids are equal.
        """
        return self.tweet_id == other.tweet_id

    def __hash__(self):
        """
        Returns a unique hash value.
        """
        return hash(self.tweet_id)

    def count_number_of_words(self):
        """
        Counts the words in the tweet.

        Retrieves the text from the tweet, splits it by spaces and counts
        the length of the list.

        Returns:
            An interger value, corresponding to the number of words in the tweet.
        """
        word_list = self.text.split()
        return len(word_list)

    def calculate_popularity(self):
        """
        Calculates the popularity of the tweet.

        Sums up the number of retweets and favorites.

        Returns:
            An interger value, corresponding to the popularity of the tweet.
        """
        return self.retweet_count + self.favorite_count


def create_tweet_from_dict(tweet_dict):
    """
    Creates a tweet object from dictionary.

    Extracts tweet_id, created_at, text, is_retweet,
    retweet_count and favorite_count from dictionary.

    Args:
        tweet_dict: A dictionary, containing tweet information.

    Returns:
        A tweet object.
    """
    # Extract parameters from dictionary
    tweet_id = tweet_dict.get('id_str')
    created_at = convert_tweet_string_to_date(tweet_dict.get('created_at'))
    text = tweet_dict.get('text')
    is_retweet = tweet_dict.get('is_retweet')
    retweet_count = tweet_dict.get('retweet_count')
    favorite_count = tweet_dict.get('favorite_count')

    # Create tweet object
    tweet = Tweet(tweet_id, created_at, text, is_retweet, retweet_count, favorite_count)

    return tweet
