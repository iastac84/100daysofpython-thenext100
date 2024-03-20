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
    "neworg 2 security splunkprod",
    "neworg 2 security sre",
    "myorg 2 security sre",
    "neworg 2 security tidatalake",
    "neworg 2 tsp worklink",
    "neworg 2 valuemanagement ops",
    "neworg 2 vndly qa",
    "neworg 2 wcp extend",
    "neworg 2 xwt sre",
    "neworg 3 analytics appeng",
    "neworg 3 analytics bds",
    "neworg 3 analytics daas",
    "myorg 3 analytics prism",
    "neworg 3 analytics prism",
    "neworg 3 appsqa xotools",
    "neworg 3 arch lodestar",
    "neworg 3 businesstech alphalabs",
    "neworg 3 businesstech bi",
    "myorg 3 businesstech bi",
    "neworg 3 businesstech devops",
    "neworg 3 businesstech it",
    "neworg 3 businesstech netdevops",
    "neworg 3 businesstech nexus",
    "myorg 3 businesstech syseng",
    "neworg 3 businesstech vcr"
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

print_tree(tree)

