import networkx as nx
import glob
import settings as settings
# import matplotlib as plt

workflows = glob.glob(settings.workflow_path + "/*")

for workflow in workflows:
    print workflow
    import workflow.value()

# def get_activities(path):
#     activities = []
#     f = open(path, "r")
#     contents = f.readlines()
#     f.close()
#     for line in contents:
#
#
# print workflows
