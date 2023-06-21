import { useState } from "react";
import { Card, CardContent, CardMedia, Typography, CardActionArea } from '@mui/material';
import { Box } from "@mui/material";

function ProductCard({product_id, image_url, product_name, calorie_count, price}) {

    const cardOnClick = () => {
        console.log("clicked!")
    }

    return (
        <Card variant="outlined" sx={{ maxWidth: 300, maxHeight: 400 }}>
            <CardActionArea onClick={cardOnClick}>
                <CardMedia
                    sx={{ height: 150 }}
                    image={image_url}
                    title={product_name}
                />
                <CardContent>
                    <Typography gutterBottom variant="body5" component="div">
                        {product_name}
                    </Typography>
                    <Box sx={{display: "flex", justifyContent: "space-between"}}>
                        <Typography variant="body2" color="text.secondary">
                            (Cals: {calorie_count})
                        </Typography>
                        <Typography variant="body2" color="text.secondary" sx={{alignSelf: "end"}}>
                            ${price.toFixed(2)}
                        </Typography>
                    </Box>
                </CardContent>
            </CardActionArea>
        </Card>
    )
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

export { ProductCard, createProductCard }