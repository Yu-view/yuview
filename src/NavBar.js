import { AppBar, Typography, InputBase, Toolbar, Stack, IconButton, Menu, MenuItem } from "@mui/material";
import { styled, alpha } from '@mui/material/styles'
import { Search, Settings, ShoppingCart } from "@mui/icons-material";
import { useContext, useState } from "react";
import { QueryContext } from "./context";

const SearchBox = styled('div')(({ theme }) => ({
    position: 'relative',
    borderRadius: theme.shape.borderRadius,
    backgroundColor: alpha(theme.palette.common.white, 0.15),
    '&:hover': {
        backgroundColor: alpha(theme.palette.common.white, 0.25),
    },
}));

const StyledInputBase = styled(InputBase)(({ theme }) => ({
    color: 'inherit',
    '& .MuiInputBase-input': {
        padding: theme.spacing(1, 1, 1, 1),
        // vertical padding + font size from searchIcon
        transition: theme.transitions.create('width'),
        marginLeft: theme.spacing(1),
        width: '100%',
        [theme.breakpoints.up('md')]: {
            width: '60ch',
        },
    },
}));

function NavBar() {
    const [anchorEl, setAnchorEl] = useState(null);
    const [userSearch, setUserSearch] = useState(null);
    const { query, setQuery } = useContext(QueryContext);

    const handleMenu = (event) => {
        setAnchorEl(event.currentTarget);
    }
    const handleClose = () => {
        setAnchorEl(null);
    }
    const handleInput = (event) => {
        setUserSearch(event.target.value);
    }
    const handleSearch = () => {
        setQuery({
            query: userSearch,
            search: true
        })
        console.log(query)
    }

    return (
        <AppBar position="sticky">
            <Toolbar sx={{ justifyContent: "space-between" }}>
                <Stack spacing={1} direction="row" alignItems="center">
                    <ShoppingCart />
                    <Typography
                        variant="h5"
                        noWrap
                        components="div"
                    >
                        Yuview
                    </Typography>
                </Stack>
                <SearchBox>
                    <StyledInputBase
                        placeholder="Search..."
                        onChange={handleInput}
                    />
                    <IconButton
                        onClick={handleSearch}>
                        <Search />
                    </IconButton>
                </SearchBox>
                <IconButton
                    onClick={handleMenu}>
                    <Settings />
                </IconButton>
                <Menu
                    id="menu"
                    anchorEl={anchorEl}
                    keepMounted
                    open={Boolean(anchorEl)}
                    onClose={handleClose}
                    transformOrigin={{ horizontal: 'right', vertical: 'top' }}
                    anchorOrigin={{ horizontal: 'right', vertical: 'bottom' }}>
                    <MenuItem>History</MenuItem>
                    <MenuItem>Themes</MenuItem>
                </Menu>
            </Toolbar>
        </AppBar>
    )
}

export default NavBar;