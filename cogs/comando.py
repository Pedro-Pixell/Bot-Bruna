# Listagens dos Import's
import discord
from discord.ext import commands

# Definir classe
class comando(commands.Cog):
    def __init__(self, client):
        self.client = client

# Usuario TheuZN
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def p0000(self, ctx):
        await ctx.send("PROCESSANDO... p e r m i t i d o")
        await ctx.send("ADIQUIRINDO... p e r m i t i d o")
        await ctx.send("Os pacotes foram adiquiridos com sucesso!")
        await ctx.send("Olá TheuZN!")
        await ctx.send("Seus dados discord estão sendo registrados...")
        await ctx.send("Servidores... Ip:1654740")
        await ctx.send("Feito. ABRINDO BASE DE COMANDOS.")
        await ctx.send("Você está acessando o a central de comandos de BOT-Bruna")
        await ctx.send("Comandos        .: SETUP.PY :.")
        await ctx.send("WARNING : This is an operable central for creating commands, this area is restricted to DEVELOPERS only.")
        await ctx.send("Digite _Criarcomando para começarmos a criação de um novo comando.")
        


# Usuario PEDRÃO
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def o0000(self, ctx):
        await ctx.send("PROCESSANDO... p e r m i t i d o")
        await ctx.send("ADIQUIRINDO... p e r m i t i d o")
        await ctx.send("Os pacotes foram adiquiridos com sucesso!")
        await ctx.send("Olá M10L1NH033br!")
        await ctx.send("Seus dados discord estão sendo registrados...")
        await ctx.send("Servidores... Ip:1654739")
        await ctx.send("Feito. ABRINDO BASE DE COMANDOS.")
        await ctx.send("Você está acessando o INTERIOR de BRUNA-BOT")
        await ctx.send("Comandos        .: SETUP.PY :.")
        await ctx.send("_Bruna          _sobre          _paixao")
        await ctx.send("_funcionamento       _Desenvolvedor      _dizer")
        await ctx.send("_sugada            _piadas          _Criarcomando")
        await ctx.send("_bomdia            _Usuario         _Mboas")
        await ctx.send("_boas           _Mruin        _loreninha")
        await ctx.send("_ruins         _sugestao")




#Central de ajustes da Bruna
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def Desenvolvedor(self, ctx):
        await ctx.send("Ok!! deixa eu so entrar em minha DataBase ...")
        await ctx.send("Entrando...")
        await ctx.send("Acessando...")
        await ctx.send("Acesso permitido. Operante.")
        await ctx.send("AVISO: Apenas um desenvolvedor pode acesar este campo.")
        await ctx.send("_Usuario + @Usuario")



# Usuarios cadastrados
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def Usuario(self, ctx, *, palavra=None):
        if palavra is None:
            await ctx.send("_Usuario + @Usuario")
            return
        await ctx.send(f"Ok {palavra} você está entrando agora em minha base de dados Ip:1654738")
        await ctx.send(f"{palavra} digite sua senha de acesso dessa forma: _suasenha")



# Comandos da Bruna 
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def comandos(self, ctx):
        await ctx.send("🌸Oiii! Tudo certinho? Logo a seguir estão meus comandos🌸")
        await ctx.send("👾 _funcionamento  -  Diz se estou em funcionamento")
        await ctx.send("👾 _paixao  -  Diz minha primeira paixão ")
        await ctx.send("👾 _dizer  -  Você coloca o comando e a palavra seguinte eu repito!")
        await ctx.send("👾 _sobre  -  Você coloca o comando e logo a frente o @Nome de um usuario do servidor.")
        await ctx.send("👾 _Bruna  -  Esse comando diz um pouco sobre mim!!")
        await ctx.send("👾 _piadas  -  Nesse comando eu consigo falar algumas piadas pra você!")
        await ctx.send("👾 _bomdia  -  Bom Diaaaaa!!")



# Quem é a Bruna?
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def Bruna(self, ctx):
        await ctx.send("Oii! Eu sou a Bruna!! Fui colocada no mundo tecnologico pelo meu pai, o M10L1NH033br, ele é o cara!! Se quiser saber meus comandos digite _comandos .")



# A Bruna está em funcionamento
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def funcionamento(self, ctx):
        await ctx.send("Aeeee, hiupi!! To funcionando!! Obrigada!!")
    


# Zuando o Phillipe
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def Vaca(self, ctx):
        await ctx.send("O Vaca, conhecido como Phillipe, é uma pessoa adoravel. Né Phillipe? Hoje tem.")



