# -*- coding: utf-8 -*-

# Original source : https://github.com/jskDr/keraspp/blob/master/ex9_4_2_tfwithkeras.py

# tensorflow session 선언
import tensorflow as tf
config = tf.ConfigProto()
config.gpu_options.allow_growth=True # gpu 메모리를 필요한 만큼만 할당
sess = tf.Session(config=config)

# keras session과 tensorflow session을 연결
from keras import backend as K
K.set_session(sess)

# 분류 DNN 모델 구현 ########################
from keras.models import Sequential, Model
from keras.layers import Dense, Dropout
from keras.metrics import categorical_accuracy, categorical_crossentropy

# DNN 클래스
class DNN():
    def __init__(self, Nin, Nh_l, Nout): # Nin은 입력 크기, Nh_I는 은닉층 크기, Nout은 출력층 크기 
        self.X_ph = tf.placeholder(tf.float32, shape=(None, Nin)) # 입력 플레이스홀더
        self.L_ph = tf.placeholder(tf.float32, shape=(None, Nout)) # 레이블 플레이스홀더
        
        # Modeling
        H = Dense(Nh_l[0], activation='relu')(self.X_ph) # 입력 플레이스홀더를 넣고, 첫 번째 은닉층 크기만큼 반환하는 은닉층1
        H = Dropout(0.5)(H) # 드롭아웃
        H = Dense(Nh_l[1], activation='relu')(H) # 입력 플레이스홀더를 넣고, 두 번째 은닉층 크기만큼 반환하는 은닉층1 
        H = Dropout(0.25)(H) # 드롭아웃
        self.Y_tf = Dense(Nout, activation='softmax')(H) # 출력층, 소프트맥스
        
        # Operation
        self.Loss_tf = tf.reduce_mean(
            categorical_crossentropy(self.L_ph, self.Y_tf)) # 손실함수는 레이블과 출력 간 크로스엔트로피
        self.Train_tf = tf.train.AdamOptimizer().minimize(self.Loss_tf) # 최적화함수는 에이담
        self.Acc_tf = categorical_accuracy(self.L_ph, self.Y_tf) # 정확도 산출은 케라스 함수로
        self.Init_tf = tf.global_variables_initializer() # 초기화 함수는 텐서플로 글로벌 전역 초기화 함수

# 데이터 준비 ##############################
import numpy as np
from keras import datasets  # mnist
from keras.utils import np_utils  # to_categorical

def Data_func():
    (X_train, y_train), (X_test, y_test) = datasets.mnist.load_data() # mnist 데이터 불러오기

    Y_train = np_utils.to_categorical(y_train) # 훈련 정답값을 원핫인코딩
    Y_test = np_utils.to_categorical(y_test) # 테스트 정답값을 원핫인코딩

    # MLP에 넣기위해 평탄화
    L, W, H = X_train.shape 
    X_train = X_train.reshape(-1, W * H)
    X_test = X_test.reshape(-1, W * H)

    # 데이터 정규화 (MinMax 정규화)
    X_train = X_train / 255.0
    X_test = X_test / 255.0

    return (X_train, Y_train), (X_test, Y_test) # 데이터셋 반환


# 학습 효과 분석 ##############################
from keraspp.skeras import plot_loss, plot_acc # 손실함수 및 정확도 그래프 출력 함수
import matplotlib.pyplot as plt

def run(model, data, sess, epochs, batch_size=100): # 모델, 데이터, 세션, 에폭, 배치크기를 입력으로 받음
    # epochs = 2
    # batch_size = 100
    (X_train, Y_train), (X_test, Y_test) = data # 데이터 입력
    sess.run(model.Init_tf) # 세션 초기화
    with sess.as_default(): # 입력 세션을 기본 세션으로 설정하고, 
        N_tr = X_train.shape[0] # 훈련셋 크기 얻기
        for epoch in range(epochs): # 매 에폭마다
            for b in range(N_tr // batch_size): # 훈련셋 / 배치사이즈 개수 만큼
                X_tr_b = X_train[batch_size * (b-1):batch_size * b] # 배치 데이터 획득
                Y_tr_b = Y_train[batch_size * (b-1):batch_size * b] # 배치 레이블 획득

                model.Train_tf.run(feed_dict={model.X_ph: X_tr_b, model.L_ph: Y_tr_b, K.learning_phase(): 1}) # 최적화함수 실행, 플레이스홀더에 각각 배치 데이터 입력, 학습 페이즈 입력
            loss = sess.run(model.Loss_tf, feed_dict={model.X_ph: X_test, model.L_ph: Y_test, K.learning_phase(): 0}) # 손실함수 계산
            acc = model.Acc_tf.eval(feed_dict={model.X_ph: X_test, model.L_ph: Y_test, K.learning_phase(): 0}) # 정확도 계산 
            print("Epoch {0}: loss = {1:.3f}, acc = {2:.3f}".format(epoch, loss, np.mean(acc))) # 에폭 당 손실값 및 정확도 표시

# 분류 DNN 학습 및 테스팅 ####################
def main():
    Nin = 784 # 입력 크기
    Nh_l = [100, 50] # 은닉층 크기
    number_of_class = 10 # 클래스 개수
    Nout = number_of_class # 출력 크기

    data = Data_func() # 데이터 불러오기
    model = DNN(Nin, Nh_l, Nout) # 모델 선언

    run(model, data, sess, 10, 100) # 학습 실행


if __name__ == '__main__': # 메인함수 실행
    main()
