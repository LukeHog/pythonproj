def greet(name):
    """
    This function greets to the person
    passed in as a parameter
    :param name: name
    :return: NiL
    """
    print("Hello, " + name + ". Good Morning!")
    return None

ip = input("Enter a name: ")
greet(ip)