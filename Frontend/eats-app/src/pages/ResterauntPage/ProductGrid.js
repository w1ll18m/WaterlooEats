import { useState, useEffect } from "react";
import useFetch from "../../hooks/useFetch";
import ProductCard from "./ProductCard";
import { Grid } from "@mui/material";

function ProductGrid({load_endpoint}) {
    const {data, isLoading, error, setData} = useFetch(load_endpoint)
    const [productList, setProductList] = useState([])

    function createProductCard(product) {
        return (
            <ProductCard    
                product_id = {product.product_id}
                image_url = {product.image_url}
                product_name = {product.product_name}
                calorie_count = {product.calorie_count}
                price = {product.price}
            />
        )
    }
    
    useEffect(() => {
        setProductList(data)
    }, data)

    function lol() {
        return(
            <div>
                Hello
            </div>
        )
    }

    return(
        <Grid container spacing={2}>
            {isLoading && lol()}
            {productList && productList.map((product) => {
                return(
                    <Grid item xs={12} sm={4} md={2} lg={2}>
                        {createProductCard(product)}
                    </Grid>
                )
            })}
        </Grid>
    )
}

export default ProductGrid