import cProfile
import pstats
import re
from pstats import SortKey

cProfile.run("re.compile('foo|bar')", "restats")
p = pstats.Stats("restats")
p.strip_dirs().sort_stats(-1).print_stats()

# 214 fn calls out of which 207 were primitive, meaning that the call was not induced via recursion.
# strip_dirs() method removes the extraneous path from all the module names.
