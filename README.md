# py-dotenv
dot env loader

This is created to learn Python.



## How to use

Read env file at same directory.



##### env

```bash
USERNAME=testuser
PASSWORD=testpass # Can use a comment too.
```



##### example

```python
from loader import env_load
env = env_load()

print(env)
print(env["USERNAME"]) # ---> testuser
print(env["PASSWORD"]) # ---> testpass
```



## test

```bash
python -m unittest discover
```

