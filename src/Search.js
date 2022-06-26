import { List, ListItem, ListItemButton, ListItemIcon, ListItemText } from "@mui/material";
import {Inbox, Drafts, Money, Apple, Google} from '@mui/icons-material'

function Search() {
    return (
        <List>
          <ListItem disablePadding>
            <ListItemButton>
              <ListItemIcon>
                <Apple />
              </ListItemIcon>
              <ListItemText primary="Product 1" />
            </ListItemButton>
          </ListItem>
          <ListItem disablePadding>
            <ListItemButton>
              <ListItemIcon>
                <Google />
              </ListItemIcon>
              <ListItemText primary="Product 2" />
            </ListItemButton>
          </ListItem>
        </List>
    ) 
}

export default Search;