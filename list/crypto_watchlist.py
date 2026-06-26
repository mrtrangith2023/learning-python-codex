# Yêu cầu:

# Tạo list gồm 10 dự án airdrop đang theo dõi.
# In toàn bộ dự án.
# Thêm 2 dự án mới.
# Xóa 1 dự án.
# In tổng số dự án còn lại.
# Đánh số thứ tự từ 1 đến N.
projects = [
    "MegaETH",
    "Monad",
    "Robinhood",
    "Tempo",
    "Aic",
    "Arc",
    "GenLayer",
    "Merits",
    "Multipli",
    "Concrete"
]
print("DANH SÁCH DỰ ÁN AIRDROP ĐANG THEO DÕI:")
for project in projects:
    print(project)

print("Thêm 2 dự án mới: ")
projects.append("Rital")
projects.append("DAC")
print("================")

print(projects)

print("Xóa 1 dự án: ")
projects.remove("MegaETH")

print("TỔNG SỐ DỰ ÁN CON LẠI: ")
print(len(projects))

print("ĐÁNH SỐ THỨ TỰ TỪ 1 ĐẾN N: ")
for i, project in enumerate(projects, start=1):
    print(f"{i}. {project}")