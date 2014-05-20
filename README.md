QGame
=====

Quatris game developed in pyhton

### Widget tree
MainScreen(BoxLayout)
    GameGrid(GridLayout)
        GridEntries(Button) (1 per ogni cella, insomma i bottoni che formano il campo)
    Popup(Popup)
        ScreenManager(ScreenManager)
            ResultScreen(Screen)
                Boxlayout(vertical)
                    ResultLabel(Label)
                    BoxLayout(horizontal)
                        NewGameButton(Button)
                        SettingsButton(Button)
            SettingsScreen(Screen)
            
Separati nelle seguenti classi:
-MainScreen (eredita da BoxLayout)
-GameGrid (eredita da GridLayout) 
-Popup (eredita, sempre che sia possibile, da Popup)

Il main screen fa da "wrapper organizza tutto", per tenere il popup separato dal campo di gioco e non ridurre tutto a
funzioni e pastrocchi nestati sul campo.

GameGrid è la griglia di bottoni che fa da campo da gioco

Popup salta fuori alla fine della partita mostrando il risultato nel resultscreen. Le settings sono uno screen accessibile da qui che dovrebbero rimanere quindi nel popup

Non so bene se qualcuna di queste cose non si possa fare
