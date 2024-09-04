import streamlit as st

def predict_images(file) :
    import numpy as np
    from PIL import Image
    import matplotlib.pyplot as plt

    import cv2
    import tensorflow   as tf
#학습되어잇는모델
    resnet50 = tf.keras.applications.resnet.ResNet50(weights='imagenet', input_shape=(224,224,3))
    from tensorflow.keras.applications.imagenet_utils import decode_predictions
#리사이징 리쉬이핑 하고 머신돌리기
    image = np.array(Image.open(file))
    st.image(image, use_column_width=True)

    image_resized = cv2.resize(image,(224,224))
    image_reshaped = image_resized.reshape([1,224,224,3])
    predicted = resnet50.predict(image_reshaped)
     
    decode_predict = decode_predictions(predicted)
    return decode_predict[0]

st.title('이미지분류')
file = st.file_uploader('이미지를 올려주세요', type=['jpg','png','gif'])

if file is None:
    st.text('이미지를 선택하세용')
else:
    with st.spinner('Please Wait...'):
        predcited = predict_images(file)
        for i, pre in enumerate(predcited):
            st.success('{}위: {}({:.2f}%)'.format(i+1, pre[1],pre[2]*100))
