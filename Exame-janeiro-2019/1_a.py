def flatten(content):
    return [y for elem in content for y in flatten(elem)] if type(content) == list else [content]

print(flatten([1,[],[range(2,5)],[[["VI"]],["sete"]]]))