
import random # this is used for shuffling

# create a deck of cards
mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def deal(numhands, n = 5, deck = mydeck):
  "Function to randomly deal a hand from a deck of cards"
  return [[random.choice(mydeck) for j in xrange(n)] for i in xrange(numhands)]

def poker(hands):
    "Return a list of winning hands: poker([hand, ...]) => [hand,.....]"
    return allmax(hands, key = lambda x: hand_rank(x))

def allmax(iterable, key = None):
  "Returns a list of all items equal to the max of iterable."
  m = max(iterable, key = key)
  return [element for element in iterable if key(element) == key(m)]


def hand_rank(hand):
    "Return a value indicating the rank of a hand"
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):              # straight flush
      return (8, max(ranks))
    elif kind(4, ranks): 							 # 4 of a kind
      return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):          # full house
      return (6, kind(3,ranks), kind(2, ranks))
    elif flush(hand):								 # flush
      return (5, max(ranks), ranks)

    elif straight(ranks):							 # stright

    elif straight(ranks):							 # straight

      return (4, max(ranks))
    elif kind(3, ranks):							 # 3 of a kind
      return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):							 # 2 pair
      return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):							 # high card
      return (1, kind(2, ranks), ranks)
    else:
      return (0,ranks)

def card_ranks(cards):
  "Return a list of the ranks, sorted with higher first"
<<<<<<< HEAD
  ranks = [' 123456789TJQKA'.index(r) for r,s in cards]
  ranks.sort(reverse = True)
  return ranks

def test():
  "Test cases for the function in poker program"
  sf = "6C 7C 8C 9C TC".split() # straight flush
  fk = "9D 9H 9S 9C 7D".split() # four kind
  fh = "TD TC TH 7C 7D".split() # full house
  assert poker([sf, fk, fh]) == sf
  assert poker([fk, fh]) == fk
  assert poker([fh, fh]) == fh
  assert poker([sf]) = sf
=======
  ranks = sorted(['--23456789TJQKA'.index(r) for r,s in cards], reverse = True)
  return [5, 4, 3, 2, 1] if ranks == [14, 5, 4, 3, 2] else ranks

def straight(ranks):
  "Returns True if the ordered ranks form a five-card straight"
  return all([ranks[0] - ranks[i] == i for i, j in enumerate(ranks)])

def flush(hand):
  "Return True if all cards have the same suit."
  return all([hand[0][1] == s for r,s in hand])

def kind(n, ranks):
  """ Return the first rank that this hand has exactly n of.
  Return None if there no n-of-a-kind in the hand."""
  x = [ranks.count(i) for i in ranks]
  for i, j in enumerate(x):
    if j == n:
      return ranks[i]
  return None


def two_pair(ranks):
  """ If there are two pairs, return the two ranks as a tuple:
  (highest, lowest); otherwise return None. """
  f = kind(2, ranks)
  s = kind(2, ranks[1:])
  if f and s:
    return (max(f,s), min(f,s))
  return None




def test():
  "Test cases for the function in poker program"

  # some hands
  sf = "6C 7C 8C 9C TC".split() # straight flush
  fk = "9D 9H 9S 9C 7D".split() # four kind
  fh = "TD TC TH 7C 7D".split() # full house
  tp = "5S 5D 9S 9C 6S".split() # two pair
  s1 = "AS 2S 3S 4S 5C".split() # A-5 straight
  s2 = "2C 3C 4C 5S 6S".split() # 2-6 straight
  ah = "AS 2S 3S 4S 6C".split() # A high
  sh = "2S 3S 4S 6C 7D".split() # 7 high

  # tests for poker function
  assert poker([s1, s2, ah, sh]) == s2
  assert poker([sf, fk, fh]) == sf
  assert poker([fk, fh]) == fk
  assert poker([fh, fh]) == fh
  assert poker([sf]) == sf

  assert poker([sf for i in xrange(100)]) == sf


  # tests for hand_rank function
  assert hand_rank(sf) == (8, 10)
  assert hand_rank(fk) == (7, 9, 7)
  assert hand_rank(fh) == (6, 10, 7)
  return "tests pass"

  # test for card_ranks function

  assert card_ranks(sf) = [10, 9, 8, 7, 6]
  assert card_ranks(fk) = [9, 9, 9, 9, 7]
  assert card_ranks(fh) = [10, 10, 10, 7, 7]


  assert card_ranks(sf) == [10, 9, 8, 7, 6]
  assert card_ranks(fk) == [9, 9, 9, 9, 7]
  assert card_ranks(fh) == [10, 10, 10, 7, 7]

  # tests for straight function
  assert straight([9, 8, 7, 6, 5]) == True
  assert straight([9, 8, 8, 6, 5]) == False

  # tests for flush function
  assert flush(sf) == True
  assert flush(fk) == False

  # test for kind function
  fkranks = card_ranks(fk)
  tpranks = card_ranks(tp)

  assert kind(4, fkranks) == 9
  assert kind(3, fkranks) == None
  assert kind(2, fkranks) == None
  assert kind(1, fkranks) == 7

  # test for two-pair function
  assert two_pair (fkranks) == None
  assert two_pair (tpranks) == (9, 5)



print test()
