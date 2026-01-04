import tictactoe as ttt
import unittest

class TestTicTacToe(unittest.TestCase):
    def test_initial_state(self):
        board = ttt.initial_state()
        self.assertEqual(board, [[None, None, None], [None, None, None], [None, None, None]])

    def test_player(self):
        board = ttt.initial_state()
        self.assertEqual(ttt.player(board), ttt.X)
        
        board[0][0] = ttt.X
        self.assertEqual(ttt.player(board), ttt.O)
        
        board[0][1] = ttt.O
        self.assertEqual(ttt.player(board), ttt.X)

    def test_actions(self):
        board = ttt.initial_state()
        self.assertEqual(len(ttt.actions(board)), 9)
        
        board[0][0] = ttt.X
        actions = ttt.actions(board)
        self.assertEqual(len(actions), 8)
        self.assertNotIn((0, 0), actions)

    def test_result(self):
        board = ttt.initial_state()
        new_board = ttt.result(board, (0, 0))
        self.assertEqual(new_board[0][0], ttt.X)
        self.assertEqual(board[0][0], None)
        
        with self.assertRaises(Exception):
            ttt.result(new_board, (0, 0))
            
        # Test invalid action on modified board logic check
        board_filled = [[ttt.X, ttt.O, ttt.X], [ttt.X, ttt.O, ttt.X], [ttt.O, ttt.X, ttt.O]]
        with self.assertRaises(Exception):
             ttt.result(board_filled, (0, 0))

    def test_winner(self):
        board = [[ttt.X, ttt.X, ttt.X], [ttt.O, ttt.O, None], [None, None, None]]
        self.assertEqual(ttt.winner(board), ttt.X)
        
        board = [[ttt.O, ttt.X, ttt.X], [ttt.O, ttt.O, None], [ttt.O, None, None]]
        self.assertEqual(ttt.winner(board), ttt.O)
        
        board = [[ttt.X, ttt.O, ttt.X], [ttt.O, ttt.X, ttt.O], [ttt.O, ttt.X, ttt.O]]
        self.assertIsNone(ttt.winner(board))

    def test_terminal(self):
        board = ttt.initial_state()
        self.assertFalse(ttt.terminal(board))
        
        board = [[ttt.X, ttt.X, ttt.X], [ttt.O, ttt.O, None], [None, None, None]]
        self.assertTrue(ttt.terminal(board))
        
        board = [[ttt.X, ttt.O, ttt.X], [ttt.O, ttt.X, ttt.O], [ttt.O, ttt.X, ttt.O]]
        self.assertTrue(ttt.terminal(board))

    def test_utility(self):
        board = [[ttt.X, ttt.X, ttt.X], [ttt.O, ttt.O, None], [None, None, None]]
        self.assertEqual(ttt.utility(board), 1)
        
        board = [[ttt.O, ttt.X, ttt.X], [ttt.O, ttt.O, None], [ttt.O, None, None]]
        self.assertEqual(ttt.utility(board), -1)
        
        board = [[ttt.X, ttt.O, ttt.X], [ttt.O, ttt.X, ttt.O], [ttt.O, ttt.X, ttt.O]]
        self.assertEqual(ttt.utility(board), 0)

    def test_minimax(self):
        # X can win in one move
        board = [[ttt.X, ttt.X, None], [ttt.O, ttt.O, None], [None, None, None]]
        move = ttt.minimax(board)
        self.assertEqual(move, (0, 2))
        
        # O needs to block X
        board = [[ttt.X, None, None], [None, ttt.O, None], [ttt.X, None, None]]
        # X is threatening (0,0) and (2,0), so O must block? No, wait.
        # X moves first.
        # Let's set up a board where it is O's turn and X is about to win.
        board = [[ttt.X, ttt.X, None], [None, ttt.O, None], [None, None, None]]
        # Player is O. X has (0,0) and (0,1). O must block at (0,2).
        move = ttt.minimax(board)
        self.assertEqual(move, (0, 2))

if __name__ == '__main__':
    unittest.main()
