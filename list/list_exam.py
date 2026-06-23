fruits = ["apple", "banana", "organce"]

print("Danh sách fruits: ", fruits)


print("Truy cập phần tử: ")
print(fruits[0])
print(fruits[1])

print("Thay đổi giá trị: ")
fruits[1] = "mango"
print(fruits)

print("Thêm phần tử ở cuối danh sách: ")
fruits.append("tomato")
print(fruits)

print("Xóa phần tử: ")
fruits.remove("apple")
print(fruits)

print("Đếm tổng số độ dài phần tử: ")
print(len(fruits))

print("Duyệt qua danh sách fruits: ")
for fruit in fruits:
    print(fruit)

print("Tạo danh sách chưa nhiều loại dữ liệu khác nhau: ")
student = ["Nam", 24, True, "Ca Mau", 22.5]
print("Danh sách sinh viên:", student)


print("Ví dụ thực tế")
print("-------------")

wallets = [
    "0x1234abc",
    "0x1235def",
    "0x1236ghi"
]

for wallet in wallets:
    print("Checking", wallet)