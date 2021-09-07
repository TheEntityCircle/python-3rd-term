def foo():
    print("Foo is working, context", __name__)

print("Top level code is working, context", __name__)
foo()
