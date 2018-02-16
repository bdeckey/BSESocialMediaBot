import facebook
from credentials import *

def main():
  # Fill in the values noted in previous steps here
  cfg = {
    "page_id"      : page_id,  # Step 1
    "access_token" : access_token   # Step 3
    }
  
  graph = facebook.GraphAPI(access_token=access_token, version="2.7")
  with open('/Users/jacobbegemann/Documents/BSESocialMediaBot/Bots/Blastoff.jpg') as image_ref:
    status = graph.put_photo(image=image_ref,
                message='Blast off!')

if __name__ == "__main__":
  main()
