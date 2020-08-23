def str_repeat(st):
    st = st.split( ' ' )
    st1 = st[0]
    st2 = st[1]
    st1_new = str()
    result = 0
    if st1 == st2:
        result = 1
        return result
    else:
        if len( st1 ) == len( st2 ):
            for i in range( len( st1 ) ):
                if st1[i] == st2[i]:
                    st1_new += st2[i]
                    result = 1
                else:
                    if st1.count( str( st1[i] ) ) > 1:
                        sim = st1[i]  #ищем номера вхождений в первой строке
                        sim_list = list()
                        sim_result = list()
                        for g in range(len(st1)):
                            if st1[g] == sim:
                                sim_list.append(g)
                        for gg in sim_list:
                            if st1[gg] == sim:
                                sim_result.append(1)
                        if len(sim_result) == sim_result.count(1):
                            result = 1
                            st1_new += st2[i]
                        else:
                            break
                    else:
                        st1_new += st2[i]
            print(st1_new)
            if st1_new == st2:
                print(result)
            else:
                print(0)
        else:
            print(0)
# st = input()
st = "ааббдд дкббаа"
str_repeat( st )
