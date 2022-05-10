from ..model import User,Post,Session,engine,exc

class Posts_Route:
    def __init__(self):
        self.local_session = Session(bind=engine)
        self.count = 1
#Function to create add new posts 

    def add_post(self,user_id,title,description):
        try:
            self.post = Post(post_name=title,author_id=user_id)    
            self.local_session.add(self.post)
            self.local_session.commit()
            return {"status":"Success"}
        except:
            print("error")
            return {"status":"not"}
            

# Function to show posts by user

    def show_posts_by_user(self,id):
            try:
                self.result = self.local_session.query(User).join(Post).filter(User.id==id and Post.author_id==User.id)
                if self.result:
                    print("exists")
                    for user in self.result:
                        for post in user.posts:
                         print(user.id,post.post_name)
                    return {"message":"Posts exists",
                            "status":"Success"}
                else:
                    print("not exists")
           
                # return {"message":"Success"}
            except:
                return {"message":"false"}
                    
