import streamlit as st
import pandas as pd
from IPython.display import IFrame
from PIL import Image
import matplotlib.pyplot as plt
import base64

header = st.container()
background = st.container()
dataset = st.container()
question = st.container()
Data_Development = st.container()
visualization = st.container()
inference = st.container()
copywright = st.container()

with header:
	st.title('WORLD CUP Analysis')
	st.write('A concise analysis to provide general insights about the world cup in 2022 in Quatar. The data analyzed gave an overall insight about the very competitive and most talked about competition in the world. In here, the overall performance for teams, individual players and set pieces and other metrics of the game.')

	with background:
		st.header("ROAD TO WORLD CUP")
		st.write("The 2022 FIFA World Cup was an international football tournament contested by the men's national teams of FIFA's member associations and 22nd edition of the FIFA World Cup. It took place in Qatar from 20 November to 18 December 2022, making it the first World Cup held in the Arab world and Muslim world, and the second held entirely in Asia after the 2002 tournament in South Korea and Japan. This tournament was the last with 32 participating teams, with the number of teams being increased to 48 for the 2026 edition. To avoid the extremes of Qatar's hot climate,the event was held during November and December.It was held over a reduced time frame of 29 days with 64 matches played in eight venues across five cities. Qatar entered the event—their first World Cup—automatically as the host's national team, alongside 31 teams determined by the qualification process.")

	with dataset:
		st.header("Data gathered from the Kaggle.")
		st.write('Here, the dataset contains about 48 countries in europe with their recorded cases, recovery rates, deaths. This data was collected over the period of time while the pandemic ravaged in 2020.')

		cup_data = pd.read_csv('./image/fifa.csv')
		st.write(cup_data.head())

	with question:
		st.header('Analysis Background')
		st.write('In this section, I provided more insights on some important questions that could arise during and after the pandemic. This insights will be a guide to our analysis and visualization as a whole.')


		st.markdown('* **first:** How each country faired in the competition: the goals, assists, players performances, the walk to victory.')
		st.markdown('* **second:** The oustanding players: the highest goal scorer(s), goalkeeper of the tournament and so on.')


	with Data_Development:
		st.header('Data Development')
		st.write("I downloaded the dataset from kaggle and thereafter, I used excel for the data cleaning process and to get the general overview of our dataset: removed unwanted columns, then imported our data into microsoft powerbi for visualization and to answer our questions")



	with visualization:
		st.header('Time to visualize our data!')
		st.write('#CovidAnalysis, #DataAnalysis, #Analysis, #Data, #DataVisualization, #PowerBi')

		sel_col, disp_col = st.columns(2)

		#Dashboard = IFrame(src" ", width = 1000, height = 600)
		#display(Dashboard)

		img = Image.open("./image/5.jpg")
		st.image(img)


	with inference:
		st.header("Insights")
		st.write("Argentina were crowned the champions after winning the final against the title holder France 4–2 on penalties following a 3–3 draw after extra time. It was Argentina's third title and their first since 1986, as well being the first nation from outside of Europe to win the tournament since 2002. French player Kylian Mbappé became the first player to score a hat-trick in a World Cup final since Geoff Hurst in the 1966 final and won the Golden Boot as he scored the most goals (eight) during the tournament. Argentine captain Lionel Messi was voted the tournament's best player, winning the Golden Ball. Teammates Emiliano Martínez and Enzo Fernández won the Golden Glove, awarded to the tournament's best goalkeeper, and the Young Player Award, awarded to the tournament's best young player, respectively. With 172 goals, the tournament set a new record for the highest number of goals scored with the 32-team format, with every participating team scoring at least one goal.")

		url = 'To view the interactive live dashboard on powerbi service, click  [Dashboard](https://app.powerbi.com/view?r=eyJrIjoiYTY5YmIzNzYtZWJmOS00YWZkLTk3NTUtMmZmOWVhYmUzZTgyIiwidCI6IjhlOTVjNGQxLWRiZmQtNGFmNS1iODA2LTIwMGJkZDY2ZDJjZSJ9)'
		st.markdown(url,unsafe_allow_html=True)

		urlp = 'To view my portfolio and contact me, please click  [Portfolio](https://letters-of-michael.github.io/Oluwaseyi-Michael.github.io/)'
		st.markdown(urlp,unsafe_allow_html=True)	

	with copywright:
		st.text('By Oluwaseyi Michael')




