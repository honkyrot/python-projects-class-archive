import build_user
from build_user import build_profile
from build_user import build_profile as bp
import build_user as bu
from build_user import *

user_profile = build_user.build_profile('Hong', 'Rot',
                                        location='Fort Wayne',
                                        came_from="Southeast Asian",
                                        field='Software Developer',
                                        likes='Games & Anime',
                                        plays='Apex Legends & Rocket League')  # I like lots of games!
print(user_profile)  # uses import

user_profile = build_profile('Hong', 'Rot',
                             location='Fort Wayne',
                             came_from="Southeast Asian",
                             field='Software Developer',
                             likes='Games & Anime',
                             plays='Apex Legends & Rocket League')  # I like lots of games!
print(user_profile)  # uses from, import

user_profile = bp('Hong', 'Rot',
                  location='Fort Wayne',
                  came_from="Southeast Asian",
                  field='Software Developer',
                  likes='Games & Anime',
                  plays='Apex Legends & Rocket League')  # I like lots of games!
print(user_profile)  # uses from, import, and as

user_profile = bu.build_profile('Hong', 'Rot',
                  location='Fort Wayne',
                  came_from="Southeast Asian",
                  field='Software Developer',
                  likes='Games & Anime',
                  plays='Apex Legends & Rocket League')  # I like lots of games!
print(user_profile)  # uses import, and as
