def return_actor(infor):
    name, nationality, age = infor
    return {
        "name": name,
        "nationality": nationality,
        "age": age
    }


data = ("Tom Hardy", "English", 42)
ans = return_actor(data)
print(ans)
