```
**Setting up the environment
```
# pip install virtualenv
# virtualenv venv
# . venv/bin/activate
# pip install -r requirements.txt

```
**Running initial node
```
# python run.py <host ip>

```
**Joining an existing network
```
# python run.py <host ip> <seed ip>

Mac OSX requires you to run `sudo ifconfig lo0 alias <ip> up` for each IP
