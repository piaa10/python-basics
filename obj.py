from users import *
from post import *

user1 = Users("xyz@xyz", "Priya Belhkear", "passwprd", "Devops Eng")
user1.get_infor()
user1.change_title("Senior Devops Engineer")
user1.get_infor()

new_post = Post("on a secret mission", user1.name)
new_post.get_post_info()