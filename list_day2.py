projects = ["Arc", "Fhenix", "OnBalance"]

print(projects)
print("Tìm vị trí theo chỉ số index", projects[2])

print("Duyệt qua list ta sử dụng for")

for project in projects:
    print(project)


projects[2] = "Monad"
print(projects)

projects.append("OnBalance")
print(projects)

print("Mở rộng phần cuối list ta dùng extend")
new_projects = ["MegaETH", "ACI", "Robinhood"]

projects.extend(new_projects)
print("Danh sách mở rộng", projects)

print("Xóa phần tử theo tên phân tử ta sử dụng Remove")
projects.remove("Fhenix")
print(projects)

projects.reverse()
print(projects)

print("Xóa 1 phần tử theo vị trí Index")
projects.pop(2)
print(projects)

print(f"Đếm phần tử 'Monad' ta dùng count và tên phần tử")
count_projects = projects.count("Monad")
print("Số phần tử là:", count_projects)


student = ["Tran", 18, True]
print("Thong tin SV: ", student)
for sv in student:
    print(sv)

student.append("Ca Mau")
print(student)

x = student.index(True)
print("Tìm vị trí theo index", x)