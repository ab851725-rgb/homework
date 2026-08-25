class Streamer:    
  def live(self):       
    return "Запускаю стрим! Подписывайтесь, ставьте лайки!"
  def earn(self):       
    return "Заработал 500 донатов за 2 часа"

class TikToker:    
  def live(self):        
   return "Снимаю трендовый тикток под песню месяца!"
  
  def viral(self):        
      return "Набрал 3 миллиона просмотров за сутки!"

class Mutant:    
  def live(self):        
    return "Я... я свечусь в темноте... это мой вайб..."
    
  def superpower(self):       
    return "Летаю и стреляю лазерами из глаз"

class GlowStreamer1(Streamer, Mutant):
    pass
    def ultimate_content(self):
        return  f'ультимейт {self.earn()} и {self.superpower()}'

class ViralCyborg1(TikToker, Mutant):
    pass
    def ultimate_content(self):
        return  f'ультимейт {self.viral()} и {self.superpower()}'

class DonateMage1(Streamer, TikToker):
    pass
    def ultimate_content(self):
        return  f'ультимейт {self.earn()} и {self.viral()}'


GlowStreamer = GlowStreamer1()
ViralCyborg = ViralCyborg1()
DonateMage = DonateMage1()
streamers = [GlowStreamer, ViralCyborg, DonateMage]
print(GlowStreamer.live())
print(GlowStreamer1.__mro__)
print(ViralCyborg.live())
print(ViralCyborg1.__mro__)
print(DonateMage.live())
print(DonateMage1.__mro__)
for i in streamers:
  print(i.ultimate_content())