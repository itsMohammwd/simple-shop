
import streamlit as st

from database import add_product, get_all_products, delete_product

st.title("Simple Shop")

st.header("Add Product")

name = st.text_input("Product Name")
price = st.number_input("Price", min_value=0, step=1)
stock = st.number_input("Stock", min_value=0, step=1)

if st.button("Add Product"):
    if name.strip():
        add_product(name, int(price), int(stock))
        st.success("Product added successfully!")
    else:
        st.warning("Enter product name")

st.divider()

st.header("Products")

products = get_all_products()

if products:
    st.dataframe(products)

    product_id = st.selectbox(
        "Select Product ID",
        [product["id"] for product in products]
    )

    if st.button("Delete Product"):
        delete_product(product_id)
        st.success("Product deleted!")
        st.rerun()
else:
    st.info("No products found")
