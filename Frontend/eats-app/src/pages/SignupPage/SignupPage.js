import { useState } from "react"
import { Box, TextField, Typography, Divider, Button } from "@mui/material"
import { useFormik } from "formik"
import * as Yup from 'yup'
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { useNavigate } from "react-router-dom";

const BASE_URL = "http://127.0.0.1:5000/"

const SignupPage = () => {
    const navigate = useNavigate()

    const handleSignup = async () => {
        const myPath = BASE_URL + "/auth/add-user"
        let formData = new FormData()
        formData.append("username", formik.values.username)
        formData.append("email", formik.values.email)
        formData.append("password", formik.values.password)

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
            navigate("/login")
        } catch(error) {
            console.log("handleSignup Error:", error)
        }
    }

    const formikValidationSchema = Yup.object({
        username: Yup.string()
            .required("Username is Required")
            .min(3, "Username Must Be More Than 3 Characters")
            .max(30, "Username Must Be Less Than 30 Characters"),
        email: Yup.string()
            .max(50, "Email must be less than 50 characters")
            .required("Email is Required")
            .email("Invalid Email Address") ,
        password: Yup.string().required("Passowrd is Required")
            .min(5, "Password Must Be More Than 5 Characters")
            .max(30, "Password Must Be Less Than 30 Characters")
            .required("Password is Required")
    })

    const formik = useFormik({
        initialValues: {username: "", email: "", password: ""},
        onSubmit: handleSignup,
        validationSchema: formikValidationSchema
    })

    return(
        <Box>
            <Box sx={{marginTop: 10, marginLeft: 30, marginRight: 30}} style={{display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center", gap: 10}}>
                <Typography variant="h5">Create your account</Typography>

                <TextField 
                    name="username" label="Username" 
                    value={formik.values.username} onChange={formik.handleChange} onBlur={formik.handleBlur} 
                    variant="outlined" error={formik.touched.username && formik.errors.username} style={{width: "50%"}}
                />
                {formik.touched.username && formik.errors.username && 
                    <Box style={{width: "50%"}}>
                        <Typography color="red" variant="subtitle2">{formik.errors.username}</Typography>
                    </Box>
                }

                <TextField 
                    name="email" label="Email" 
                    value={formik.values.email} onChange={formik.handleChange} onBlur={formik.handleBlur} 
                    variant="outlined" error={formik.touched.email && formik.errors.email} style={{width: "50%"}}
                />
                {formik.touched.email && formik.errors.email && 
                    <Box style={{width: "50%"}}>
                        <Typography color="red" variant="subtitle2">{formik.errors.email}</Typography>
                    </Box>
                }

                <TextField 
                    name="password" label="Password" 
                    value={formik.values.passowrd} onChange={formik.handleChange} onBlur={formik.handleBlur} 
                    variant="outlined" type="password"
                    error={formik.touched.password && formik.errors.password} style={{width: "50%"}}
                />
                {formik.touched.password && formik.errors.password && 
                    <Box style={{width: "50%"}}>
                        <Typography color="red" variant="subtitle2">{formik.errors.password}</Typography>
                    </Box>
                }

                <Button onClick={formik.handleSubmit} disabled={!formik.isValid} variant="contained" style={{width: "50%"}}>Sign Up</Button>
            </Box>
        </Box>
    )
}

export default SignupPage