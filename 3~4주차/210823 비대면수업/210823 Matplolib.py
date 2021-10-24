import matplotlib.pyplot as plt
import numpy as np
# plt.plot([1,2,3,4])     #matplotlib의 기본 그래프 출력지정
# plt.ylabel('Somethere')     #y축의 라벨 지정
# plt.xlabel('data')      #x축의 라벨 지정
# plt.show()      #그래프를 보여주는 함수 print()와 같은 역할

# plt.plot([1,2,3,4],[2,4,6,8]) #plt.plot([x축 값],[y축 값])
# plt.show()

# plt.plot([1,2,3,4],[2,4,6,8] , 'ro-') #plt.plot([x축 값],[y축 값], #'ro-' = '포인터 \ 색 포인터 특성 \ 선 특성' )
# plt.show()

# # plt.plot([10, 20, 30, 40], [1, 4, 9, 16]) 에 색상, 선스타일, 선너비, 마커, 마커사이즈, 마커테두리색, 마커테두리 두께 지정
# plt.plot([10,20,30,45] , [1,4,9,16] ,
#          color='g' , linestyle ='--' , linewidth ='5' , marker ='o' ,
#          markersize ='15' , markeredgecolor = 'b' , markeredgewidth='3')
# plt.show

# # 위 지정방식을 약어로 표기
# plt.plot([10,20,30,45] , [1,4,9,16] ,
#          c='g' , ls ='--' , lw ='5' , marker ='o' ,
#          ms ='15' , mec = 'b' , mew='3' ,mfc='r')
# plt.show

# plt.plot([10,20,30,45] , [1,4,9,16] ,
#          c='g' , ls ='--' , lw ='5' , marker ='o' ,
#          ms ='15' , mec = 'b' , mew='3' ,mfc='r')
# plt.axis([0,100,0,50])
# plt.xlim(5.45)
# plt.ylim(-5.20)
# plt.show

# t = np.arange(0., 5., 0.2)
# plt.title("Multiple line graphs on a window, Method 1")
# plt.plot(t,t,'r--', t, 0.5*t**2 ,'bs:',t, 0.3* t**2 ,'g^-.')

# plt.title("Multiple line graphs on a window, Method 2")
# plt.plot([1,4,9,16] ,
#          c='r' , lw = 5 , ls= '--' , marker = 'o' ,ms=15 , mec = 'g' , mew = 5 , mfc ='m')
# plt.plot([5,3,7,11] ,
#          c='k' , lw = 7 , ls= ':' , marker = 's' , ms =10 , mec = 'b' , mew = 5 , mfc ='m')

# 사인, 코사인 그래프
# X = np.linspace(-np.pi , np.pi , 256)
# C , S = np.cos(X) , np.sin(X)
# plt.plot(X,C,'b--' , label = 'Cosign')
# plt.plot(X,S, 'r:' , label = 'sine')
# plt.xlabel('Angle(radian)')
# plt.ylabel('Ampltude')
# plt.legend()
# plt.show
#
# # 범례추가
# # 사인, 코사인 그래프
# X = np.linspace(-np.pi , np.pi , 256)
# C , S = np.cos(X) , np.sin(X)
# plt.plot(X,C,'b--')
# plt.plot(X,S, 'r:')
# plt.xlabel('Angle(radian)')
# plt.ylabel('Ampltude')
# plt.show

# # 1행 3열 중 1열
# plt.subplot(131)
# plt.plot([1,3,5])
#
# # 1행 3열 중 2열
# plt.subplot(132)
# plt.scatter([1,2,3],[1,2,3])
#
# # 1행 3열 중 3열
# ax = plt.subplot(133)
# plt.bar([10,11,12] , [1,3,5])
#
# # 1행 3열 중 3열 -> 축 전달 방식 : 3.3부터는 지원하지 않음
# plt.subplot(ax)
# plt.bar([13,14,15] , [2,4,8])
#
# # 자동 레이아웃
# plt.tight_layout()