import time
import datetime


class Posts:
    """Creates Posts object from pushshift link. """

    def __init__(self, query='', sort='desc', size=25, after=0, before=int(time.time()), subreddit=''):
        """
        Parameters
        ----------
        query: Not supported (look at pushshift docs).
        sort: Descending or ascending. Defaults to 'desc'.
        size: Number of objects in API call (max 1000 per call).
        after(int): Unix timestamp.
        before(int): Unix timestamp.
        subreddit: Subreddit, if '' then r/all.

        """
        self.query = query
        self.sort = sort
        self.size = size
        self.after = after
        self.before = before
        self.sub = subreddit

    def make_url(self):
        url = 'https://api.pushshift.io/reddit/search/submission/?q={}&size={}&sort={}&after={}&before={}&subreddit={}'.\
               format(self.query, self.size, self.sort, self.after, self.before, self.sub)
        return url


class Comments(Posts):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def make_url(self):
        url = 'https://api.pushshift.io/reddit/search/comment/?q={}&size={}&sort={}&after={}&before={}&subreddit={}'.\
               format(self.query, self.size, self.sort, self.after, self.before, self.sub)
        return url


class Post:
    """Makes Post from dict (json)."""

    def __init__(self, author, created_utc, post_id, num_comments, score, subreddit, title, selftext):
        self.author = author
        self.created_utc = created_utc
        self.post_id = post_id
        self.num_comments = num_comments
        self.score = score
        self.subreddit = subreddit
        self.title = title
        self.selftext = selftext
        self.is_post = True

    @staticmethod
    def make_post_obj(post):
        return Post(post['author'], post['created_utc'], post['id'], post['num_comments'], post['score'],
                    post['subreddit'], post['title'], post['selftext'])


class Comment:

    def __init__(self, author, body, created_utc, link_id, parent_id, score, subreddit):
        self.author = author
        self.body = body
        self.created_utc = created_utc
        self.link_id = link_id
        self.parent_id = parent_id
        self.score = score
        self.subreddit = subreddit
        self.is_post = False

    @staticmethod
    def make_comment_obj(comment):
        return Comment(comment['author'], comment['body'], comment['created_utc'], comment['link_id'],
                       comment['parent_id'], comment['score'], comment['subreddit'])
