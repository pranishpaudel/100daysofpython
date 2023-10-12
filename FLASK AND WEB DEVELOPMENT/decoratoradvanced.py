class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def authentication_decorator(function):
     def wrapper(*args):
          if args[0].is_logged_in== True:
            function(args[0])
          else:
               print("NOT AUTHENTICATED")
     return wrapper

@authentication_decorator
def create_blog_post(user):
        print(f"This is {user.name}'s new blog post")


new_user = User("pranish")
new_user.is_logged_in=True
create_blog_post(new_user)
