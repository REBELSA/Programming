import os
if os.path.exists("Hey"):
    os.remove("Hey")
    print("File del success")
else:
    print("No exist")