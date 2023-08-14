import { useState } from "react"
import { Box, TextField, Typography, Divider, Button } from "@mui/material"
import { useFormik } from "formik"
import * as Yup from 'yup'
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { useNavigate } from "react-router-dom";
import { useAuth0 } from "@auth0/auth0-react";

const SignupPage = () => {
    const navigate = useNavigate()
    const { getIdTokenClaims, getAccessTokenSilently } = useAuth0()

    const getAccessToken = async () => {
        let accessToken = await getAccessTokenSilently({
            scope: "read:data"
        })
        console.log("Access Token", accessToken)
    }

    getAccessToken()

    const handleCreateUser = async () => {
        const idToken = await getIdTokenClaims()
        const myPath = process.env.REACT_APP_SERVER_BASE_URL + "/auth/create-user"
        let formData = new FormData()

        formData.append("uuid", idToken.sub)
        formData.append("email", idToken.email) 
        formData.append("phone_number", formik.values.phone_number)
        formData.append("address", formik.values.address)

        try {
            const res = await fetch(myPath, {method: "POST", body: formData})
            const response = await res.text()
            if (!res.ok) {
                toast.error(response, {
                    position: toast.POSITION.TOP_RIGHT,
                    autoClose: 3000
                })
                return
            }
            navigate("/resteraunts")
        } catch(error) {
            console.error("handleSignup Error:", error)
        }
    }

    const formikValidationSchema = Yup.object({
        phone_number: Yup.string()
            .required("Phone Number is Required")
            .length(10, "Invalid Phone Number")
            .matches(/^\d{10}$/, "Invalid Phone Number"),
        address: Yup.string()
            .max(128, "Address must be less than 128 Characters")
            .required("Address is Required")
    })

    const formik = useFormik({
        initialValues: {phone_number: "", address: ""},
        onSubmit: handleCreateUser,
        validationSchema: formikValidationSchema
    })

    return(
        <Box>
            <Box sx={{marginTop: 10, marginLeft: 30, marginRight: 30}} style={{display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center", gap: 10}}>
                <Typography variant="h5">Finish creating your account</Typography>

                <TextField 
                    name="phone_number" label="Phone Number"
                    value={formik.values.phone_number} onChange={formik.handleChange} onBlur={formik.handleBlur} 
                    variant="outlined" error={formik.touched.phone_number && formik.errors.phone_number} style={{width: "50%"}}
                />
                {formik.touched.phone_number && formik.errors.phone_number && 
                    <Box style={{width: "50%"}}>
                        <Typography color="red" variant="subtitle2">{formik.errors.phone_number}</Typography>
                    </Box>
                }

                <TextField 
                    name="address" label="Home Address" 
                    value={formik.values.address} onChange={formik.handleChange} onBlur={formik.handleBlur} 
                    variant="outlined" error={formik.touched.address && formik.errors.address} style={{width: "50%"}}
                />
                {formik.touched.address && formik.errors.address && 
                    <Box style={{width: "50%"}}>
                        <Typography color="red" variant="subtitle2">{formik.errors.address}</Typography>
                    </Box>
                }

                <Button onClick={formik.handleSubmit} disabled={!formik.isValid} variant="contained" style={{width: "50%"}}>Sign Up</Button>
            </Box>
        </Box>
    )
}

export default SignupPage