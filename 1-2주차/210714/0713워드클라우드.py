from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
t = '''
현지시간으로 지난 12일 오후 이라크 남부 도시 나시리야의 코로나바이러스 
병원에서 불이 나 현재까지 최소 50명이 사망하고, 10여명이 다쳤다고 AP통신 
등이보도했습니다. 이번 화재는 전기 합선이나 산소 용기 폭발 등에 의해 발생한 
것으로 추정되고 있습니다. 올해 들어 이라크에서 병원 화재로 입원 치료 중이던 코로나19 
환자들이 사망한 사고가 발생한 것은 이번이 두 번째로 앞서 지난 4월 수도 바그다드에 위치한 
한 병원에서 산소 용기 폭발로 인한 불이 나 최소 82명이 숨졌습니다.
'''

spwords=set(STOPWORDS)
#spwords.add('병원에서')


wc = WordCloud('C://Windows//Fonts//gulim' ,
               background_color='white',
               stopwords=spwords,
               width=1000,
               height=1000,
               max_words=100,
               max_font_size=150
               )
wc.generate(t)

plt.imshow(wc, interpolation='lanczos')
plt.axis('off')
plt.show()

