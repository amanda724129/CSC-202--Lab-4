import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6) 

BinTree: TypeAlias = Union[None,"BTNode"]
@dataclass(frozen=True)
class BTNode:
    val: Any
    left: BinTree
    right: BinTree

@dataclass(frozen=True)
class BinarySearchTree:
    comes_before: Callable[[Any, Any], bool]
    tree: BinTree

def less_than(a: Any, b: Any) -> bool:
    return a < b

def is_empty(bst: BinarySearchTree) -> bool:
    if bst.tree is None:
        return True
    else: 
        return False
    
def insert(bst: BinarySearchTree, value: Any) -> BinarySearchTree:
    def insert_node(node: BinTree, value: Any, cb: Callable[[Any, Any], bool]) -> BTNode:
        if node is None:
            return BTNode(value, None, None)
        elif cb(value, node.val):
            return BTNode(node.val, insert_node(node.left, value, cb), node.right)
        else:
            return BTNode(node.val, node.left, insert_node(node.right, value, cb))
    new_tree = insert_node(bst.tree, value, bst.comes_before)
    return BinarySearchTree(bst.comes_before, new_tree)

def lookup(bst: BinarySearchTree, value: Any) -> bool:
    def find_node(node: BinTree, value: Any, cb: Callable[[Any, Any], bool]) -> bool:
        if node is None:
            return False
        elif cb(value, node.val):
            return find_node(node.left, value, cb)
        elif cb(node.val, value):
            return find_node(node.right, value, cb)
        else:
            return True
    return find_node(bst.tree, value, bst.comes_before)

def delete(bst: BinarySearchTree, value: Any) -> BinarySearchTree:
    if not lookup(bst, value):
        return bst
    def find_min(node: BTNode) -> Any:
        while node.left is not None:
            node = node.left
        return node.val
    def delete_node(node: BinTree, value: Any, cb: Callable[[Any, Any], bool]) -> BTNode:
        if node is None:
            return None
        elif cb(value, node.val):
            return BTNode(node.val, delete_node(node.left, value, cb), node.right)
        elif cb(node.val, value):
            return BTNode(node.val, node.left, delete_node(node.right, value, cb))
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_val = find_min(node.right)
                new_right = delete_node(node.right, min_val, cb)
                return BTNode(min_val, node.left, new_right)
    new_tree = delete_node(bst.tree, value, bst.comes_before)
    return BinarySearchTree(bst.comes_before, new_tree)
