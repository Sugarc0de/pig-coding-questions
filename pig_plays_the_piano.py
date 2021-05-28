# Method: Array
def can_play(notes):
    diff = []
    for note, start, duration in notes:
        diff.append((start, 1, note))
        diff.append((start + duration, -1, note))
    diff = list(sorted(diff))
    values = set()
    for ts, change, note in diff:
        if change == 1:
            values.add(note)
        elif change == -1:
            values.remove(note)
        if (
            len(values) > 0 and max(values) - min(values) > 10
        ):  # pig only has 10 fingers
            return False
    return True


# True, only one note
print(can_play([(50, 0, 5)]))

# True, notes are not overlapping in time
print(can_play([(50, 0, 5), (70, 5, 2)]))

# False, notes are overlapping during [4-5]
print(can_play([(50, 0, 5), (70, 4, 2)]))

# False, notes 1 and 3 are overlapping
print(can_play([(50, 0, 10), (58, 5, 10), (65, 8, 10)]))

# True, lots of notes but no overlap
print(can_play([(50, 0, 10), (58, 5, 10), (48, 8, 10), (40, 1, 3)]))
