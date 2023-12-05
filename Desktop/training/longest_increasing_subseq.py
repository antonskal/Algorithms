def logic_for_lis_is_in_need_of_a_better_name(i,j):
	return (a[j] > a[i] and m[i] + 1 > m[j])

lines = input("Input the sequence using the , delimter to seperate\n")
a = lines.split(",")

m = []
for j in range(0,len(a)):
	m.append(1)
	for i in range(0,j):
		if logic_for_lis_is_in_need_of_a_better_name(i,j):
			m[j] = m[i] + 1

print(max(m))
