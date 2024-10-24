import main
import unittest

class TestMain(unittest.TestCase):

    def test_build_empty_graph(self):
        g = main.build_graph(0, [])
        self.assertEqual(g.k, 0)
        self.assertEqual(g.idx_to_node, {})
        self.assertCountEqual(g.idx_no_parent, set())
        # Topo sort
        s = main.valid_order(g)
        self.assertEqual(s, [])

    def test_build_graph_one_element(self):
        g = main.build_graph(1, [])
        self.assertEqual(g.k, 1)
        self.assertCountEqual(g.idx_to_node.keys(), [1])
        self.assertCountEqual(g.idx_no_parent, set([1]))
        # Topo sort
        s = main.valid_order(g)
        self.assertEqual(s, [1])

    def test_remove_node(self):
        g = main.build_graph(1, [])
        self.assertEqual(g.k, 1)
        self.assertCountEqual(g.idx_to_node.keys(), [1])
        self.assertCountEqual(g.idx_no_parent, set([1]))
        n = main.remove_node(1, g) 
        self.assertEqual(g.k, 1)
        self.assertCountEqual(g.idx_to_node.keys(), [])
        self.assertCountEqual(g.idx_no_parent, set([]))
        self.assertEqual(n.id, 1)

    def test_build_graph_two_elements_no_edge(self):
        g = main.build_graph(2, [])
        self.assertEqual(g.k, 2)
        self.assertCountEqual(g.idx_to_node.keys(), [1, 2])
        self.assertCountEqual(g.idx_no_parent, set([1, 2]))
        # Topo sort
        s = main.valid_order(g)
        self.assertCountEqual(s, [1, 2])

    def test_build_graph_two_elements_one_edge_1(self):
        g = main.build_graph(2, [[1, 2]])
        self.assertEqual(g.k, 2)
        self.assertCountEqual(g.idx_to_node.keys(), [1, 2])
        self.assertCountEqual(g.idx_no_parent, set([1]))
        # Topo sort
        s = main.valid_order(g)
        self.assertEqual(s, [1, 2])

    def test_build_graph_two_elements_one_edge_2(self):
        g = main.build_graph(2, [[2, 1]])
        self.assertEqual(g.k, 2)
        self.assertCountEqual(g.idx_to_node.keys(), [1, 2])
        self.assertCountEqual(g.idx_no_parent, set([2]))
        # Topo sort
        s = main.valid_order(g)
        self.assertEqual(s, [2, 1])

    def test_build_graph_two_elements_with_loop(self):
        g = main.build_graph(2, [[2, 1], [1, 2]])
        self.assertEqual(g.k, 2)
        self.assertCountEqual(g.idx_to_node.keys(), [1, 2])
        self.assertCountEqual(g.idx_no_parent, set())
        # No valid topo sort
        s = main.valid_order(g)
        self.assertEqual(s, None)

    def test_build_graph_leetcode_ex(self):
        g = main.build_graph(3, [[1, 2], [3, 2]])
        self.assertEqual(g.k, 3)
        self.assertCountEqual(g.idx_to_node.keys(), [1, 2, 3])
        self.assertCountEqual(g.idx_no_parent, set([1, 3]))
        # Topo sort
        s = main.valid_order(g)
        self.assertCountEqual(s, [1,2,3])
        self.assertEqual(s[2], 2)

    def test_build_matrix_1(self):
        row_order = [1, 2, 3]
        col_order = [1, 2, 3]
        m = main.build_matrix(row_order, col_order)
        row_1 = m[0]
        row_2 = m[1]
        row_3 = m[2]
        self.assertEqual(row_1, [1, 0, 0])
        self.assertEqual(row_2, [0, 2, 0])
        self.assertEqual(row_3, [0, 0, 3])

    def test_build_matrix_2(self):
        row_order = [1, 2, 3]
        col_order = [3, 2, 1]
        m = main.build_matrix(row_order, col_order)
        row_1 = m[0]
        row_2 = m[1]
        row_3 = m[2]
        self.assertEqual(row_1, [0, 0, 1])
        self.assertEqual(row_2, [0, 2, 0])
        self.assertEqual(row_3, [3, 0, 0])


    def test_solution_1(self):
        s = main.Solution()
        row_cond = [[1, 2], [3, 2]]
        col_cond = [[2, 1], [3, 2]]
        k = 3
        mtx = s.buildMatrix(k, row_cond, col_cond)
        self.assertEqual(mtx[2][1], 2)

    def test_solution_2(self):
        s = main.Solution()
        row_cond = [[1,2],[2,3],[3,1],[2,3]]
        col_cond = [[2,1]]
        k = 3
        mtx = s.buildMatrix(k, row_cond, col_cond)
        self.assertEqual(mtx, [])                        
                        

if __name__ == '__main__':
    unittest.main()
