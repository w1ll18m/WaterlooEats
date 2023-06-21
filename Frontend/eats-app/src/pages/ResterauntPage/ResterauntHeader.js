import { useState, useEffect } from "react";
import useFetch from "../../hooks/useFetch";
import { Card, CardContent, CardMedia, Typography, CardActionArea } from '@mui/material';
import { Box } from "@mui/material";

const BASE_URL = "http://127.0.0.1:5000/"

function ResterauntHeader({resteraunt_id}) {
    let resteraunt_path = BASE_URL + "resteraunt/get/" + resteraunt_id.toString()
    const {data: resterauntData, isLoading: resterauntLoading, error: resterauntError, setData: setResterauntData} = useFetch(resteraunt_path)
    const [resterauntInfo, setResterauntInfo] = useState({})

    useEffect(() => {
        setResterauntInfo(resterauntData)
    }, [resterauntData])

    return (
        <Box height={"100%"}>
            <Box height={"40%"} justifyContent={"center"}>
                <img 
                    src={resterauntInfo ? resterauntInfo.image_url : "https://validuspharma.com/wp-content/uploads/2019/06/nologo.png"}
                    style={{height: "100%", width: "100%", objectFit: "cover"}}
                />
            </Box>
            {resterauntInfo &&
                <div style={{marginLeft: "2%", marginTop: "1%"}}>
                    <Typography variant="h3" sx={{ fontFamily: 'Impact' }}>
                        {resterauntInfo.resteraunt_name}
                    </Typography>
                    <div style={{display: "flex"}}>
                        <Typography variant="subtitle1" sx={{ fontFamily: 'Times New Roman' }}>
                            {resterauntInfo.cuisine_type} • 
                            ${resterauntInfo.delivery_fee} Delivery Fee • {" "} 
                            <a href="/" style={{color: "black"}}>More Info</a>
                        </Typography>
                    </div>
                </div>
            }
        </Box>
    )
}

export default ResterauntHeader