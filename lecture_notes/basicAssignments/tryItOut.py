import os


def getPath():
    cwd = os.getcwd()
    path_for_templates = os.path.join(cwd, "templates")
    print(path_for_templates)
    # print("Current working dir : %s" % os.getcwd())
    if not os.path.exists(path_for_templates):
        os.makedirs(path_for_templates)


getPath()
