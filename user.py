from .. model import User,Profile,Session,engine,exc,desc

class User_Controller():
    def __init__(self):
        self.local_session = Session(bind=engine)
    def add_user(self,username,email,sponser_id,address):
        try:
            self.add_user = User(username=username, email=email)
            self.local_session.add(self.add_user)
            new_id = self.local_session.query(User).order_by(desc(User.id)).first()
            print("new id:",new_id.id)
            add_profile = Profile(user_id=new_id.id,sponser_id = sponser_id,address = address)
            self.local_session.add(add_profile)
            self.local_session.commit()
            return {'message':'successfully created users',
                    'id':new_id.id}
        except exc.SQLAlchemyError as error:
            print(error)
            return {'message':'not created sqlalchemy error'}
        
    def show_user(self,id):
        try:
            self.user = self.local_session.query(User).filter(User.id == id).first()
            if self.user:
                print("exists")
                print(self.user.username)
                return {"id":self.user.id,"username":self.user.username}
      
        except:
            print("not exists")
        
    def delete_user(self,id):
            try:
                self.user = self.local_session.query(User).filter(User.id == id).first()
                self.local_session.delete(self.user)
                self.local_session.commit()
                return {"message":"success"}
            except:
                return {"message":"not"}
        
    def update_user(self,id,address):
        try:
            self.user = self.local_session.query(Profile).filter(Profile.user_id==id).first()
            self.user.address = address
            self.local_session.commit()
            return {"message":"success"}
        except:
            return {"message":"not"}
