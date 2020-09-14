print("Nhập tiền lương cơ bản: ",end='')
iTienluong=int(input())
print("Nhập vào số ngày đi làm: ",end='')
iSongay =int(input())
print("Nhập vào tiền phụ cấp: ",end='')
iPhucap = int(input())
a = (iTienluong + iPhucap)/22
b = iSongay
c = a *b
print("Lương chính là: " +str(c))