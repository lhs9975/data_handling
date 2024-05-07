# csv 행열 반전

import pandas as pd

# CSV 파일 불러오기
data = pd.read_csv(r"C:\Users\MSI\Desktop\회사\개발\MLTA\company_data\trace_data_excel\tra_abnormal_concat_10_2\abnormal_concat_10_2.csv",
                   header=None)  # 'input.csv'는 사용자의 CSV 파일명입니다.

# 행과 열 반전
transposed_data = data.transpose()

# 새로운 CSV 파일로 저장
transposed_data.to_csv(r"C:\Users\MSI\Desktop\회사\개발\MLTA\company_data\trace_data_excel\tra_abnormal_concat_10_2\abnormal_concat_10_2_T.csv",
                       index=False, header=False, encoding='utf-8')  # 'output.csv'는 저장할 CSV 파일명입니다.
