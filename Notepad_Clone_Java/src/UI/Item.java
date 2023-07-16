package UI;

import javax.swing.JMenuItem;
public class Item extends JMenuItem{
    private static final long serialVersionUID = 8532439481035757726L;

	Item(String nomeItem){
        this.setText(nomeItem);
    }

}