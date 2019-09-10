
# f= open("testSuper.py")  # 默认只读
# text=f.read()
# # f.write("hello")
# print(text)
# f.close()

f= open("testSuper.py","rb")  # 默认只读
fw= open("testSuper1111.py","wb")  # 默认只读
text=f.read()
fw.write(text)
print(text)
f.close()
fw.close()


# f= open("aaaa.png","rb")  # 默认只读
# fw= open("bbbb.png","wb")  # 默认只读
# text=f.read()
# fw.write(text)
# print(text)
# f.close()
# fw.close()