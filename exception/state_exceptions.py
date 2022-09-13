class NoTransitionWithThisAction(Exception):
    """Exception when there is no next state for a defined action in a state

    Args:
        state (state.state.State): current state of the FSM
        action (state.state.Action): Input action 
    """

    def __init__(self, state, action, *args: object) -> None:
        super().__init__(*args)
        self.state = state
        self.action = action

    def __str__(self) -> str:
        return f"NoTransitionWithThisAction: Current State: {self.state} - Input Action: {self.action}"


class ActionAlreadyExists(Exception):
    """Exception when duplicate action tends to be added to the transitions dictionary

    Args:
        action (state.state.Action): Input action 
    """

    def __init__(self, action, *args: object) -> None:
        super().__init__(*args)
        self.action = action

    def __str__(self) -> str:
        return f"ActionAlreadyExists: [{self.action}] already exists in transitions mapping"


class NoHandlerSet(Exception):
    """Exception when calling a state which does not have any handlers

    Args:
        state (state.state.State): current state
    """

    def __init__(self, state, *args: object) -> None:
        super().__init__(*args)
        self.state = state

    def __str__(self) -> str:
        return f"NoHandlerSet: [{self.state}] does not have any handlers"
        