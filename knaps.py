import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from collections import OrderedDict

#Metrics
from sklearn.metrics import make_scorer, accuracy_score,precision_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score ,precision_score,recall_score,f1_score

#Model Select
from sklearn.model_selection import KFold,train_test_split,cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import  LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier 
from sklearn import svm
from sklearn import metrics 

st.title(' Aplikasi Web Data Mining')
st.write("""
### Klasifikasi tingkat kematian gagal jantung menggunakan Metode Decision tree, Random forest, dan SVM
""")
st.write('## 1. Introduction')
st.write('Gagal Jantung adalah kondisi ketika otot jantung tidak dapat memompa darah sebagaimana mestinya untuk memenuhi kebutuhan tubuh. Darah merupakan cairan terpenting yang beredar ke seluruh tubuh dengan menyuplai oksigen ke seluruh bagian tubuh. Penyakit kardiovaskular (CVDs) adalah penyebab kematian nomor 1 secara global, merenggut sekitar 17,9 juta nyawa setiap tahun, yang merupakan 31% dari semua kematian di seluruh dunia. Ancaman masalah kardiovaskular yang terus-menerus ini telah meningkat karena pilihan gaya hidup yang buruk seiring dengan sikap acuh tak acuh terhadap kesehatan. Dengan sebagian besar orang berjuang dengan masalah mental, kebiasaan seperti penggunaan tembakau, pola makan yang tidak sehat dan obesitas, ketidakaktifan fisik dan penggunaan alkohol yang berbahaya telah dilakukan oleh populasi massal. Oleh karena itu, orang yang memiliki risiko kardiovaskular tinggi memerlukan deteksi dan manajemen dini di mana model pembelajaran mesin dapat sangat membantu!')

st.sidebar.write("""
            ### Pilih Metode yang anda inginkan :"""
            )
algoritma=st.sidebar.selectbox(
    'Pilih', ('Decision Tree','Random Forest','SVM')
)

st.write('## 2. About Dataset (Heart Failure)')
data_hf = pd.read_csv("https://raw.githubusercontent.com/ranianuraini/datminweb/main/fetal_health.csv")
st.write("Dataset Heart Failure : (https://raw.githubusercontent.com/ranianuraini/datminweb/main/fetal_health.csv) ", data_hf)

st.write('Dataset Description :')
st.write('1. baseline value: Baseline Fetal Heart Rate (FHR)')
st.write('2. accelerations: Number of accelerations per second')
st.write('3. fetal_movement: Number of fetal movements per second')
st.write('4. uterine_contractions: Number of uterine contractions per second')
st.write('5. light_decelerations: Number of LDs per second')
st.write('6. severe_decelerations: Number of SDs per second')
st.write('7. prolongued_decelerations: Number of PDs per second')
st.write('8. abnormal_short_term_variability: Percentage of time with abnormal short term variability')
st.write('9. mean_value_of_short_term_variability: Mean value of short term variability')
st.write('10. spercentage_of_time_with_abnormal_long_term_variabilityex: Percentage of time with abnormal long term variability')

st.write('Jumlah baris dan kolom :', data_hf.shape)

X=data_hf.iloc[:,0:12].values 
y=data_hf.iloc[:,12].values

st.write('Jumlah kelas : ', len(np.unique(y)))

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)


#Train and Test split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)

# Decision Tree
decision_tree = DecisionTreeClassifier() 
decision_tree.fit(X_train, y_train)  
Y_pred = decision_tree.predict(X_test) 
accuracy_dt=round(accuracy_score(y_test,Y_pred)* 100, 2)
acc_decision_tree = round(decision_tree.score(X_train, y_train) * 100, 2)

cm = confusion_matrix(y_test, Y_pred)
accuracy = accuracy_score(y_test,Y_pred)
precision =precision_score(y_test, Y_pred,average='micro')
recall =  recall_score(y_test, Y_pred,average='micro')
f1 = f1_score(y_test,Y_pred,average='micro')
print('Confusion matrix for DecisionTree\n',cm)
print('accuracy_DecisionTree: %.3f' %accuracy)
print('precision_DecisionTree: %.3f' %precision)
print('recall_DecisionTree: %.3f' %recall)
print('f1-score_DecisionTree : %.3f' %f1)

# Random Forest
random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(X_train, y_train)
Y_prediction = random_forest.predict(X_test)
accuracy_rf=round(accuracy_score(y_test,Y_prediction)* 100, 2)
acc_random_forest = round(random_forest.score(X_train, y_train) * 100, 2)


cm = confusion_matrix(y_test, Y_prediction)
accuracy = accuracy_score(y_test,Y_prediction)
precision =precision_score(y_test, Y_prediction,average='micro')
recall =  recall_score(y_test, Y_prediction,average='micro')
f1 = f1_score(y_test,Y_prediction,average='micro')
print('Confusion matrix for Random Forest\n',cm)
print('accuracy_random_Forest : %.3f' %accuracy)
print('precision_random_Forest : %.3f' %precision)
print('recall_random_Forest : %.3f' %recall)
print('f1-score_random_Forest : %.3f' %f1)

