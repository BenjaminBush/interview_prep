class rbnode(object):
    def __init__(self, key):
        self._red = False
        self._key = key
        self._left = None
        self._right = None
        self._p = None
        
    red = property(fget=lambda self:self._red, doc="The color of the rb node")
    key = property(fget=lambda self:self._key, doc="The key of the rb node")
    left = property(fget=lambda self:self._left, doc="The left child of the rb node")
    right = property(fget=lambda self:self._right, doc="The right child of the rb node")
    p = property(fget=lambda self:self._p, doc="The parent of the rb node")

    def __str__(self):
        return str(self._key)
    def __repr__(self):
        return str(self._key)
    
class rbtree(object):
    """
    Basic Implementation of a Red-Black tree. (CLRS)
    """
    
    
    def __init__(self, create_node=rbnode):        
        self._nil = create_node(key=None)        
        self._root = self.nil        
        self._create_node = create_node

    root = property(fget=lambda self: self._root, doc="The tree's root node")
    nil = property(fget=lambda self: self._nil, doc="The tree's nil node")
    
    
    def search(self, key, x=None):
        if None == x:
            x = self.root
        while x != self.nil and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    
    def minimum(self, x=None):
        if None == x:
            x = self.root
        while x.left != self.nil:
            x = x.left
        return x

    
    def maximum(self, x=None):
        if None == x:
            x = self.root
        while x.right != self.nil:
            x = x.right
        return x

    
    def insert_key(self, key):
        self.insert_node(self._create_node(key=key))
    
    
    def insert_node(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z._p = y
        if y == self.nil:
            self._root = z
        elif z.key < y.key:
            y._left = z
        else:
            y._right = z
        z._left = self.nil
        z._right = self.nil
        z._red = True
        self._insert_fixup(z)
        
        
    def _insert_fixup(self, z):
        while z.p.red:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.red:
                    z.p._red = False
                    y._red = False
                    z.p.p._red = True
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self._left_rotate(z)
                    z.p._red = False
                    z.p.p._red = True
                    self._right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.red:
                    z.p._red = False
                    y._red = False
                    z.p.p._red = True
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self._right_rotate(z)
                    z.p._red = False
                    z.p.p._red = True
                    self._left_rotate(z.p.p)
        self.root._red = False

    
    def _left_rotate(self, x):
        y = x.right
        x._right = y.left
        if y.left != self.nil:
            y.left._p = x
        y._p = x.p
        if x.p == self.nil:
            self._root = y
        elif x == x.p.left:
            x.p._left = y
        else:
            x.p._right = y
        y._left = x
        x._p = y


    def _right_rotate(self, y):
        "Left rotate y."
        x = y.left
        y._left = x.right
        if x.right != self.nil:
            x.right._p = y
        x._p = y.p
        if y.p == self.nil:
            self._root = x
        elif y == y.p.right:
            y.p._right = x
        else:
            y.p._left = x
        x._right = y
        y._p = x

    def _transplant(self, u, v):
        if u.p == self.nil:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p 

    def _delete(self, z):
        y = z
        y_original_color = y._red
        if z.left == self.nil:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y._red
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self._transplant(z, y)
            y.left = z.left
            y.left.p = y
            y._red = z._red
        if not y_original_color:
            self._delete_fixup(x)
            
    def _delete_fixup(self, x):
        while x != self.root and x._red == False:
            if x == x.p.left:
                w = x.p.right
                if w._red:
                    w._red = False
                    x.p._red = True
                    self._left_rotate(x.p)
                    w = x.p.right
                if not w.left._red and not w.right._red:
                    w._red = True
                    x = x.p
                else:
                    if not w.right._red:
                        w.left._red = False
                        w._red = True
                        self._right_rotate(w)
                        w = x.p.right
                    w._red = x.p._red
                    x.p._red = False
                    w.right._red = False
                    self._left_rotate(x.p)
                    x = self.root
            else:
                w = x.p.left
                if w._red:
                    w._red = False
                    x.p._red = True
                    self._right_rotate(x.p)
                    w = x.p.left
                if not w.right._red and not w.left._red:
                    w._red = True
                    x = x.p
                else:
                    if not w.left._red:
                        w.right._red = False
                        w._red = True
                        self._left_rotate(w)
                        w = x.p.left
                    w._red = x.p._red
                    x.p._red = False
                    w.left._red = False
                    self._right_rotate(x.p)
                    x = self.root
        x._red = False


    def check_invariants(self):
        def is_red_black_node(node):
            # check has _left and _right or neither
            if (node.left and not node.right) or (node.right and not node.left):
                return 0, False

            # check leaves are black
            if not node.left and not node.right and node.red:
                return 0, False

            # if node is red, check children are black
            if node.red and node.left and node.right:
                if node.left.red or node.right.red:
                    return 0, False
                    
            # descend tree and check black counts are balanced
            if node.left and node.right:
                
                # check children's parents are correct
                if self.nil != node.left and node != node.left.p:
                    return 0, False
                if self.nil != node.right and node != node.right.p:
                    return 0, False

                # check children are ok
                left_counts, left_ok = is_red_black_node(node.left)
                if not left_ok:
                    return 0, False
                right_counts, right_ok = is_red_black_node(node.right)
                if not right_ok:
                    return 0, False

                # check children's counts are ok
                if left_counts != right_counts:
                    return 0, False
                return left_counts, True
            else:
                return 0, True
                
        num_black, is_ok = is_red_black_node(self.root)
        return is_ok and not self.root._red
                


def test_tree(t, keys):
    "Insert keys one by one checking invariants and membership as we go."
    assert t.check_invariants()
    for i, key in enumerate(keys):
        for key2 in keys[:i]:
            assert t.nil != t.search(key2)
        for key2 in keys[i:]:
            assert (t.nil == t.search(key2)) ^ (key2 in keys[:i])
        t.insert_key(key)
        assert t.check_invariants()
    

if __name__=='__main__':
    import os, sys, numpy.random as R        
    # test the rbtree
    R.seed(2)
    size=50
    keys = R.randint(-50, 50, size=size)
    t = rbtree()
    test_tree(t, keys)