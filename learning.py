# #8-9. Messages
# short_text_msgs = ["hello","hi","a messaage"]
# printed_text_msgs = []
# def show_messages(text_msgs):
#     while text_msgs:
#         show_text_msgs = text_msgs.pop()
#         print(f"{show_text_msgs}")
#         printed_text_msgs.append(show_text_msgs)

# show_messages(short_text_msgs)

#8-10. Sending Messages:
send_text_msgs = ["hello","hi","a messaage"]
sent_txt_msgs = []
def show_messages(text_msgs):
    while text_msgs:
        show_text_msgs = text_msgs.pop()
        print(f"{show_text_msgs}")
        sent_txt_msgs.append(show_text_msgs)
show_messages(send_text_msgs)
print(send_text_msgs)
print(sent_txt_msgs)