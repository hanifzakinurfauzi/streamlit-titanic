# Project Titanic Survival Prediction
Repository ini merupakan salah satu proses dari project mandiri Bootcamp Data Science di Qarir Generator Batch 28 dan disusun oleh:<br>
Hanif Zaki Nur Fauzi<br>
Data source: https://www.kaggle.com/code/alexisbcook/titanic-tutorial

## Introduction
Tenggelamnya RMS Titanic terjadi pada dini hari tanggal 15 April 1912 di Samudra Atlantik Utara, empat hari setelah pelayaran perdananya dari Southampton menuju New York City. Titanic merupakan kapal samudra terbesar yang beroperasi pada masa itu, yang mengangkut kurang lebih 2.224 penumpang ketika menabrak gunung es kira-kira pukul 23.40 (waktu kapal) pada hari Minggu, 14 April 1912. Kapal tersebut tenggelam dua jam empat puluh menit kemudian pada pukul 02.20 waktu kapal (05:18 GMT) hari Senin, 15 April, mengakibatkan lebih dari 1.500 penumpang dan awak tewas, menjadikannya salah satu bencana maritim masa damai paling mematikan dalam sejarah.

Titanic menerima enam peringatan bahaya es laut pada tanggal 14 April, tetapi sedang melaju dengan kecepatan 22 knot (41 km/h) ketika pengintai melihat keberadaan gunung es. Kapal tidak bisa berbelok dengan cukup cepat dan menabrak gunung es, yang melekukkan sisi kanan kapal dan melubangi enam dari enam belas kompartemennya. Titanic dirancang untuk tetap mengapung jika empat kompartemennya bocor, dan para awak segera menyadari bahwa kapal akan tenggelam. Mereka menggunakan suara mara bahaya dan pesan radio nirkabel untuk meminta bantuan selagi penumpang diungsikan ke sekoci.

Resource: https://id.wikipedia.org/wiki/Tenggelamnya_RMS_Titanic#Referensi

## Problem Statement
Melalui analisis dataset Titanic, tujuan penelitian ini adalah untuk menentukan faktor-faktor yang paling signifikan dalam mempengaruhi tingkat kelangsungan hidup penumpang. Analisis akan mencakup variabel seperti kelas tiket, jenis kelamin, usia, dan jumlah saudara kandung atau pasangan. Hasil analisis ini diharapkan dapat memberikan wawasan yang mendalam tentang karakteristik penumpang yang memiliki tingkat kelangsungan hidup lebih tinggi, yang pada gilirannya dapat membantu dalam pengembangan kebijakan keselamatan kapal atau rekomendasi pelayaran di masa depan.

## Metrics Evaluation<br>
```Precision```: Karena kita ingin meminimalkan jumlah prediksi yang salah tentang orang yang tidak selamat. Artinya kita ingin mengurangi prediksi salah orang yang tidka selamat tapi kenyataannya selamat.<br>
```AUC-ROC```: mengukur kualitas keseluruhan model untuk memisahkan kelas positif dan negatif. Kurva ROC (Receiver Operating Characteristic) memplot nilai True Positive Rate (Recall) terhadap False Positive Rate pada berbagai threshold. AUC-ROC memberikan nilai keseluruhan kinerja model independen dari threshold.

## Variable Description<br>
```PassengerId```: unique id number to each passenger<br>
```Survived```: passenger survive(1) or died(0)<br>
```Pclass```: passenger class<br>
```Name```: name<br>
```Sex```: gender of passenger<br>
```Age```: age of passenger<br>
```SibSp```: number of siblings/spouses<br>
```Parch```: number of parents/children<br>
```Ticket```: ticket number<br>
```Fare```: amount of money spent on ticket<br>
```Cabin```: cabin category<br>
```Embarked```: port where passenger embarked (C = Cherbourg, Q = Queenstown, S = Southampton)<br>

## Deployment
Link : [Titanic Survival Prediction](https://app-titanic-7fmcqhnbcemxds8y28ornq.streamlit.app/)
