# --- Day 1: Report Repair ---
# After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island.
# Surely, Christmas will go on without you.
#
# The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of
# a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow,
# you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.
#
# To save your vacation, you need to get all fifty stars by December 25th.
#
# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar;
# the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
#
# Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently,
# something isn't quite adding up.
#
# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
#
# For example, suppose your expense report contained the following:
#
# 1721
# 979
# 366
# 299
# 675
# 1456
# In this list, the two entries that sum to 2020 are 1721 and 299.
# Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.
#
# Of course, your expense report is much larger.
# Find the two entries that sum to 2020; what do you get if you multiply them together?

# noinspection PyShadowingBuiltins
input = [1755, 1668, 837, 1900, 1687, 1901, 1765, 1963, 1945, 1791, 1688, 1792, 1865, 1833, 1811, 438, 1862, 1851, 1877,
         1808, 1253, 1933, 1578, 1841, 1871, 1784, 1567, 1797, 1941, 1747, 1787, 1744, 1450, 1795, 1602, 1972, 1946,
         1827, 1950, 1704, 547, 1971, 1910, 1502, 1750, 1967, 1656, 1834, 1754, 1446, 1678, 1647, 1695, 1525, 1923,
         1488, 1829, 1848, 1766, 1662, 1724, 1897, 1751, 1823, 1540, 1736, 1929, 1772, 1778, 1732, 1948, 1691, 1820,
         1788, 1601, 1708, 2005, 1543, 1990, 1666, 1994, 1689, 1980, 1839, 2008, 1801, 1592, 1739, 1845, 1434, 360,
         1828, 1942, 1713, 1721, 1984, 1966, 2006, 1459, 1944, 1849, 1959, 1740, 1692, 1842, 1999, 1711, 1702, 1777,
         1222, 1745, 686, 1447, 2002, 1895, 1590, 1498, 1643, 1870, 412, 73, 1467, 1917, 1438, 2001, 1758, 1810, 1425,
         1969, 1884, 1534, 1761, 1512, 1937, 1654, 1796, 1495, 1996, 1473, 1831, 1988, 1469, 1924, 1621, 1403, 1746,
         1998, 1858, 1706, 1798, 1978, 1559, 1898, 1815, 1623, 1785, 1753, 1436, 608, 1652, 1940, 336, 1894, 1454, 1599,
         1604, 1975, 1881, 1716, 1878, 1595, 1928, 1550, 1414, 1962, 1607, 1756, 1986, 1775, 1952, 1415, 1864, 1813,
         650, 1492, 1960, 641, 1953, 1873, 1985, 1588, 1680, 1817, 1685, 1723, 1799, 1640, 1479, 1912, 1638]

for a in input:
    b = 2020 - a
    if b in input:
        print(f"{a} * {b} = {a * b}")
        break

# --- Part Two ---
# The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over
# from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet
# the same criteria.
#
# Using the above example again, the three entries that sum to 2020 are 979, 366, and 675.
# Multiplying them together produces the answer, 241861950.
#
# In your expense report, what is the product of the three entries that sum to 2020?

for a in input:
    points = 2020 - a
    for b in input:
        c = points - b
        if c in input:
            print(f"{a} * {b} * {c} = {a * b * c}")
