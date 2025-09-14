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
    msg.clear()


show_msg(txt_msg)
print(sent_msg)  # sent messages
print(txt_msg)  # txt_msg old list, should be empty
