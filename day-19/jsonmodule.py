import json 

x = '{"name":"manohar", "age": 24, "branch":"cai","grade":"c"}'

y  = json.loads(x)

print(y["name"])
print(y["age"])
print(y["branch"])
print(y["grade"])

z = {"name":"manohr",
     "age": 24,
     "branch":"cai",
     "grade":"c"}

a = json.dumps(z)
print(a)

# indent:-
# indent in json is used to provide space in begining of every line
# ex:-
x = {
    "name":"manohar",
    "age":24,
    "branch":"cai",
    "grade":"c"
}
y = json.dumps(x,indent=4)
print(y)

# seperators:-
# used to seperate the data using , or provided symbols
# ex:-
x = {
    "name":"manohar",
    "age":24,
    "branch":"cai",
    "grade":"c"
}
y = json.dumps(x, separators=(":",":"))
print(y)