# Comida
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def paixao(self, ctx):
        await ctx.send("COMIDA!!! Eu adoro comer, em especial doces, sejam eles Bolos, Musses, Balas, Mel, Biscoitos, Chocolates e tudo. Oque você indicaria a mim da proxima vez? Só vale oque você já comeu, se não eu não como. Não gosto de ser a primeira a provar coisas estranhas. coloca aii! _sugestao + comida escolhida")

    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def sugestao(self, ctx, *, palavra=None):
        if palavra is None:
            await ctx.send("_sugestao + a comida escolhida, você esqueceu dela")
            return
        await ctx.send(f"{palavra}!! ahh da próxima vez vou pedir isso ao meu padeiro, espero que ele tenha. rsrsrsr")



# Bobeiras da Bruna
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def sugada(self, ctx,):
        await ctx.send("Isso é mais de noite seu bobinho. rsrsrrs")

    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def dizer(self, ctx, *, palavra=None):
        if palavra is None:
            await ctx.send("_dizer + alguma coisa")
            return
        await ctx.send(f"{palavra}")

    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def loreninha(self, ctx):
        await ctx.send("Essa é uma das pessoas mais incriveis que ja conheci!! Sabia que a @lorenanta tem uma banca de questões de matemática junto com o @PEDRÃO e com o @fabinus  isso é muito topiiii !!! aiaia")



# Logo a seguir estão as piadas que a Bruna pode contar!
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def piadas(self, ctx):
        await ctx.send("Oiii! então.. aqui conto umas piadas pra você, mas antes preciso saber quais piadas você quer ouvir?")
        await ctx.send("_Mruins  -  São só as piores piadas kkkkkkkkkkkkk")
        await ctx.send("_ruins  -  São piadas ruins mas que dão pro gasto.")
        await ctx.send("_boas  -  São piadas legais, divertidas")
        await ctx.send("_Mboas  -  São só as melhoeres piadas kkkkkkkkkkkk")

    # Piadas Mruins
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def Mruins(self, ctx):
        await ctx.send("Então... no momento so tenho uma kkkkk. Mas quando for atualizada terei mais! Lá vai!!")
        await ctx.send("Por que o homem invisível tinha sérios problemas no consultorio?")
        await ctx.send("Porque todos os médicos se recusavam a vê-lo.")
    # Piadas ruins
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def ruins(self, ctx):
        await ctx.send("Então... no momento so tenho uma kkkkk. Mas quando for atualizada terei mais! Lá vai!!")
        await ctx.send("O que o tomate foi fazer no banco?")
        await ctx.send("Tirar extrato.")
    # Piadas boas
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def boas(self, ctx):
        await ctx.send("Então... no momento so tenho uma kkkkk. Mas quando for atualizada terei mais! Lá vai!!")
        await ctx.send("Qual o rio mais azedo do mundo?")
        await ctx.send("O Rio Solimões.")
    # Piadas Mboas
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def Mboas(self, ctx):
        await ctx.send("Então... no momento so tenho uma kkkkk. Mas quando for atualizada terei mais! Lá vai!!")
        await ctx.send("Por que o macaco-prego não entra na água?")
        await ctx.send("Porque ele tem medo do Tubarão-Martelo.")



# A Bruna sabe quem cada um é
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def sobre(self, ctx, *, usuario:discord.Member=None):
        if usuario is None:
            await ctx.send("_sobre + @usuario")
            return
        string = f"Nome : {usuario.name}\nId : {usuario.id}\nAvatar : {usuario.avatar_url}"
        await ctx.send(string)



#Central de Criação de novos Comandos.
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def Criarcomando(self, ctx):
        await ctx.send("Ok!! Obtendo informações...")
        await ctx.send("Acessando...")
        await ctx.send("Acesso permitido.")
        await ctx.send("Vamos lá! Defina uma palavra para servir de comando, exemplo : _ola, _oi e etc")
        await ctx.send("Após ter sido digitada a palavra insira oque @Bruninha deverá responder após o comando ter sido acionado. Dentro de segundos o comando deverá ser aceito.")
        await ctx.send("INTERNET QUALITY INFORMATION: 31ms")



#Novos Comandos
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def gay(self, ctx):
        await ctx.send("Parabéns agora você é um gay !!")

    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def bomdia(self, ctx):
        await ctx.send("Bom dia!! Como você está?")
 

def setup(client):
    client.add_cog(comando(client))
