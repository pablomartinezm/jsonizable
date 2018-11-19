# Jsonizable
Jsonizable is a python library that allows to parse json objects into python classes and vice versa. This is really helpful to deal with complex APIs that return long JSON objects.

The Jsonizable class allows the user to insert logic in JSONs recieved by external servers and it's really helpful in the data integrity check with only two methods `write` and `read`.

__Guide:__
* [Quickstart](#quickstart)
* [Collections](#collections)
* [Optional Parameters](#optional-parameters)
* [Nested Objects](#nested-objects)

## Quickstart

The recommended way to use this package is defining data schemas for each class. To do this we will need to implement a `Meta`class inside our object and there define a `schema`, which is a dictionary containing the name and type of our JSON object.

```python
class Car(Jsonizable):
    class Meta:
        schema = dict(
            name=str,
            model=str,
            year=int,
            max_speed=float,
            is_new=bool,
        )
```

By doing this we will be able to parse and serialize the `Car` object into JSON.

```python
json = {
    "name": 'Tesla',
    "model": 'v6',
    "year": 2017,
    "max_speed": 186.63,
    "is_new": True,
}

# Parse the JSON object into a car
my_car = Car(json=json)
print(my_car.name)
>> Tesla

print(my_car.year)
>> 2017

#Serialize the Car into a JSON object
my_car.write()
>> { "name": "Tesla", "model": "v6", "year": 2017, "max_speed": 186.63, "is_new": True }
```

## Collections

It is also posible to define collections for our Jsonized classes. We can define dictionaries, tuples and lists with generic types:

```python
class MyJsonizableClass(Jsonizable):
    class Meta:
        schema = dict(
            some_list=list,
            some_tuple=tuple,
            some_dict=dict,
        )

json = {
    some_list: [1, 2, "Forest", 4],
    some_tuple: [1, 2.23, 3, "hello"],
    some_dict: {
        "name": "John Doe",
        4: "Martin Lee",
    },
}

obj = MyJsonizableClass(json=json)

```

And again we will receive an object with it's inner parameters.

But, in the most of the cases we will want to provide the collection a type, that will be checked. We can force the types as follows:

```python
class Lottery(Jsonizable):
    class Meta:
        schema=dict(
            first_prize=int,
            second_prizes=[int],
            third_prizes=(int, ),
        )

json = {
    "first_prize": 24666123,
    "second_prizes": [1244123, 4551235512, 32341234],
    "third_prizes": [2344123, 412555123, 234444512, 12333415],
}

obj = Lottery(json=json)
```

## Optional Parameters
Sometimes our objects will have some optional parameters, that obviously cannot be sent as `None`to the API because the validator inmediatly explodes. In this case we will probably want to define optional parameters, to do so we will end the parameter name with a question marker `my_param?` as the example below:

```python
class MyQuanticClass(Jsonizable):
    class Meta:
        schema={
            "name": str, # This is mandatory parameter
            "state?": int, # This is an optional parameter
        }

json1 = {
    "name": "Electron",
}

class1 = MyQuanticClass(json=json1)

json2 = {
    "name": "Proton",
    "state": 3,
}
 class2 = MyQuanticClass(json=json2)

```

Works like charm ;).

## Nested Objects

Ok, it was easy until now, simple objects and simple interfaces.  What happens when we deal with nasty hard nested objects. To do so you can simply define a hierarchy of objects and tell the parent the type of the son.  (Better with an example, huh?)

```python
# Define a parent class
class PetShop(Jsonizable):
    class Meta:
        schema={
            "name": str,
            "pets": [Pet],
        }

# Define the subclass
class Pet(Jsonizable):
    class Meta:
        schema={
            "species": str,
            "name": str,
            "price": float,
        }

json={
    "name": "Funny puppies",
    "pets": [
        {
            "species": "dog",
            "name": "Tobby",
            "price": 150,
        },
        {
            "species": "bird",
            "name": "Mr. Tingles",
            "price": 20,
        }
    ]
}

pet_shop = PetShop(json=json)
print(pet_shop.pets[1].name)
>> Mr. Tingles
```