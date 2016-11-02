sec = str(input("Paste the DNA sequence here: ")).upper()
count = input("")
count = str(input("Which bases would you like to count?")).upper()

#count = 'ACGT'
#sec = 'asd'

base_count = []

for base in count:
    base_count.append(
        str(sec.count(base))
    )

print(
    ' '.join(count)
)

print(
    ' '.join(base_count)
)