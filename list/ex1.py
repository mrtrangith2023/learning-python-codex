# Bài 1: Danh sách công việc hằng ngày
# Yêu cầu
# In tổng số công việc.
# Thêm một công việc mới.
# Xóa một công việc.

# Ví dụ kết quả:
jobs = [
    "Learning Python",
    "Testnet Airdrop",
    "Learning English",
    "Build Project",
    "Entertaiment"
]
print("=====Kết quả=====")
print("Tổng công việc:", len(jobs))

print("Danh sách công việc:")
for job in jobs:
    print(job)

print("-----------------")
print("Thêm một công việc mới:")
jobs.append("Learning Hackathon")
print(jobs)
job_new = jobs[5]
print("Công việc mới thêm:", job_new)

print("-----------------")
print("Xóa 1 công việc:")
jobs.remove("Learning English")
print(jobs)