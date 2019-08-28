import sqlalchemy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

conn = sqlalchemy.create_engine(
    'mysql+pymysql://root:Khakim@17@localhost:3306/world'
)

df = pd.read_sql_query("select * from country where region = 'Southeast Asia' order by name", conn)


#1. Populasi Negara ASEAN ====================================================
# plt.style.use('seaborn')
# plt.bar(list(df['Name']), list(df['Population']), color=['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'grey', 'gold', 'cyan', 'blue'])
# plt.xticks(rotation=60)
# plt.title('Populasi Negara ASEAN', fontdict={'fontsize':'22'})
# plt.xlabel('Negara')
# plt.ylabel('Populasi(x100jt jiwa)')
# xlocs = plt.xticks()
# plt.subplots_adjust(bottom=0.16)

# for x, y in zip (xlocs[0],(list(df['Population']))):
#     plt.text(x - 0.30, y + 1000000, str(y))
# plt.show()



#2. Persentase Populasi ASEAN ===================================================
# wedges, texts, autotexts = plt.pie(list(df['Population']), labels=list(df['Name']), autopct='%1.1f%%')
# plt.title('Persentase Negara ASEAN', fontdict={'fontsize':'20'})
# for autotext in autotexts:
#     autotext.set_color('white')
# plt.show()


#3. Pendapatan Bruto Nasional ASEAN ==============================================
# plt.style.use('seaborn')
# plt.bar(list(df['Name']), list(df['GNP']), color=['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'grey', 'gold', 'cyan', 'blue'])
# plt.xticks(rotation=60)
# plt.title('Pendapatan Bruto Nasional ASEAN', fontdict={'fontsize':'22'})
# plt.xlabel('Negara')
# plt.ylabel('Gross National Product (US$)')
# xlocs = plt.xticks()
# plt.subplots_adjust(bottom=0.16)

# for x, y in zip (xlocs[0],(list(df['GNP']))):
#     plt.text(x - 0.25, y + 2000, str(y))
# plt.show()



#4. Persentase Luas Daratan ASEAN ==============================================
# wedges, texts, autotexts = plt.pie(list(df['SurfaceArea']), labels=list(df['Name']), autopct='%1.1f%%')
# plt.title('Persentase Luas Daratan ASEAN', fontdict={'fontsize':'22'})
# for autotext in autotexts:
#     autotext.set_color('white')
# plt.show()




#=================================================================================
