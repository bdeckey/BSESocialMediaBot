from InstagramAPI import InstagramAPI
user, pwd = 'user', 'pwd'

InstagramAPI = InstagramAPI(user, pwd)
InstagramAPI.login()  # login

photo_path = 'bob.jpg'
caption = "Sample photo"
InstagramAPI.uploadPhoto(photo_path, caption)
