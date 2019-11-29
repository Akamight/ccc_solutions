first_string = input()
anagram = input()

distinct_values = list(set(list(first_string)))

counts = [first_string.count(i) for i in distinct_values]

print(distinct_values, counts)

counts_anagram = [anagram.count(i) for i in distinct_values]
print(counts_anagram)

difference = [abs(i - p) for i,p in zip(counts,counts_anagram)]
difference = sum(difference)


if difference > anagram.count("*"):
    print("N")
else:
    print("A")
