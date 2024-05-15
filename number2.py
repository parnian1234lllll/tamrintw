
# تعریف لیست دوطرفه دو چند جمله ای
polynomial1 = list(map(int, input(): ").split()))


polynomial2 = list(map(int, input(): ").split()))

# حساب جمع
sum_result = [polynomial1[i] + polynomial2[i] for i in range(max(len(polynomial1), len(polynomial2)))]

# حساب ضرب
product_result = [0] * (len(polynomial1) + len(polynomial2) - 1)
for i in range(len(polynomial1)):
    for j in range(len(polynomial2)):
        product_result[i + j] += polynomial1[i] * polynomial2[j]

# حساب تقسیم و تفریق
if len(polynomial1) > len(polynomial2):
    division_result = polynomial1[len(polynomial2):]
    subtraction_result = [polynomial1[i] - polynomial2[i] if i < len(polynomial2) else polynomial1[i] for i in range(len(polynomial1))]
else:
    division_result = [0]
    subtraction_result = [polynomial1[i] - polynomial2[i] if i < len(polynomial1) else -polynomial2[i] for i in range(len(polynomial2))]

print("حاصل جمع: ", sum_result)
print("حاصل ضرب: ", product_result)
print("حاصل تقسیم: ", division_result)
print("حاصل تفریق: ", subtraction_result)