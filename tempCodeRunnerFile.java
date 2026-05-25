public class LyricsSync {

    public static void main(String[] args) throws InterruptedException {

        System.out.println("Paredes - Jorge e Matheus...");
        Thread.sleep(16000); // espera até 0:16

        mostrarVerso("(Eu tentei tebalhar, ta dificil concentrar)");
        Thread.sleep(4000);

        mostrarVerso("(Fim de tarde é pior... ao se por do sol...)");
        Thread.sleep(5000);

        mostrarVerso("(Ela me esperava, com o sorriso estampado na cara)");
        Thread.sleep(6000);

        mostrarVerso("(Hoje o dia ta passando, a saudade apertando, e eu sozinho nessa casa)");
        Thread.sleep(7000);

        mostrarVerso("(Ah se essas paredes não falassem...)");
        Thread.sleep(4000);

        mostrarVerso("(A se o travesseiro não lembrasse... todas as noites de amor)");
        Thread.sleep(4000);
        
        mostrarVerso("(Que eu vivi com você...)")
        Thread.sleep(2000);

         mostrarVerso("(Ah se essa cama não lembrasse)")
        Thread.sleep(2000);

         mostrarVerso("(Ah se o espelho mostrasse...)")
        Thread.sleep(2000);

         mostrarVerso("(Você aqui... pra eu conseguir dormir...)")
        Thread.sleep(2000);


        System.out.println("\nFim do trecho.");
    }

    public static void mostrarVerso(String verso);
            throws InterruptedException {

        limparTela();

        System.out.println();
        System.out.println("♪ " + verso);
        System.out.println();
    }

    public static void limparTela() {

        for (int i = 0; i < 40; i++) {
            System.out.println();
        }
    }
}