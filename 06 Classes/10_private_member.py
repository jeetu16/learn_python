class TagCloud:
    def __init__(self):
        # __tags denotes it is a private member attribute of class
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("Javascript")
cloud.add("javascript")
cloud.add("javascript")
print(cloud["JAVASCRIPT"])
# To prevent private member from accidental access.
print(cloud.__tags)
# To access private member attribute
print(cloud._TagCloud__tags)
