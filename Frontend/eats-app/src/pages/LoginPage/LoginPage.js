import { useState } from "react"
import { Box, TextField, Typography, Divider, Button } from "@mui/material"
import { useFormik } from "formik"
import * as Yup from 'yup'
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { useAuth } from "../../providers/AuthProvider";
import { useAuth0 } from "@auth0/auth0-react";
import { useNavigate } from "react-router-dom";
import GoogleButton from 'react-google-button'

const BASE_URL = "http://127.0.0.1:5000/"

const LoginPage = () => {
    const {user, isAuthenticated, login, logout} = useAuth()
    const {loginWithRedirect} = useAuth0()
    const navigate = useNavigate()
    const [currentStage, setCurrentStage] = useState("One")

    const stageOneValidationScheme = Yup.object({
        username: Yup.string(),
        email: Yup.string()
            .email("Invalid Email Address")
            .when('username', {
                is: usernameValue => !usernameValue || usernameValue.trim() == '',
                then: (schema) => schema.required("Email Address is Required"),
                otherwise: (schema) => schema.notRequired()
            })
    })

    const stageTwoValidationScheme = Yup.object({
        id: Yup.string().required("Username/Email is Required"),
        password: Yup.string()
            .max(80, "Exceeded Maximum Password Length")
            .required("Password is Required")
    })

    const validateExistingUser = (values) => {
        let myPath = BASE_URL + "/auth/checkuser"
        let formData = new FormData()
        let stage_one_id = ""
        if (values.email) {
            formData.append("identification", values.email)
            formData.append("identification_type", "email")
            stage_one_id = values.email
        } else {
            formData.append("identification", values.username)
            formData.append("identification_type", "username")
            stage_one_id = values.username
        }

        try {
            fetch(myPath, {method: "POST", body: formData}).then((res) => {
                if (res.status != 200) return
                res.json().then((response) => {
                    if (response.valid_user == true) {
                        setCurrentStage("Two")
                        formikStageTwo.setFieldValue("id", stage_one_id)
                    } else {
                        toast.error("User does not exist. Please create a new account", {
                            position: toast.POSITION.TOP_RIGHT,
                            autoClose: 3000
                        })
                    }
                })
            })
        } catch(error) {
            console.log("validateExistingUser Error: ", error)
        }
    }

    const userLogIn = (values) => {
        let myPath = BASE_URL + "/auth/login"
        let formData = new FormData()
        formData.append("username", values.id)
        formData.append("password", values.password)

        try {
            fetch(myPath, {method: "POST", body: formData}).then((res) => {
                if (res.status != 200) {
                    toast.error("User does not exist or incorrect password", {
                        position: toast.POSITION.TOP_RIGHT,
                        autoClose: 3000
                    })
                    return
                }
                res.json().then((response) => {
                    let authenticated_user = {
                        token: response.token,
                        role: response.role,
                        id: response.id
                    }
                    login(authenticated_user) 
                    navigate("/")
                })
            })  
        } catch(error) {
            console.log("userLogIn Error: ", error)
        }
    }

    const formikStageOne = useFormik({
        initialValues: {"username": "", "email": ""},
        onSubmit: validateExistingUser,
        validationSchema: stageOneValidationScheme
    })

    const formikStageTwo = useFormik({
        initialValues: {"id": "", "password": ""},
        onSubmit: userLogIn,
        validationSchema: stageTwoValidationScheme
    })

    return(
        <Box>
            {currentStage == "One" &&
                <Box sx={{marginTop: 10, marginLeft: 30, marginRight: 30}} style={{display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center", gap: 10}}>
                    <Typography variant="h5">What's your username or email?</Typography>

                    <TextField 
                        name="username" 
                        label="Username" 
                        value={formikStageOne.values.username} 
                        onChange={formikStageOne.handleChange} 
                        onBlur={formikStageOne.handleBlur} 
                        variant="outlined" 
                        style={{width: "50%"}}
                    />
                    {formikStageOne.touched.username && formikStageOne.errors.username && 
                        <Box style={{width: "50%"}}>
                            <Typography color="red" variant="subtitle2">{formikStageOne.errors.username}</Typography>
                        </Box>
                    }

                    <Box style={{display: "flex"}}>
                        <Divider />
                        <Typography> or </Typography>
                        <Divider/>
                    </Box>

                    <TextField 
                        name="email" 
                        label="Email" 
                        value={formikStageOne.values.email} 
                        onChange={formikStageOne.handleChange} 
                        onBlur={formikStageOne.handleBlur} 
                        variant="outlined" 
                        error={!formikStageOne.isValid}
                        style={{width: "50%"}}
                    />
                    {formikStageOne.touched.email && formikStageOne.errors.email && 
                        <Box style={{width: "50%"}}>
                            <Typography color="red" variant="subtitle2">{formikStageOne.errors.email}</Typography>
                        </Box>
                    }

                    <Button onClick={formikStageOne.handleSubmit} disabled={!formikStageOne.isValid} variant="contained" style={{width: "50%"}}>Continue to Sign In</Button>

                    <Box style={{display: "flex"}}>
                        <Divider/>
                        <Typography> or continue with third-party service </Typography>
                        <Divider/>
                    </Box>

                    <GoogleButton onClick={loginWithRedirect} style={{width: "50%"}}/>
                </Box>
            }
            {currentStage == "Two" &&
                <Box sx={{marginTop: 10, marginLeft: 30, marginRight: 30}} style={{display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center", gap: 10}}>
                    <Typography variant="h5">Enter your password</Typography>

                    <TextField 
                        name="id" label="Username/Email" 
                        value={formikStageTwo.values.id} onChange={formikStageTwo.handleChange} onBlur={formikStageTwo.handleBlur} 
                        variant="outlined" 
                        style={{width: "50%"}}
                        InputProps={{
                            readOnly: true,
                        }}
                    />

                    <TextField 
                        name="password" label="Password" 
                        value={formikStageTwo.values.password} onChange={formikStageTwo.handleChange} onBlur={formikStageTwo.handleBlur} 
                        variant="outlined" type="password"
                        error={!formikStageTwo.isValid}
                        style={{width: "50%"}}
                    />
                    {formikStageTwo.touched.password && formikStageTwo.errors.password && 
                        <Box style={{width: "50%"}}>
                            <Typography color="red" variant="subtitle2">{formikStageTwo.errors.password}</Typography>
                        </Box>
                    }

                    <Button onClick={formikStageTwo.handleSubmit} disabled={!formikStageTwo.isValid} variant="contained" style={{width: "50%"}}>Log In to WaterlooEats</Button>
                </Box>
            }
        </Box>
    )
}

export default LoginPage