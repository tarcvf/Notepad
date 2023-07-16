package UI;

import java.io.File;
import java.util.Scanner;

import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JScrollPane;
import javax.swing.JMenuBar;
import Func.Func;
import javax.swing.JOptionPane;

public class Janela extends JFrame {
    private static final long serialVersionUID = 6818723520219925371L;
	String caminho;
    @SuppressWarnings("deprecation")
    
	public Janela() {
        //Bloco onde constroi a janela
        this.setTitle("Notepad JAVA - NOVO");
        this.setSize(600, 600);
        this.setDefaultCloseOperation(3);
        //Bloco onde declara as variaveis de barra de menu e menus
        JMenuBar BarraMenu = new JMenuBar();
        JMenu MenuArquivo = new JMenu("Arquivo");
        JMenu MenuEditar = new JMenu("Editar");
        JMenu MenuSobre = new JMenu("Sobre");
        
        //Bloco onde se cria os itens do menu arquivo
        Item abrirItem = new Item("Abrir");
        Item novoItem = new Item("Novo");
        Item salvarItem = new Item("Salvar");
        Item salvar_como_Item = new Item("Salvar como");
        //Bloco onde atribui itens ao menu abrir
        MenuArquivo.add(abrirItem);
        MenuArquivo.add(novoItem);
        MenuArquivo.add(salvarItem);
        MenuArquivo.add(salvar_como_Item);
        //Bloco onde associa menus a barra de menu
        BarraMenu.add(MenuArquivo);
        BarraMenu.add(MenuEditar);
        BarraMenu.add(MenuSobre);
        //Bloco onde associa a barra de menu a janela principal
        BarraMenu.show(true);
        this.setJMenuBar(BarraMenu);
        //Adicionando texto e scroll
        Texto texto = new Texto();
        this.add(texto);
        JScrollPane sp = new JScrollPane(texto);
        this.add(sp);
        //Atribuir funções
        Func lf = new Func();
        abrirItem.addActionListener(lambda ->{
        	
            try{
            caminho = lf.Abrir();
            File f = new File(caminho);
            Scanner sc = new Scanner(f);
            StringBuilder stb = new StringBuilder();
            while(sc.hasNextLine()){
            String line = sc.nextLine();
            stb.append(line).append("\n");
                }
            sc.close();
            texto.setText(stb.toString());
            this.setTitle("Notepad JAVA - "+caminho);
            stb = null;
            } 
            catch (Exception e)
            {
                System.out.println(e);
                return;
            }
        });
        salvarItem.addActionListener(lambda ->{
            if(caminho != null){
                lf.Salvar(caminho, texto.getText());
            }else{
              caminho = lf.Saveas(texto.getText());
              this.setTitle(caminho);
                
            }
            
        });
        salvar_como_Item.addActionListener(lambda ->{
           caminho = lf.Saveas(texto.getText());
           this.setTitle(caminho);
        });
        //Mostra a janela
        this.setVisible(true);
        
        
    }

}

