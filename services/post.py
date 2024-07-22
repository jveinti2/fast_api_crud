
from models.post import Post as PostModel

class PostServices():
    
    def __init__(self, db) -> None:
        self.db = db
    
    def get_posts(self):
        return self.db.query(PostModel).all()
    
    def get_post(self, post_id):
        return self.db.query(PostModel).filter(PostModel.id == post_id).first()
    