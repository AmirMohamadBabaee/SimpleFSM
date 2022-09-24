"""
This module has the implementation of Finite State Machine
(Combination of Actions and States)
"""

from typing import List
from state.state import Action, State, StartState

class FiniteStateMachine:
    """
    Finite State Machine
    """

    def __init__(self, start_state: StartState, states: List[State]) -> None:
        """Initialize FiniteStateMachine

        Args:
            start_state (StartState): the start state of the FSM
            states (List[State]): all defined state of the FSM
        """

        self.current_state   = start_state
        self.states         = states
        self.is_enable       = True

        if self.current_state not in self.states:
            self.states.append(self.current_state)

    def run_one_transition(self, action: Action) -> None:
        """Run one round to input the action to the FSM

        Args:
            action (Action): input action
        """

        previous_state = self.current_state
        self.current_state = self.current_state.next_state(action)
        print(f'{previous_state}\t--{action}--> {self.current_state}')

        if self.current_state.is_end:
            self.is_enable = False

    def run_transitions(self, actions: List[Action]) -> None:
        """Run multiple rounds to input list of actions to the FSM

        Args:
            actions (List[Action]): sequence of input actions
        """

        for action in actions:
            if not self.is_enable:
                break
            self.run_one_transition(action)
