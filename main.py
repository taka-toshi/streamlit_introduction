import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

st.write("レイアウト")
number=st.sidebar.slider("あなたの好きな数字は？",0,100,50)
"あなたの好きな数字",number
st.sidebar.write(number)

st.write("プログレスバーの表示")
"Start!!"
latest_iteration=st.empty()
bar=st.progress(0)
for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.02)
"Done!!"

st.title("Streamlit 超入門")
st.write("DataFrame")

df=pd.DataFrame({
    "1列目":[1,2,3,4],
    "2列目":[10,20,30,40]
})
st.dataframe(df.style.highlight_max(axis=0),width=100,height=100)
st.write(df.style.highlight_max(axis=0),width=100,height=100)
st.table(df.style.highlight_max(axis=0))

df2=pd.DataFrame(
    np.random.rand(20,3),
    columns=["a","b","c"]
)
st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

df3=pd.DataFrame(
    np.random.rand(100,2)/[50,50] +[35.69,139.70],
    columns=["lat","lon"]
)
st.map(df3)

st.write("Display Image")
img=Image.open("sample-photo.jpg")
st.image(img,caption="kesiki",use_column_width=True)

st.write("Interactive Widgets")
if st.checkbox("Show Image"):
    img=Image.open("sample-photo.jpg")
    st.image(img,caption="kesiki",use_column_width=True)

option = st.selectbox(
    "あなたが好きな数字を教えて下さい。",
    list(range(1,11))
)
"あなたの数字は、",option,"です。"

text1=st.text_input("あなたの趣味を教えて下さい。")
"あなたの趣味：",text1

condition=st.slider("あなたの今の調子は？",0,100,50)
"コンディション：",condition

left_column,right_column=st.columns(2)
button=left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander=st.expander("問い合わせ")
expander.write("問い合わせ内容を書く")

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)