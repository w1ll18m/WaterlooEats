import { useState } from "react";
import ProductCard from "./ProductCard";
import { Box, Grid } from "@mui/material";

function ResterauntPage() {
    const items = [
        {
            image_url: "https://mma.prnewswire.com/media/1227532/Wendys_4_for_4_Spicy_Chicken.jpg",
            product_name: "Spicy Crispy Sandwhich Combo",
            calories: "900",
            price: "$6.50"
        },
        {
            image_url: "https://media.npr.org/assets/img/2017/05/09/10-piece-chicken-nuggets-ss_0_custom-db31f599b4b36050d9a26986abaf75c76c655f37-s1100-c50.jpg",
            product_name: "Classic Breaded Chicken Nuggets",
            calories: "350",
            price: "$3.00"
        },
        {
            image_url: "https://people.com/thmb/SfTdO0MCEUX1h7v6sBZ3tX0Ylo8=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc():focal(277x0:279x2)/Wendys_Hot_Crispy_Fries-62b1b426bec34ea2b97d3c5c6041c82d.jpg",
            product_name: "French Fries",
            calories: "600",
            price: "$2.50"
        },
        {
            image_url: "https://www.wendys.com/sites/default/files/styles/max_325x325/public/2021-05/combos-305_medium_US_en.png?itok=TFnjsi9f",
            product_name: "Dave's Triple Combo",
            calories: "1200",
            price: "$12.99"
        },
        {
            image_url: "https://www.foodbusinessnews.net/ext/resources/2022/11/16/wendys-chicken-sandwich_LEAD.jpg?height=667&t=1668623216&width=1080",
            product_name: "Cheesy Mozerella Sandwhich",
            calories: "1025",
            price: "$8.75"
        },
        {
            image_url: "https://www.wendys.com/sites/default/files/styles/max_325x325/public/2021-05/wendys-kids-meal-129_medium_US_en.png?itok=OrSE2T4o",
            product_name: "Wendy's Kids Meal",
            calories: "460",
            price: "$6.50"
        },  
        {
            image_url: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLYhIYiuNffUebAWvfEe67s3JGrUGjP9Vk4w&usqp=CAU",
            product_name: "Sausage Breakfast Sandwhich Combo",
            calories: "850",
            price: "$6.75"
        },
        {
            image_url: "https://www.wendys.com/sites/default/files/styles/max_325x325/public/2021-05/frosty-126_medium_US_en.png?itok=kMWt88LW",
            product_name: "Vanilla Frosty",
            calories: "600",
            price: "$1.25"
        },
    ]

    function createProductCard(product) {
        return (
            <ProductCard
                image_url = {product.image_url}
                product_name = {product.product_name}
                calories = {product.calories}
                price = {product.price}
            />
        )
    }

    return (
        <div>
            <Grid container spacing={2}>
                {items.map((item) => {
                    return(
                        <Grid item xs={12} sm={4} md={2} lg={2}>
                            {createProductCard(item)}
                        </Grid>
                    )
                })}
            </Grid>
        </div>
    )
}

export default ResterauntPage