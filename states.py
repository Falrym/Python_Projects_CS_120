def main():
    states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia",
        "Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
        "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire",
        "New Jersey","New Mex ico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
        "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington",
        "West Virginia","Wisconsin","Wyoming"]
    number_of_letters = int(input("Enter a number for a list of states: "))
    new_states = get_states_by_length(number_of_letters,states)
    print(f"Number of states with at least {number_of_letters} letters: {len(new_states)}")
    for state in new_states:
        print(state)
    new_states2 = get_states_by_spaces(states)
    print(f"The number of states with spaces {len(new_states2)}")
    for state in new_states2:
        print(state)

def get_states_by_length(number,states):
    new_states = []
    for state in states:
        if len(state) >= number:
            new_states.append(state)
    return new_states

def get_states_by_spaces(states):
    new_states2 = []
    for state in states:
        for character in state:
            if character == " ":
                new_states2.append(state)
                break
    return new_states2


main()