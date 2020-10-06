def foo():
    print("Our __name__ is:",  __name__)
    print("Foo is working")

if __name__ == "__main__":
    print("Our __name__ is:",  __name__)
    print("Top level code is working")
    foo()
