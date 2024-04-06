language_poll_takers={
    "john":"english",
    "bob":"spanish",
    "david":"english"
}

should_take_poll=["john","jack","bob","david"]

for needed_takers in should_take_poll:
    if needed_takers in language_poll_takers.keys():
        print(f"{needed_takers} has taken the poll")
    else:
        print(f"{needed_takers} still hasn't taken the poll")