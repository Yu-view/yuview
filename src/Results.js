import { List, ListItem, ListItemButton, ListItemIcon, ListItemText } from "@mui/material";
import { Apple, Google } from '@mui/icons-material'
import { QueryContext } from "./context";
import { useContext } from "react";

function ResultsDisplay() {
  const { listings } = useContext(QueryContext);
  return (
    <List>
      {
        listings.map(({ name }) => {
          return (
            <ListItem disablePadding>
              <ListItemButton>
                <ListItemIcon>
                  <Apple />
                </ListItemIcon>
                <ListItemText primary={name} />
              </ListItemButton>
            </ListItem>)
        })
      }
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

export default ResultsDisplay;