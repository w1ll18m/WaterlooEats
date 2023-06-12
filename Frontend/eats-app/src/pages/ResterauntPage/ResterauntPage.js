import { useState, useEffect } from "react";
import ProductCard from "./ProductCard";
import { Box, Grid } from "@mui/material";

const BASE_URL = "http://127.0.0.1:5000/"

function ResterauntPage() {
    const [productList, setProductList] = useState([])

    useEffect(() => {
        loadProductList().then((res) => {
            setProductList(res)
        })
    }, [])

    const loadProductList = async() => {
        try {
            let resteraunt_id = 1
            let path = BASE_URL + 'product/list/' + resteraunt_id.toString()

            const res = await fetch(path)
            const response = await res.json()

            console.log("This is loadProductList response:", response)
            return response
        } 
        catch (err) {
            console.log("Error on loadProductList: ", err)
        }
    }

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

    return (
        <div>
            <div>
                <Grid container spacing={2}>
                    {productList.map((product) => {
                        return(
                            <Grid item xs={12} sm={4} md={2} lg={2}>
                                {createProductCard(product)}
                            </Grid>
                        )
                    })}
                </Grid>
            </div>
        </div>
    )
}

export default ResterauntPage