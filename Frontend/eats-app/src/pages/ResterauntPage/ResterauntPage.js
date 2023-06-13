import { useState, useEffect } from "react";
import useFetch from "../../hooks/useFetch";
import ProductGrid from "./ProductGrid";
import { Button, Typography } from "@mui/material";

const BASE_URL = "http://127.0.0.1:5000/"
const RESTERAUNT_ID = 1

function ResterauntPage() {
    let tag_path = BASE_URL + "tag/list/" + RESTERAUNT_ID.toString()
    const {data: tagData, isLoading, error, setData: setTagData} = useFetch(tag_path)
    const [tagList, setTagList] = useState(tagData)
    // const [isScrolled, setIsScrolled] = useState(true)
    // const [scrollPosition, setScrollPosition] = useState(0)

    function navigateToTag(tag_id) {
        let navigate_id = tag_id

        if (tag_id != "all_products") {
            navigate_id = "tag_" + tag_id
        } 

        let navigate_item = document.getElementById(navigate_id)

        if (navigate_item) {
            navigate_item.scrollIntoView({behavior: 'smooth'});
        }
    }

    useEffect(() => {
        setTagList(tagData)
    }, tagData)

    /*
    useEffect(() => {
        const handleScroll = () => {
            setScrollPosition(window.scrollY)
            setIsScrolled(window.scrollY > 0)
        }
    }, [])
    */

    return (
        <div>
            <div style={{height: "30%"}}>
                <br/>
                <br/>
                <br/>
                <br/>
                <br/>
            </div>
            <div style={{height:"70%", display: "flex"}} id="product_list">
                <div style={{width: "40%"}}> 
                    {tagList && tagList.map((tag) => {
                        return(
                            <div style={{marginBottom: "7.5%", marginLeft: "7.5%"}}>
                                <Button variant="text" 
                                    onClick={() => navigateToTag(tag.tag_id)} 
                                    sx={{fontWeight: "medium", color: "black", position: "fixed"}} 
                                    size="small">
                                    {tag.tag_name}
                                </Button>
                                <br/>
                            </div>
                        )
                    })}
                    <div style={{marginBottom: "7.5%", marginLeft: "7.5%"}}>
                        <Button variant="text" 
                            onClick={() => navigateToTag("all_products")} 
                            sx={{fontWeight: "medium", color: "black", position: "fixed"}} 
                            size="small">
                            All Products
                        </Button>
                        <br/>
                    </div>
                </div>
                <div>
                    {tagList && tagList.map((tag) => {
                        let path = BASE_URL + "product-tags/list-product-by-tag/" + tag.tag_id.toString()
                        return(
                            <div id={"tag_" + tag.tag_id}>
                                <Typography variant="h4" sx={{marginBottom: "2%", marginTop: "1.5%", fontWeight: "bold"}}>
                                    {tag.tag_name}
                                </Typography>
                                <ProductGrid load_endpoint={path}/>
                            </div>
                        )
                    })}
                    <div id="all_products"> 
                        <Typography variant="h4" sx={{marginBottom: "2%", marginTop: "1.5%", fontWeight: "bold"}}>
                            All Products
                        </Typography>
                        <ProductGrid load_endpoint={BASE_URL + "product/list/" + RESTERAUNT_ID.toString()}/>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default ResterauntPage