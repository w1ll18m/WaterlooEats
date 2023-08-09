import { useAuth0 } from "@auth0/auth0-react";
import AccountCircle from '@mui/icons-material/AccountCircle';
import IconButton from '@mui/material/IconButton';
import { Avatar } from "@mui/material";

const ProfileIcon = () => {
    const {user, isAuthenticated} = useAuth0()

    return (    
        <IconButton size="large" edge="end" color="inherit">
            {isAuthenticated ? <Avatar src={user.picture}/> : <AccountCircle/>}
        </IconButton>
    )
}

export default ProfileIcon