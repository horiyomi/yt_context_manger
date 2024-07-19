from contextlib import contextmanager


@contextmanager
def sample_context_func():
    print("this is a function")
    yield "The context"


with sample_context_func() as s:
    print("in the context")
    print("S ->", s)
























# with open("sample.txt", "w") as f:
#     f.write("Hello world")

# class SampleContext:

#     def __init__(self, file_name):
#         self.file_name = file_name

#     def __enter__(self):
#         print('Hello Sample context here')
#         return self.file_name

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Bye Sample Context')


# # sc = SampleContext()

# with SampleContext(file_name="example") as s:
#     # print("This is the context")
#     print("Value of S ->", s)

#     zero_division = 1/0






