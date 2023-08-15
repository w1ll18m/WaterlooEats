import { useState, useEffect } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import  { createProductCard } from "./ProductCard";
import { Grid, Typography, IconButton, Button } from "@mui/material";
import ArrowCircleRightOutlinedIcon from '@mui/icons-material/ArrowCircleRightOutlined';
import ArrowCircleRightIcon from '@mui/icons-material/ArrowCircleRight';
import ArrowCircleLeftIcon from '@mui/icons-material/ArrowCircleLeft';
import ArrowCircleLeftOutlinedIcon from '@mui/icons-material/ArrowCircleLeftOutlined';

function PaginatedProductGrid({load_endpoint, tag_name, items_per}) {
    const { getAccessTokenSilently } = useAuth0()
    const [productList, setProductList] = useState([])
    const [isLoading, setIsLoading] = useState(true)
    const [error, setError] = useState(false)

    const [pageNumber, setPageNumber] = useState(1)
    
    const [leftHover, setLeftHover] = useState(false)
    const [rightHover, setRightHover] = useState(false)

    const incrementPageNumber = () => {
        setPageNumber(pageNumber + 1)
    }
    const decrementPageNumber = () => {
        if (pageNumber == 1) return
        setPageNumber(pageNumber - 1)
    }

    useEffect(() => {
        const fetchData = async () => {
            setIsLoading(true);

            try {
                let formData = new FormData()

                formData.append("page_num", pageNumber)
                formData.append("items_per", items_per)

                const token = await getAccessTokenSilently()

                const response = await fetch(load_endpoint, {
                    method: "POST",
                    body: formData,
                    headers: {
                        "Authorization": token
                    }
                })
                if (!response.ok) {
                  throw new Error("Failed to fetch data")
                }
        
                const data = await response.json()
                setProductList(data)
            } catch (error) {
                setError(error)
            } finally {
                setIsLoading(false)
            }
        }

        fetchData()
    }, [pageNumber])

    return(
        <div>
            <div style={{display: "flex"}}>
                <Typography variant="h4" sx={{marginBottom: "2%", marginTop: "1.5%", fontWeight: "bold"}}>
                    {tag_name}
                </Typography>
                <div style={{marginBottom: "2%", marginTop: "1.5%", marginLeft: "auto"}}>
                    <IconButton size="large" onClick={decrementPageNumber}
                                onMouseOver={() => setLeftHover(true)} onMouseLeave={() => setLeftHover(false)}>
                        {leftHover ? <ArrowCircleLeftIcon/> 
                                : <ArrowCircleLeftOutlinedIcon/>}
                    </IconButton>
                    <IconButton size="large" onClick={incrementPageNumber} 
                                onMouseOver={() => setRightHover(true)} onMouseLeave={() => setRightHover(false)}>
                        {rightHover ? <ArrowCircleRightIcon/> 
                                    : <ArrowCircleRightOutlinedIcon/>}  
                    </IconButton>
                </div>
            </div>

            <Grid container spacing={2}>
                {productList && productList.map((product) => {
                    return(
                        <Grid item xs={12} sm={4} md={2} lg={2}>
                            {createProductCard(product)}
                        </Grid>
                    )
                })}
            </Grid>
        </div>
    )
}

export default PaginatedProductGrid