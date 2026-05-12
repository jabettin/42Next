>Note that the subject attached to this module might differ from yours.
>
>They tend to get updated often
>
>Per ex3/ft_plant_factory.py note to **Not** include the json, and just copy the json contents into main as follows:

```python
if __name__ == '__main__':
plant_dict = [
    {"name": "Rose",      "height": 25.0, "age": 21},
    {"name": "Sunflower", "height": 44.3, "age": 19},
    {"name": "Cactus",    "height": 33.1, "age": 30},
    {"name": "Lilly",     "height": 13.5, "age": 18},
    {"name": "Poppy",     "height": 15.2, "age": 24}
]
print("=== Plant Factory Output ===")
    for x in factory(plant_dict):
        x.show()
