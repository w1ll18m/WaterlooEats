import { useState, useEffect } from "react";
import useFetch from "../../hooks/useFetch";
import ProductGrid from "./ProductGrid";
import PaginatedProductGrid from "./PaginatedProductGrid";
import ResterauntHeader from "./ResterauntHeader";
import { Button, Typography } from "@mui/material";

const BASE_URL = "http://127.0.0.1:5000/"
const RESTERAUNT_ID = 1

function ResterauntPage() {
    let tag_path = BASE_URL + "tag/list/" + RESTERAUNT_ID.toString()
    const {data: tagData, isLoading: tagLoading, error: tagError, setData: setTagData} = useFetch(tag_path)
    const [tagList, setTagList] = useState(tagData)

    const [scrollPosition, setScrollPosition] = useState(0)
    const [currentPosition, setCurrentPosition] = useState(0)

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

    function tagActive(tag_id) {
        let grid = document.getElementById(tag_id)

        // executes if product grid has not been rendered 
        if (!grid) return false

        let grid_pos = grid.getBoundingClientRect();

        // returns true if grid's position in the viewport is at the top of the page
        if (grid_pos.top <= scrollPosition && grid_pos.bottom >= scrollPosition) {   
            return true
        } else {
            return false
        }
    }

    useEffect(() => {
        setTagList(tagData)
    }, [tagData])

    useEffect(() => {
        // sets currentPosition to current scroll position of the window
        function handleScroll() {
            const cur_pos = window.scrollY
            setCurrentPosition(cur_pos)
        }

        // causes the ResterauntPage component to rerender every time page is scrolled (NEED REFACTORING)
        window.addEventListener('scroll', handleScroll)

        // stores the position of the top of the page into scrollPosition variable
        let product_div = document.getElementById("product_div")
        let div_pos = product_div.getBoundingClientRect();
        setScrollPosition(div_pos.top)

        return () => {
            window.removeEventListener('scroll', handleScroll)
        }
    }, [])

    return (
        <div style={{height: "100vh"}}>
            <div style={{height: "25%"}}>
                <ResterauntHeader resteraunt_id={RESTERAUNT_ID}/>
            </div>
            <div style={{height:"75%", display: "flex"}}>
                <div id="tag_div" style={{width: "15%"}}> 
                    {tagList && tagList.map((tag) => {
                        return(
                            <div style={{marginBottom: "7.5%", marginLeft: "7.5%"}}>
                                <Button variant="text" 
                                    onClick={() => navigateToTag(tag.tag_id)} 
                                    sx={{fontWeight: "medium", color: "black", position: "fixed"}} 
                                    size="small">
                                    {/* underlines button content if grid's position is at the top of the page */}
                                    {tagActive("tag_" + tag.tag_id) ? <u>{tag.tag_name}</u> : tag.tag_name}
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
                            {tagActive("all_products") ? <u>All Products</u> : <p>All Products</p>}
                        </Button>
                        <br/>
                    </div>
                </div>
                <div id="product_div" style={{width: "85%"}}>
                    {tagList && tagList.map((tag) => {
                        let path = BASE_URL + "product-tags/list-product-by-tag/" + tag.tag_id.toString()
                        return(
                            <div id={"tag_" + tag.tag_id} style={{marginRight: "1%"}}>
                                <PaginatedProductGrid load_endpoint={path} tag_name={tag.tag_name} items_per={6}/>
                            </div>
                        )
                    })}
                    <div id="all_products" style={{marginRight: "1%"}}> 
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