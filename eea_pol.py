def gf_degree(a) :
  res = 0
  a >>= 1
  while (a != 0) :
    a >>= 1;
    res += 1;
  return res

def gf_invert(a, irr_pol=0x1B, gf_power=8) :
  v = irr_pol
  g1 = 1
  g2 = 0
  j = gf_degree(a) - gf_power

  while (a != 1) :
    if (j < 0) :
      a, v = v, a
      g1, g2 = g2, g1
      j = -j

    a ^= v << j
    g1 ^= g2 << j

    a %= (2**gf_power)
    g1 %= (2**gf_power)

    j = gf_degree(a) - gf_degree(v)

  return bin(g1), hex(g1), g1

print(gf_invert(0x61, 0b11001011, 7))
# a = yang dicari, irr_pol = irreducible polynom, gf_power = GF(2^n)
# 0b111000011 = x^8 + x^7 + x^6 + x^1 + x^0
# kalo mau dalam hex ganti jadi 0x...
# referensi https://stackoverflow.com/questions/45442396/a-pure-python-way-to-calculate-the-multiplicative-inverse-in-gf28-using-pytho