#SVM
SVM = svm.SVC(kernel='linear') 
SVM.fit(X_train, y_train)
Y_prediction = SVM.predict(X_test)
accuracy_SVM=round(accuracy_score(y_test,Y_pred)* 100, 2)
acc_SVM = round(SVM.score(X_train, y_train) * 100, 2)

cm = confusion_matrix(y_test, Y_pred)
accuracy = accuracy_score(y_test,Y_pred)
precision =precision_score(y_test, Y_pred,average='micro')
recall =  recall_score(y_test, Y_pred,average='micro')
f1 = f1_score(y_test,Y_pred,average='micro')
print('Confusion matrix for SVM\n',cm)
print('accuracy_SVM : %.3f' %accuracy)
print('precision_SVM : %.3f' %precision)
print('recall_SVM : %.3f' %recall)
print('f1-score_SVM : %.3f' %f1)

st.write('## 3. Akurasi Metode')

results = pd.DataFrame({
    'Model': ['Decision Tree','Random Forest','SVM'],
    'Accuracy_score':[accuracy_dt,
                      accuracy_rf,accuracy_SVM
                     ]})
result_df = results.sort_values(by='Accuracy_score', ascending=False)
result_df = result_df.reset_index(drop=True)
result_df.head(9)
st.write(result_df)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(['Decision Tree', 'Random Forest','SVM'],[accuracy_dt, accuracy_rf, accuracy_SVM])
plt.show()
st.pyplot(fig)

baseline value = st.sidebar.number_input("baseline value =", min_value=106 ,max_value=160)
accelerations = st.sidebar.number_input("accelerations =", min_value=0, max_value=0.2)
fetal_movement = st.sidebar.number_input("fetal_movement =", min_value=0 , max_value=0.48)
uterine_contractions = st.sidebar.number_input("uterine_contractions =", min_value=0, max_value=0.01)
light_decelerations = st.sidebar.number_input("light_decelerations =", min_value=0, max_value=0.01)
severe_decelerations = st.sidebar.number_input("severe_decelerations =", min_value=0 ,max_value=0)
prolongued_decelerations = st.sidebar.number_input("prolongued_decelerations =", min_value=0, max_value=0.01)
abnormal_short_term_variability = st.sidebar.number_input("abnormal_short_term_variability =", min_value=12, max_value=87)
mean_value_of_short_term_variability = st.sidebar.number_input("mean_value_of_short_term_variability =", min_value=0.2, max_value=7)
spercentage_of_time_with_abnormal_long_term_variabilityex = st.sidebar.number_input("spercentage_of_time_with_abnormal_long_term_variabilityex =", min_value=0, max_value=91)
submit = st.sidebar.button("Submit")

if submit :
    if algoritma == 'Decision Tree' :
        X_new = np.array([[baseline value, accelerations, fetal_movement, uterine_contractions, light_decelerations, severe_decelerations, prolongued_decelerations,
        abnormal_short_term_variability, mean_value_of_short_term_variability, spercentage_of_time_with_abnormal_long_term_variabilityex]])
        prediksi = decision_tree.predict(X_new)
        if prediksi == 1 :
            st.sidebar.write(""" # Hasil Prediksi :
             rekiso meninggal tinggi""")
        else : 
            st.sidebar.write("""# Hasil Prediksi :
             rekiso meninggal rendah""")
    elif algoritma == 'Random Forest' :
        X_new = np.array([[baseline value, accelerations, fetal_movement, uterine_contractions, light_decelerations, severe_decelerations, prolongued_decelerations,
        abnormal_short_term_variability, mean_value_of_short_term_variability, spercentage_of_time_with_abnormal_long_term_variabilityex]])
        prediksi = random_forest.predict(X_new)
        if prediksi == 1 :
            st.sidebar.write("""# Hasil Prediksi :
            rekiso meninggal tinggi""")
        else : 
            st.sidebar.write("""# Hasil Prediksi :
            rekiso meninggal rendah""")
    else :
        X_new = np.array([[baseline value, accelerations, fetal_movement, uterine_contractions, light_decelerations, severe_decelerations, prolongued_decelerations,
        abnormal_short_term_variability, mean_value_of_short_term_variability, spercentage_of_time_with_abnormal_long_term_variabilityex]])
        prediksi = SVM.predict(X_new)
        if prediksi == 1 :
            st.sidebar.write("""# Hasil Prediksi :
            rekiso meninggal tinggi""")
        else : 
            st.sidebar.write("""# Hasil Prediksi :
            rekiso meninggal rendah""")