from InstagramAPI import InstagramAPI
user, pwd = 'hear_from_bruno', 'groundsoftware'

InstagramAPI = InstagramAPI(user, pwd)
InstagramAPI.login()  # login

photo_path = 'bob.jpg'
caption = "Sample photo"
InstagramAPI.uploadPhoto(photo_path, caption)
