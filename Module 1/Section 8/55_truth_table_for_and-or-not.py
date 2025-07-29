# Create a truth table for and, or, not for two boolean inputs.

p_TF = lambda x: "True" if x else "False"

print(f"\n{"A":<6} {"B":<6} {"A and B":<10} {"A or B":<10} {"not A":<8} {"not B":<8}")

print("")
for A in [True, False]:
    for B in [True, False]:
        and_result = A and B
        or_result = A or B
        not_A = not A
        not_B = not B
        print(
            f"{p_TF(A):<6} {p_TF(B):<6} {p_TF(and_result):<10} {p_TF(or_result):<10} {p_TF(not_A):<8} {p_TF(not_B):<8}"
        )
        # print(f"{A:<6} {B:<6} {and_result:<10} {or_result:<10} {not_A:<8} {not_B:<8}")
