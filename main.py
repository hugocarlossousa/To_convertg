#Bibliotecas Utilizadas
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen 
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import sys

#interface KivyMD
KV = '''

<Tela1>

    name: 't1'

    MDFloatLayout:
        md_bg_color:('#DCDCDC')
          
        MDTopAppBar:                
            title: "SPEED HITTER CONVEYOR"
            right_action_items: [["close", lambda x: root.fechar()]]
            md_bg_color: ("#eb640c")
            pos_hint: {'top': True}
        
        MDBoxLayout:
            size_hint: 1, 0.08
            md_bg_color: ("#FFFAFA") 

        Image:
            source:"Vlogo.png"
            size_hint_x: 0.288
            pos_hint: {'center_x': 0.842,'center_y': 0.0355}               

        MDTextField:
            id: tf1
            hint_text: "Conveyor Actual Speed m/s"
            mode: "rectangle"
            size_hint_x: .70
            line_color_focus: "#4682B4"
            line_color_normal: "white"
            text_color_focus: "#4682B4"
            hint_text_color_normal:"#eb640c"
            hint_text_color_focus:"#ff8c00"
            pos_hint: {'center_x': 0.5,'center_y': 0.78}

        MDTextField:
            id: tf2
            hint_text: "Target Speed"
            mode: "rectangle"
            size_hint_x: .70
            line_color_focus: "#4682B4"
            line_color_normal: "white"
            text_color_focus: "#4682B4"
            hint_text_color_normal:"#eb640c"
            hint_text_color_focus:"#ff8c00"
            pos_hint: {'center_x': 0.5,'center_y': 0.65}

        MDTextField:
            id: tf3
            hint_text: "Seted module RPM"
            mode: "rectangle"
            size_hint_x: .70
            line_color_focus: "#4682B4"
            line_color_normal: "white"
            text_color_focus: "#4682B4"
            hint_text_color_normal:"#eb640c"
            hint_text_color_focus:"ff8c00"
            pos_hint: {'center_x': 0.5,'center_y': 0.52}

            
        MDIconButton:
            icon: "eraser"
            theme_icon_color: "Custom"
            icon_color:("#eb640c")
            icon_size: "45sp"  
            pos_hint: {'center_x': 0.40,'center_y': 0.40} 
            on_press:
                root.limpar()
        
        MDLabel: 
            text: "Clear"
            color: ("#eb640c")
            font_size: 20
            halign: 'center'
            pos_hint: {'center_x': 0.40,'center_y': 0.35}

        MDIconButton:
            icon: "check-circle"
            theme_icon_color: "Custom"
            icon_color:("#eb640c")
            icon_size: "45sp"  
            pos_hint: {'center_x': 0.60,'center_y': 0.40} 
            on_press:
                root.analisar()
        
        MDLabel: 
            text: "Run"
            color: ("#eb640c")
            font_size: 20
            halign: 'center'
            pos_hint: {'center_x': 0.60,'center_y': 0.35}
                
        MDLabel:
            id: resp 
            text: " "
            color: '#4682B4'
            font_size: 40
            halign: 'center'
            pos_hint: {'center_x': 0.5,'center_y': 0.21}
        



'''

#Root - Main Screen.
class Tela1(MDScreen):

    #Limpar os campos anteriormente preenchidos
    def limpar(self):
        self.ids.tf1.text = ''
        self.ids.tf2.text = ''
        self.ids.tf3.text = ''
        self.ids.resp.text = ''

    #Fechar a janela 
    def fechar(self):
        sys.exit()

    #Programa Principal   
    def analisar(self):
        #ENTRADAS 
        
        #Popup de Erro
        self.dialog = MDDialog(title = 'ERROR*', text = 'Invalid Velue!\nPlease, set a new valid value',
                                buttons = [MDFlatButton(text= 'OK',
                                on_release = self.liberar)])

        try:
            #Entrada - Velocidade de Aferida no transpotador
            r1= str(self.ids.tf1.text)
            conveyorSpeed= float(r1.replace(',','.'))
            #Entrada - Velocidade desejada
            r2= str(self.ids.tf2.text)
            targetSpeed= float(r2.replace(',','.'))
            #Entrada - Pre set RPM modulo
            r3= str(self.ids.tf3.text)
            moduleRpmSpeed= float(r3.replace(',','.'))

            #PROCESAMENTO
            #Caucula o rendimento aproximado da gasolina "gambirra"
            vf = moduleRpmSpeed/conveyorSpeed * targetSpeed

            #exporta os valores obtidos durante o calculo para o label resp
            self.ids.resp.text = ('SET THE PARAMETER IN MODULE\n {:0.2f} - RPM'.format(vf))
        except:
            self.dialog.open()
    
    #Função leração de erros
    def liberar(self, obj):
        
        self.dialog.dismiss()

# Activation Class
class SpeedHitterApp(MDApp):

    def build(self):
        Builder.load_string(KV)
        sm = MDScreenManager()
        sm.add_widget(Tela1())
        
       
        return sm

SpeedHitterApp().run()
