
from hashlib import new
from os import stat
from fastapi import FastAPI,Form,Depends, HTTPException,Response,status
from fastapi.params import Body
from pydantic import BaseModel
from . schemas import Post,Users
from . routers.user import User_Controller
from . routers.posts import Posts_Route
from . model import engine,Base

app = FastAPI()
ob1 = User_Controller()
obPost = Posts_Route()

@app.get("/")
def read_root():
    print("Database created")
    Base.metadata.create_all(engine)
    return {"message","hello world"}



# Function To Create Users

@app.post("/createuser",status_code=status.HTTP_201_CREATED)
async def create_user(new_user:Users = Depends(Users.as_form)):
    print("username:",new_user.username)
    print("email:",new_user.email)
    print("Sponser id:",new_user.sponser_id)
    print("address:",new_user.adrs)




# Calling User Function to create new user
    try:
    
        result = ob1.add_user(new_user.username,new_user.email,new_user.sponser_id,new_user.adrs)
        print(result.get("message"))
        return {'message':'successfully created users'}
    except:
        return {'message':'not created',
                'error':result.get("error")}
    
    
    
    
 
#Retrieving user details 
 
@app.get("/users/{id}")
def get_user(id:int,response:Response):
    print(type(id))
    # using User_controller to call user_details information

    user_details = ob1.show_user(id)
    if user_details:
        return{'message':'success',
               'id':user_details.get("id"),
               'username':user_details.get("username")}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {id} not found")






#Delete User Details
 
@app.delete("/deleteuser/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id:int):
    user = ob1.delete_user(id)
    if user.get("message") == "success":
        print("Deleteted")
        return {"message":"true"}
       
    else:
        print("Not Deleteted")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {id} not found")
     
     
     
     
     
        
# Updating user details

@app.put("/updateuser/{id}")
def update_user(id:int,update_user:Users = Depends(Users.as_form)):
    print(id)
    updated_user = ob1.update_user(id,update_user.adrs)
    if updated_user.get("message") == "success":
        return {
            'message':'updated user successfully',
            'address':update_user.adrs
        }
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {id} doesn't exist")






#Function to create posts
    
@app.post("/createposts")
async def create_posts(new_post: Post = Depends(Post.as_form)):

        status_rtn = obPost.add_post(new_post.user_id,new_post.title,new_post.description)
        if status_rtn.get("status")=="Success":
            return {'message':'successfully created posts'}
        else:
            print(status_rtn.get("status"))
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {new_post.user_id} doesn't exist")






#Function to show_posts by user id

@app.get("/show_posts/{id}")
def show_posts(id:int,response:Response):
    
    print("id",id)
    post = obPost.show_posts_by_user(id)
    if post.get("status")=="Success":
        return {"message":post.get("message")}
    else:
        return {"message":"not"}
