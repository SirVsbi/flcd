from symbol_table import SymbolTable

if __name__ == '__main__':
    st = SymbolTable(3)

    st.add(("str", "hello world"))
    st.add(("const", 3))
    st.add(("number", 5))

    print(st)
