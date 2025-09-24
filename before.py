class MinesweeperGame:
  def __init__(self, n, k) -> None:
    self.n = n
    self.k = k
    self.minesweeper_map = self.generate_mine_sweeper_map()
    self.player_map = self.generate_playerMap()
    self.score = 0
  def generate_mine_sweeper_map(self):
    arr = [[0 for row in range(self.n)] for column in range(self.n)]
    for num in range(self.k):
      x = random.randint(0, self.n-1)
      ...    
  def generate_playerMap(self): ...
  def check_won(self, map): ...
  def sweep(self, x, y): ...
