# SimpleFSM
Implementation of a simple Finite State Machine.

# How to use it?
To better understand how you can use this package, I prepared an implemented FSM demo in [`demo.py`](./demo.py). You can check it.

## 1) Define `States`
You should define three types of states.
* At least 1 `StartState`
* Ordinary `State` (instantiate as many as you need)
* At least 1 `EndState`

```python
# initialize states
start_state     = StartState('start')
normal_state_1  = State(name='normal_state_1', handler=normal_state_1_handler)
...
normal_state_N  = State(name='normal_state_N', handler=normal_state_N_handler)
end_state       = EndState('end')
```

then aggregate them in a list variable.

```python
total_states = [start_state] +          \
                [normal_states] +       \
                [end_state]
```

## 2) Define `Actions`
The next thing you need is to define new actions to define the relations between FSM states.

```python
#initialize actions
action_1  = Action('aciton_1')
...
action_M  = Action('action_M')
```

## 3) Define Transitions
Then, You need explicitly define the relationship between two states based on initialized actions.

```python
# set transitions
start_state.add_transition(action_1, normal_state_1)
start_state.add_transition(action_2, normal_state_2)
...
normal_state_1.add_transition(action_3, normal_state_3)
normal_state_2.add_transition(action_4, normal_state_4)
...
normal_state_N.add_transition(action_M, end_state)
```

## 4) Instantiate `FiniteStateMachine`
Instantiate `FiniteStateMachine` and then pass the start_state and list of entire states as arguments.
```python
#Initialize FiniteStateMachine
fsm = FiniteStateMachine(start_state, total_states)
```

## 5) Using `run_one_transition` or `run_transitions`
```python
# for an action transition
fsm.run_one_transition(action_1)

# for a list of actions transitions
fsm.run_transitions([action_1, ..., action_N])
```

# Final Note
If you found any bugs or have any suggestions to improve the functionality of this package, raise an issue.
