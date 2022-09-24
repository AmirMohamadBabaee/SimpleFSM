"""
Demo Implementation of a simple fsm which convert alphabetical numbers
to their numerical forms.
"""

from state.machine import FiniteStateMachine
from state.state import Action, State, StartState, EndState

text2num = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10
}

# initialize states
start_state         = StartState('start')
normal_text_state   = State(name='normal_text', handler=lambda x: x)
number_text_state   = State(name='number_text', handler=lambda x: text2num[x])
end_state           = EndState('end')

total_states = [start_state] +          \
                [normal_text_state] +   \
                [number_text_state] +   \
                [end_state]

is_number_action    = Action('is_number')
is_text_action      = Action('is_text')
is_eos_action       = Action('is_eos')

# set transitions
start_state.add_transition(is_number_action, number_text_state)
start_state.add_transition(is_text_action, normal_text_state)
start_state.add_transition(is_eos_action, end_state)

normal_text_state.add_transition(is_number_action, number_text_state)
normal_text_state.add_transition(is_text_action, normal_text_state)
normal_text_state.add_transition(is_eos_action, end_state)

number_text_state.add_transition(is_number_action, number_text_state)
number_text_state.add_transition(is_text_action, normal_text_state)
number_text_state.add_transition(is_eos_action, end_state)

# initialize FSM
fsm = FiniteStateMachine(start_state, total_states)

INPUT_STR = 'this is one of our goals in ten years'
print(f'INPUT: {INPUT_STR}')
print()
input_list = INPUT_STR.split() + ['<eos>']

def token2action_handler(token: str) -> Action:
    """simple handler to generate action based on
    current token.

    Args:
        token (str): input token

    Returns:
        Action: generated action
    """
    if token in text2num:
        return is_number_action
    if token == '<eos>':
        return is_eos_action

    return is_text_action

actions = list(map(token2action_handler, input_list))

FINAL_OUTPUT = ''
for i, action in enumerate(actions):
    fsm.run_one_transition(action)
    if fsm.is_enable:
        FINAL_OUTPUT += f'{fsm.current_state(input_list[i])} '

print()
print(f'OUTPUT: {FINAL_OUTPUT}')
