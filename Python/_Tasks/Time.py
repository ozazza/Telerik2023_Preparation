d = int(input())
h = int(input())
m = int(input())
s = int(input())

d_s = d * 24 * 60 * 60
h_s = h * 60 * 60
m_s = m * 60

print(d_s + h_s + m_s + s)