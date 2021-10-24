from db import get_config
from do_action_type import perform_selection

if __name__ == '__main__':
    prompt = get_config('prompt')['prompt']
    selection = input(prompt)
    while selection != 'q':
        perform_selection(selection)
        selection = input(prompt)

    print('goodbye!')
