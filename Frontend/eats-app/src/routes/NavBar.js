import * as React from 'react';
import { useNavigate } from "react-router-dom";
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import AccountCircle from '@mui/icons-material/AccountCircle';
import { useAuth } from '../providers/AuthProvider';

const NavBar = () => {
    const authentication = useAuth()
    const navigate = useNavigate()

    const handleLogOut = () => {
        authentication.logout()
        navigate("/login")
    }

    return (
        <Box sx={{ flexGrow: 1 }}>
            <AppBar position="static">
                <Toolbar>
                    <IconButton
                        size="large"
                        edge="start"
                        color="inherit"
                        aria-label="menu"
                        sx={{ mr: 2 }}
                    >
                        <MenuIcon />
                    </IconButton>
                    <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                        WaterlooEats
                    </Typography>
                    {!authentication.user && 
                        <Button color="inherit" onClick={() => navigate("/login")}>
                            Login
                        </Button>
                    }
                    {!authentication.user && 
                        <Button color="inherit" onClick={() => navigate("/sign-up")}>
                            Sign Up
                        </Button>
                    }
                    {authentication.user && 
                        <Button color="inherit" onClick={navigate("/resteraunts")}>
                            Resteraunts
                        </Button>
                    }
                    {authentication.user && 
                        <IconButton size="large" edge="end" color="inherit">
                            <AccountCircle />
                        </IconButton>
                    }
                    {authentication.user && 
                        <Button color="inherit" onClick={handleLogOut}>
                            Sign Out
                        </Button>
                    }
                </Toolbar>
            </AppBar>
        </Box>
    )
}

export default NavBar