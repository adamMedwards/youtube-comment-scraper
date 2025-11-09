thonimport requests

def parse_youtube_comments(video_url, limit=10, include_replies=False):
    # In a real case, implement YouTube comment extraction logic
    comments = [
        {
            "content": "Great video!",
            "author": "User1",
            "commentId": "comment_id_1",
            "publishedTime": "1 day ago",
            "likeCount": 10,
            "replyCount": 0
        },
        {
            "content": "Thanks for sharing!",
            "author": "User2",
            "commentId": "comment_id_2",
            "publishedTime": "2 days ago",
            "likeCount": 5,
            "replyCount": 1
        }
    ]
    return comments