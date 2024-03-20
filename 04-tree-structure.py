#!/usr/bin/env python3
# Day 04 

# Turn list into a tree structure

def add_to_tree(tree, path):
    current = tree
    for node in path:
        if node not in current:
            current[node] = {}
        current = current[node]

def print_tree(tree, indent=''):
    for key, value in tree.items():
        print(indent + '└── ' + key)
        if value:
            print_tree(value, indent + '    ')

data = [
    "workdayou 2 security splunkprod",
    "workdayou 2 security sre",
    "myorg 2 security sre",
    "workdayou 2 security tidatalake",
    "workdayou 2 tsp worklink",
    "workdayou 2 valuemanagement ops",
    "workdayou 2 vndly qa",
    "workdayou 2 wcp extend",
    "workdayou 2 xwt sre",
    "workdayou 3 analytics appeng",
    "workdayou 3 analytics bds",
    "workdayou 3 analytics daas",
    "myorg 3 analytics prism",
    "workdayou 3 analytics prism",
    "workdayou 3 appsqa xotools",
    "workdayou 3 arch lodestar",
    "workdayou 3 businesstech alphalabs",
    "workdayou 3 businesstech bi",
    "myorg 3 businesstech bi",
    "workdayou 3 businesstech devops",
    "workdayou 3 businesstech it",
    "workdayou 3 businesstech netdevops",
    "workdayou 3 businesstech nexus",
    "myorg 3 businesstech syseng",
    "workdayou 3 businesstech vcr"
]

# Extracting the root directory dynamically
root_directory = data[0].split()[0]

tree = {}
for item in data:
    split_item = item.split()
    root = split_item[0]
    level = split_item[1]
    category = split_item[2]
    path = split_item[3:]  # Extracting the hierarchy path
    add_to_tree(tree.setdefault(root, {}).setdefault(level, {}).setdefault(category, {}), path)

print('└── ' + root_directory)
print_tree(tree)

