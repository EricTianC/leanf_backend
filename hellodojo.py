from lean_dojo import *

repo = LeanGitRepo("https://github.com/EricTianC/leanf_leandemo","demo1")
theorem = Theorem(repo, "LeanfLeandemo.lean", "hellodojo")

with Dojo(theorem) as (dojo, init_state):
  print(init_state)
  result = dojo.run_tac(init_state, "rw [add_assoc, add_comm b, ←add_assoc]")
  assert isinstance(result, ProofFinished)
  print(result)