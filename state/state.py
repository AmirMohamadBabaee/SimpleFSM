from exception.state_exceptions import NoTransitionWithThisAction
from __future__ import annotations


class Action:
    """
    Action to change state based on
    """

    def __init__(self, name) -> None:
        self.name = name


class State:
    """FSM state
    """

    def __init__(self, name: str, isStart: bool=False, isEnd: bool=False) -> None:
        """initialize state

        Args:
            name (str): the name of the state
            isStart (bool, optional): determine whether the state is start state. Defaults to False.
            isEnd (bool, optional): determine whether the state is end state. Defaults to False.
        """

        self.name           = name
        self.transitions    = {}
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

        next_state = self.transitions.get(Action)
        if not next_state:
            raise NoTransitionWithThisAction(self, action)
        
        return next_state


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
        