from typing import List, Tuple
from state.state import Action, State, StartState, EndState

class FiniteStateMachine:
    """
    Finite State Machine
    """

    def __init__(self, startState: StartState, states: List[State]) -> None:
        """Initialize FiniteStateMachine

        Args:
            startState (StartState): the start state of the FSM
            states (List[State]): all defined state of the FSM
        """

        self.currentState   = startState
        self.states         = states
        self.isEnable       = True

        if self.currentState not in self.states:
            self.states.append(self.currentState)

    def run_one_transition(self, action: Action) -> None:
        """Run one round to input the action to the FSM

        Args:
            action (Action): input action
        """
        
        previousState = self.currentState
        self.currentState = self.currentState.nextState(action)
        print(f'{previousState} --{action}--> {self.currentState}')

        if self.currentState.isEnd:
            self.isEnable = False

    def run_transitions(self, actions: List[Action]) -> None:
        """Run multiple rounds to input list of actions to the FSM

        Args:
            actions (List[Action]): _description_
        """

        for action in actions:
            if not self.isEnable:
                break
            self.run_one_transition(action)



