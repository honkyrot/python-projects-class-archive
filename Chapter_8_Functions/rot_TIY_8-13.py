def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('Hong', 'Rot',
                             location='Fort Wayne',
                             came_from="Southeast Asian",
                             field='Software Developer',
                             likes='Games & Anime',
                             plays='Apex Legends & Rocket League')  # I like lots of games!
print(user_profile)
