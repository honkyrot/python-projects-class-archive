txt_msg = ["Yo what do you think of the new meme",
           "🔥🔥🔥✍️✍️✍️🔥🔥🔥",
           "💀💀💀",
           "peak fiction",
           "yeah"]  # 2022 text messaging

sent_msg = []


def show_msg(msg):
    for index, txt in enumerate(msg):
        print(txt)
        sent_msg.append(txt)


show_msg(txt_msg.copy())
print(f"sent msg: {sent_msg}")  # sent messages
print(f"archived msg: {txt_msg}")  # txt_msg old list, should NOT be empty
