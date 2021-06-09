from File_with_foo import d_s, s_d, m_k, k_m, f_k, k_f, u_g, g_u, gal_l, l_gal, p_l, l_p
list_func = [d_s, s_d, m_k, k_m, f_k, k_f, u_g, g_u, gal_l, l_gal, p_l, l_p]
dict_func = {}
i = 0
for el in list_func:
    dict_func[i] = el
    i += 1

while True:
    x = int(input("Введите число от 1 до 12 для вызова различных функций, или 0 для выхода из программы: \n"))
    y = int(input("Введите число, которое нужно обработать: \n"))
    if x == 0:
        break
    foo = dict_func[x-1]
    print(foo(y))
