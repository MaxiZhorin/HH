def str_repeat(st):
    st = st.split( ' ' )
    st1 = st[0]
    st2 = st[1]
    st_new = str()
    if len( st1 ) == len( st2 ):
        for i in range( len( st1 ) ):
            if st1 == st2:
                pass
            else:
                if st1.count( st1[i] ) > 1:
                    sim_a = st1[i]  # ищем номера вхождений в первой строке
                    sim_b = st2[i]
                    sim_list = list()
                    sim_result = list()
                    for g in range( len( st1 ) ):
                        if st1[g] == sim_a:
                            sim_list.append( g )
                    for gg in sim_list:
                        if st2[gg] == sim_b:
                            sim_result.append( 1 )
                        else:
                            sim_result.append(0)
                    if len( sim_result ) == sim_result.count( 1 ):
                        st_new += st2[i]
                    else:
                        break
                else:
                    st_new += st2[i]
    if st_new == st2:
        print(1)
    else:
        print(0)



# st = input()
st = "ддббаа ддббааа"
str_repeat( st )