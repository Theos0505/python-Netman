# Integers and strings in python are immutable
print("--------Listing the immutable objects----------")
i = 1
print(f"i: {i} , id(i): {id(i)}")
i += 1
print(f"i: {i} , id(i): {id(i)} <-- after i += 1")
j = i
print(f"\ni: {i} , id(i): {id(i)}")
print(f"j: {j}, id(j): {id(j)}")
# The above prints the id of i and j which will have same value since they point to same memory
i = i + 1
print(f"\ni: {i} , id(i): {id(i)}")
print(f"j: {j}, id(j): {id(j)}")
# Here the i and j's ids will differ as now i points to different memory
print("\n\n")

print("--------Listing the mutable objects like 'lists'----------")

l1 = [1]
print(f"l1: {l1}, id(l1): {id(l1)}")
l1.append(2)
print(f"l1: {l1}, id(l1): {id(l1)}")
l2 = l1
print(f"\nl1: {l1}, id(l1): {id(l1)}")
print(f"l2: {l2}, id(l2): {id(l2)}")
l2.append(3)
print(f"\nl1: {l1}, id(l1): {id(l1)}")
print(f"l2: {l2}, id(l2): {id(l2)}")


print("\n\n")

print("----function call, mutable v immutable")


def func(l_var, r_var):
    l_var += 1
    r_var.append(5)
    print(f"inside function:  lvar={l_var} and r_var={r_var}")


left_var = 2
right_var = [1, 2, 3, 4]

print(f"Before:                left_var={left_var} and right_var={right_var}")
func(left_var, right_var)
print(f"After                  left_var={left_var} and right_var={right_var}")
