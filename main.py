from chatbot import ChatBot
myChatBot = ChatBot()
#apenas carregar um modelo pronto
#myChatBot.loadModel()

#criar o modelo
myChatBot.createModel()

def chatDebug():
    myChatBot.setDebug(True)
    print("Bem vindo ao Chatbot DEBUG")

    pergunta = input("como posso te ajudar?\n")
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    # print(intencao)
    print(resposta)

    while (not intencao or (intencao and intencao[0]['intent']!="despedida")):
        pergunta = input("posso lhe ajudar com algo a mais?\n")
        resposta, intencao = myChatBot.chatbot_response(pergunta)
        print(resposta + "   [" + intencao[0]['intent'] + "]")

    print("Foi um prazer atendê-lo")
    
def chatFinal():
    print("Olá! Seja muito bem vindo ao assistente PIPE! Em que posso ajudar?\n")

    pergunta = input()
    resposta, intencao = myChatBot.chatbot_response(pergunta)

    print(resposta + "\n")

    while (not intencao or (intencao and intencao[0]['intent']!="despedida")):
        pergunta = input()
        resposta, intencao = myChatBot.chatbot_response(pergunta)
        print(resposta + "   [" + intencao[0]['intent'] + "]")
        print("\n")
    
    print("Espero que eu tenha sido de boa ajuda :) Até breve!")
    
#descomente o que deseja utilizar, comentando o outro

chatFinal()
#chatDebug()