# go2RL

### Setting up the environment

1. Create a workspace folder 

2. Create a virtual environment

```
python3 -m venv <name of virtual environment>
```

3. Activate the virtual environment

```
source <name of virtual environment>/bin/activate
```

4. Install necessary libraries

```
pip install -r requirements.txt
```

5. Clone the rsl_rl repository found here https://github.com/leggedrobotics/rsl_rl/tree/main

6. Install the python package

```
cd rsl_rl
pip install -e .
```

7. Go back to the workspace

```
cd ..
```

8. Clone the genesis repository found here https://github.com/Genesis-Embodied-AI/Genesis/tree/main

9. Follow installation instructions here https://genesis-world.readthedocs.io/en/latest/user_guide/overview/installation.html

9. Go into the main directory

```
cd go2RL/
```

10. Run the training script

```
python go2_train.py
```

11. Run the evaluation script

```
python go2_eval.py
```


