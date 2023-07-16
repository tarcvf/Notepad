package Func;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

import javax.swing.JFileChooser;
import javax.swing.JOptionPane;
public class Func {
	public Func(){
		
	}
	public String Abrir() {
		System.out.println("chamada a função Abrir");
		JFileChooser c = new JFileChooser();
		c.setCurrentDirectory(new File("/home/"));
		c.showOpenDialog(c);
		System.out.println(c.getSelectedFile().getAbsolutePath());
		return c.getSelectedFile().getAbsolutePath();
	}
	public void Salvar(String caminho, String texto) {
		System.out.println("chamada a função Salvar\n"+caminho);
		try(FileWriter f = new FileWriter(caminho)){
			f.write(texto);
		}catch(Exception e){
			System.out.println("Erro: "+e);
		}
		
	}
	public String Saveas(String texto)  {
		System.out.println("chamada a função SalvarComo");
		JFileChooser c = new JFileChooser();
		c.showSaveDialog(c);
		String path = c.getSelectedFile().getAbsolutePath();
		try(BufferedWriter b = new BufferedWriter(new FileWriter(path))){
			
		}catch(IOException e){
			JOptionPane.showMessageDialog(null,"Não foi possivel abrir o arquivo\n"+ e, "Erro ao abrir arquivo", 0);
			return null;

		}
		return path;
	}
}
