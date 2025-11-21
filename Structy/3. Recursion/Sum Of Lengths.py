def sum_of_lengths(strings):
  pass # todo
  if len(strings) == 0:
    return 0 
  return len(strings[0]) + sum_of_lengths(strings[1:])
