import * as React from 'react';
import { useNavigate } from "react-router-dom";
import { Button, IconButton, AppBar, Box, Toolbar, Typography } from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';
import ProfileIcon from './ProfileIcon';
import { useAuth } from '../providers/AuthProvider';
import { useAuth0 } from '@auth0/auth0-react';

const NavBar = () => {
    const authentication = useAuth()
    const {isAuthenticated, loginWithRedirect, logout} = useAuth0()
    const navigate = useNavigate()

    const handleLogOut = () => {
        authentication.logout()
        logout()
    }

    return (
        <Box sx={{ flexGrow: 1 }}>
            <AppBar position="static">
                <Toolbar>
                    <IconButton size="large" edge="start" color="inherit" aria-label="menu" sx={{ mr: 2 }}>
                        <MenuIcon />
                    </IconButton>

                    <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                        WaterlooEats
                    </Typography>

                    {!isAuthenticated && <Button color="inherit" onClick={() => navigate("/login")}> Login </Button>}
                    {isAuthenticated && <Button color="inherit" onClick={() => navigate("/resteraunts")}> Resteraunts </Button>}
                    {isAuthenticated && <ProfileIcon/>}
                    {isAuthenticated && <Button color="inherit" onClick={handleLogOut}> Sign Out </Button>}
                </Toolbar>
            </AppBar>
        </Box>
    )
}

export default NavBar