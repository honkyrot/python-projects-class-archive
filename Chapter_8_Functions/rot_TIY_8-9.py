txt_msg = ["Yo what do you think of the new meme",
           "🔥🔥🔥✍️✍️✍️🔥🔥🔥",
           "💀💀💀",
           "peak fiction",
           "yeah"]  # 2022 text messaging

sent_msg = []

def show_msg(msg):
    for txt in msg:
        print(txt)
        sent_msg.append(txt_msg.pop())


show_msg(txt_msg)
print(sent_msg)
