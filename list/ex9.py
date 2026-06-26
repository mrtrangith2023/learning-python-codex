# Bài 9: Watchlist Airdrop

# In danh sách airdrop
# Thêm airdrop
list_airdrop = [
    "Monad",
    "Tempo",
    "GenLayer",
    "Arc"
]

for airdrop in list_airdrop:
    print(airdrop)

print("Thêm airdrop vào danh sách:")

air = input("Thêm mới airdrop: ")
list_airdrop.append(air)
print("Danh sách sau khi cập nhật:", list_airdrop)
