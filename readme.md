simple locust run

```sh
python -m locust -f test.py
```

for running distributed way

```sh
python -m locust -f test.py  --master 
```

add worker to master

```sh
python -m locust -f test.py --worker --master-host=localhost
```
