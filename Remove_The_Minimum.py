def remove_smallest(numbers):
    new=numbers[:]
    if new:
        new.remove(min(new))
    return new
    raise NotImplementedError("TODO: remove_smallest")