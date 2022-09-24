"""
This module has the implementation of States and Actions objects
"""

from __future__ import annotations
from typing import Any, Callable, Dict
from exception.state_exceptions import (
    ActionAlreadyExists,
    NoHandlerSet,
    NoTransitionWithThisAction
)


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

    def __init__(self,                                  \
                name: str,                              \
                transitions: Dict[Action, State]=None,  \
                handler: Callable=None,                 \
                is_start: bool=False,                   \
                is_end: bool=False                      \
        ) -> None:
        """initialize state

        Args:
            name (str): the name of the state
            transitions (Dict[Action, State]): mapping between the current state and
            next state based on input action

            handler (Callable): function to be run when the flow reaches the state
            is_start (bool, optional): determine whether the state is start state.
                Defaults to False.
            is_end (bool, optional): determine whether the state is end state.
                Defaults to False.
        """

        self.name           = name
        self.transitions    = transitions
        self.handler        = handler
        self.is_start        = is_start
        self.is_end          = is_end

        if not self.transitions:
            self.transitions = {}

    def next_state(self, action: Action) -> State:
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

    def add_transition(self, action: Action, next_state: State) -> None:
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

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if not self.handler:
            raise NoHandlerSet(self)

        return self.handler(*args, **kwds)

    def __str__(self) -> str:
        return f'[[{self.name}]]'

    def __repr__(self) -> str:
        return self.__str__()


class StartState(State):
    """State class with is_start attribute enabled

    Parents:
        State : FSM state
    """

    def __init__(self, name: str) -> None:
        """Initialize StartState

        Args:
            name (str): the name of the state
        """
        super().__init__(name, is_start=True)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print('Start State')

    def __str__(self) -> str:
        return f'[#[{self.name}]#]'


class EndState(State):
    """State class with is_end attribute Enabled

    Parents:
        State : FSM state
    """

    def __init__(self, name: str) -> None:
        """Initialize EndState

        Args:
            name (str): the name of the state
        """
        super().__init__(name, is_end=True)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print('End State')

    def __str__(self) -> str:
        return f'[![{self.name}]!]'
