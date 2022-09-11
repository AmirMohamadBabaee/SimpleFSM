from __future__ import annotations
from typing import Dict
from exception.state_exceptions import ActionAlreadyExists, NoTransitionWithThisAction


class Action:
    """
    Action to change state based on
    """

    def __init__(self, name: str) -> None:
        """Initialize Action

        Args:
            name (str): the name of the action
        """

        self.name = name

    def __str__(self) -> str:
        return f'({self.name})'

    def __repr__(self) -> str:
        return self.__str__()


class State:
    """FSM state
    """

    def __init__(self, name: str, transitions: Dict[Action, State]=None, isStart: bool=False, isEnd: bool=False) -> None:
        """initialize state

        Args:
            name (str): the name of the state
            transitions (Dict[Action, State]): mapping between the current state and next state based on input action
            isStart (bool, optional): determine whether the state is start state. Defaults to False.
            isEnd (bool, optional): determine whether the state is end state. Defaults to False.
        """

        self.name           = name
        self.transitions    = transitions if transitions else dict()
        self.isStart        = isStart
        self.isEnd          = isEnd

    def nextState(self, action: Action) -> State:
        """determine next state based on input action and transitions dictionary

        Args:
            action (Action): Input action

        Raises:
            NoTransitionWithThisAction: raise when current action not defined in the state

        Returns:
            State: next state based on transitions dictionary
        """

        next_state = self.transitions.get(action)
        if not next_state:
            raise NoTransitionWithThisAction(self, action)
        
        return next_state

    def addTransition(self, action: Action, next_state: State) -> None:
        """add new transition pair (action, next_state) to the current state

        Args:
            action (Action): input action in transition
            next_state (State): next state based on the action

        Raises:
            ActionAlreadyExists: raise when the action already exists in the transitions dictionary
        """

        if action in self.transitions:
            raise ActionAlreadyExists(action)

        self.transitions[action] = next_state

    def __str__(self) -> str:
        return f'[[{self.name}]]'

    def __repr__(self) -> str:
        return self.__str__()


class StartState(State):
    """State class with isStart attribute enabled

    Parents:
        State : FSM state
    """

    def __init__(self, name: str) -> None:
        """Initialize StartState

        Args:
            name (str): the name of the state
        """
        super().__init__(name, isStart=True)

    def __str__(self) -> str:
        return f'[#[{self.name}]#]'


class EndState(State):
    """State class with isEnd attribute Enabled

    Parents:
        State : FSM state
    """

    def __init__(self, name: str) -> None:
        """Initialize EndState

        Args:
            name (str): the name of the state
        """
        super().__init__(name, isEnd=True)

    def __str__(self) -> str:
        return f'[![{self.name}]!]'
