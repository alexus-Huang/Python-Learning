#8-9. Messages
short_text_msgs = ["hello","hi","a messaage"]
printed_text_msgs = []
def show_messages(text_msgs):
    while text_msgs:
        show_text_msgs = text_msgs.pop()
        print(f"{show_text_msgs}")
        printed_text_msgs.append(show_text_msgs)

show_messages(short_text_msgs)