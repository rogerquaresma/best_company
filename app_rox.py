import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import altair as alt

keyword1 = 'Career Growth'
keyword2 = 'Work Environment'
keyword3 = 'Work-Life Balance'
keyword4 = 'Diversity & Inclusion'
keyword5 = 'Technology'
keyword6 = 'Compensation'
keyword7 = 'People-Centric Culture'
keyword8 = 'Team work'
keyword9 = 'Learning & Development'
keyword10 = 'Role scope'

st.sidebar.markdown("**Apps**")
st.sidebar.write("TechMatch")

'''
# Welcome to :blue[TechMatch]!

We assist you in finding your ideal company as a data scientist. 
'''
with st.expander("How does this work?"):
    st.write("Once you've provided the necessary information, our advanced algorithm will analyze your data and generate a list of companies that align with  your preferences. You'll receive valuable insights about each company's  work-life balance, career growth opportunities, and collaborative  environment, enabling you to make an informed decision about your future workplace as a data scientist.")

st.write("To begin the process, we kindly ask you to rate ten keywords to reflect your preferences.") 
st.write("These keywords will help our algorithm identify the best matching companies for you based on your specified criteria.") 

st.write("Please assign each a value from 0 to 10. The higher the value, the more important the keyword is to you.")

col1, col2 = st.columns(2)

with col1:

# Variable 1 Slider
  variable1 = st.slider(f'Set {keyword1}: 0-10', 0, 10, 0)
# Variable 2 Slider
  variable2 = st.slider(f'Set {keyword2}: 0-10', 0, 10, 0)
# Variable 3 Slider
  variable3 = st.slider(f'Set {keyword3}: 0-10', 0, 10, 0)
# Variable 4 Slider
  variable4 = st.slider(f'Set {keyword4}: 0-10', 0, 10, 0)
# Variable 5 Slider
  variable5 = st.slider(f'Set {keyword5}: 0-10', 0, 10, 0)

with col2:
  
# Variable 6 Slider
  variable6 = st.slider(f'Set {keyword6}: 0-10', 0, 10, 0)
# Variable 7 Slider
  variable7 = st.slider(f'Set {keyword7}: 0-10', 0, 10, 0)
# Variable 8 Slider
  variable8 = st.slider(f'Set {keyword8}: 0-10', 0, 10, 0)
# Variable 9 Slider
  variable9 = st.slider(f'Set {keyword9}: 0-10', 0, 10, 0)
# Variable 10 Slider
  variable10 = st.slider(f'Set {keyword10}: 0-10', 0, 10, 0)

# Google Cloud Run URL
#url = 'https://bestcompany-nrfshmhfmq-ew.a.run.app/predict'

url = 'https://bestcompany-nrfshmhfmq-ew.a.run.app/predict'

dict_input = {'variable1': int(variable1), 
              'variable2': int(variable2),
              'variable3': int(variable3),
              'variable4': int(variable4),
              'variable5': int(variable5),
              'variable6': int(variable6),
              'variable7': int(variable7),
              'variable8': int(variable8),
              'variable9': int(variable9),
              'variable10': int(variable10)}

response = requests.get(url, params=dict_input)

if response.status_code != 200:
    print('Error')
'''

## :trophy: RESULTS :trophy: 
'''
st.write('Your closest match:')
st.write(list(response.json()['sorted_company'])[-1])

# Company Dashboard
company = list(response.json()['sorted_company'])[-1]

company_name = f'{company}'

meta = [0.027,0.050,0.164,0.301,0.457]

apple = [0.039,0.020,0.122,0.291,0.528]

google = [0.005,0.014,0.043,0.271,0.667]

amazon = [0.063,0.048,0.104,0.348,0.437]

microsoft = [0.016,0.013,0.120,0.301,0.550]

total = [0.030, 0.029, 0.111, 0.302, 0.528]


variable_dict = {keyword1: variable1, keyword2: variable2, keyword3: variable3,
                 keyword4: variable4, keyword5: variable5, keyword6: variable6, 
                 keyword7: variable7, keyword8: variable8, keyword9: variable9,
                 keyword10: variable10}

sorted_variable_dict = sorted(variable_dict.items(), key=lambda x:x[1], reverse = True)

#st.write(sorted_variable_dict)

work_life_intro = f'{company_name} is know for good {keyword1}'

if company == 'Apple':
    st.write('Apple Inc. is an American multinational technology company headquartered in Cupertino, California. Apple is the world largest technology company by revenue, and the second-largest mobile phone manufacturer in the world.')

    with st.expander("Your compatibility analysis"):
        for i in range(1):
            if list(sorted_variable_dict)[i][0] == keyword1:
                X = f'{company_name} is exceptional when it comes to career growth, as they provide a wide variety of training programs, mentoring opportunities, and resources to help employees develop their professional skills and expand their knowledge. The company is deeply committed to recognizing and promoting talent, ensuring that individuals have clear paths for advancement and can successfully achieve their career goals.'
            if list(sorted_variable_dict)[i][0] == keyword2:
                X = f'{company_name} shines in creating a positive work environment that promotes employee well-being and satisfaction. They prioritize fostering a supportive atmosphere where individuals feel valued and motivated to thrive. By offering various perks, work-life balance initiatives, and opportunities for professional development, they ensure that employees can flourish in a fulfilling work environment.'
            if list(sorted_variable_dict)[i][0] == keyword3:
                X = f'{company_name} values work-life balance as a crucial aspect of their company culture. They understand the importance of maintaining a healthy equilibrium between work and personal life. By offering flexible work arrangements, wellness programs, and supportive policies, they empower employees to manage their professional responsibilities while tending to their personal well-being.'
            if list(sorted_variable_dict)[i][0] == keyword4:
                X = f'{company_name} demonstrates a strong commitment to diversity and inclusion within their organization. They actively promote an inclusive work environment that values and respects individuals from all backgrounds and identities. By fostering diversity, they create a space where employees feel empowered to contribute their unique perspectives and experiences, leading to innovation and growth.'
            if list(sorted_variable_dict)[i][0] == keyword5:
                X = f'{company_name} is at the forefront of utilizing technology to drive innovation and enhance productivity. They embrace the latest technological advancements to streamline processes and empower their employees with efficient tools and resources. By leveraging technology, they create a dynamic work environment that promotes collaboration, creativity, and efficiency.'
            if list(sorted_variable_dict)[i][0] == keyword6:
                X = f'{company_name} stands out when it comes to compensation. They offer a wide array of benefits and rewards to recognize and appreciate their employees efforts. With competitive salaries, bonuses based on performance, and attractive incentives, they make sure employees are fairly rewarded. Additionally, they prioritize recognizing talent and supporting career growth, giving individuals opportunities to advance and earn the compensation they deserve.'
            if list(sorted_variable_dict)[i][0] == keyword7:
                X = f'{company_name} distinguishes itself with its people-centric culture that places employees at the heart of the organization. They prioritize creating a supportive and inclusive work environment where individuals feel valued, respected, and empowered. Through their comprehensive compensation packages, professional development opportunities, and recognition programs, they demonstrate their commitment to nurturing a culture that values and invests in their people.'
            if list(sorted_variable_dict)[i][0] == keyword8:
                X = f'{company_name} places a strong emphasis on teamwork and collaboration within their organization. They foster a culture that values the power of collective effort and encourages employees to work together towards shared goals. By promoting effective communication, cross-functional projects, and a supportive team environment, they enable employees to maximize their potential and achieve success collectively.'
            if list(sorted_variable_dict)[i][0] == keyword9:
                X = f'{company_name} excels in providing exceptional learning and development opportunities for their employees. They understand the significance of continuous growth and offer a range of training programs, workshops, and resources to enhance professional skills. By prioritizing learning and development, they empower individuals to reach their full potential and succeed in their careers, complementing their competitive compensation structure.'
            if list(sorted_variable_dict)[i][0] == keyword10:
                X = f'{company_name} distinguishes itself through its attention to role scope, ensuring that employees have well-defined responsibilities and opportunities for growth. They prioritize providing clear job descriptions, outlining the expectations and parameters of each role within the organization. By offering clarity in role scope, employees can understand their contributions, excel in their positions, and receive the compensation that aligns with their responsibilities.'
        for i in range(1,2):
            if list(sorted_variable_dict)[i][0] == keyword1:
                Y = f'In addition to this {company_name} is exceptional when it comes to career growth, as they provide a wide variety of training programs, mentoring opportunities, and resources to help employees develop their professional skills and expand their knowledge. The company is deeply committed to recognizing and promoting talent, ensuring that individuals have clear paths for advancement and can successfully achieve their career goals.'
            if list(sorted_variable_dict)[i][0] == keyword2:
                Y = f'In addition to this {company_name} shines in creating a positive work environment that promotes employee well-being and satisfaction. They prioritize fostering a supportive atmosphere where individuals feel valued and motivated to thrive. By offering various perks, work-life balance initiatives, and opportunities for professional development, they ensure that employees can flourish in a fulfilling work environment.'
            if list(sorted_variable_dict)[i][0] == keyword3:
                Y = f'In addition to this {company_name} values work-life balance as a crucial aspect of their company culture. They understand the importance of maintaining a healthy equilibrium between work and personal life. By offering flexible work arrangements, wellness programs, and supportive policies, they empower employees to manage their professional responsibilities while tending to their personal well-being.'
            if list(sorted_variable_dict)[i][0] == keyword4:
                Y = f'In addition to this {company_name} demonstrates a strong commitment to diversity and inclusion within their organization. They actively promote an inclusive work environment that values and respects individuals from all backgrounds and identities. By fostering diversity, they create a space where employees feel empowered to contribute their unique perspectives and experiences, leading to innovation and growth.'
            if list(sorted_variable_dict)[i][0] == keyword5:
                Y = f'In addition to this {company_name} is at the forefront of utilizing technology to drive innovation and enhance productivity. They embrace the latest technological advancements to streamline processes and empower their employees with efficient tools and resources. By leveraging technology, they create a dynamic work environment that promotes collaboration, creativity, and efficiency.'
            if list(sorted_variable_dict)[i][0] == keyword6:
                Y = f'In addition to this {company_name} stands out when it comes to compensation. They offer a wide array of benefits and rewards to recognize and appreciate their employees efforts. With competitive salaries, bonuses based on performance, and attractive incentives, they make sure employees are fairly rewarded. Additionally, they prioritize recognizing talent and supporting career growth, giving individuals opportunities to advance and earn the compensation they deserve.'
            if list(sorted_variable_dict)[i][0] == keyword7:
                Y = f'In addition to this {company_name} distinguishes itself with its people-centric culture that places employees at the heart of the organization. They prioritize creating a supportive and inclusive work environment where individuals feel valued, respected, and empowered. Through their comprehensive compensation packages, professional development opportunities, and recognition programs, they demonstrate their commitment to nurturing a culture that values and invests in their people.'
            if list(sorted_variable_dict)[i][0] == keyword8:
                Y = f'In addition to this {company_name} places a strong emphasis on teamwork and collaboration within their organization. They foster a culture that values the power of collective effort and encourages employees to work together towards shared goals. By promoting effective communication, cross-functional projects, and a supportive team environment, they enable employees to maximize their potential and achieve success collectively.'
            if list(sorted_variable_dict)[i][0] == keyword9:
                Y = f'In addition to this {company_name} excels in providing exceptional learning and development opportunities for their employees. They understand the significance of continuous growth and offer a range of training programs, workshops, and resources to enhance professional skills. By prioritizing learning and development, they empower individuals to reach their full potential and succeed in their careers, complementing their competitive compensation structure.'
            if list(sorted_variable_dict)[i][0] == keyword10:
                Y = f'In addition to this, {company_name} distinguishes itself through its attention to role scope, ensuring that employees have well-defined responsibilities and opportunities for growth. They prioritize providing clear job descriptions, outlining the expectations and parameters of each role within the organization. By offering clarity in role scope, employees can understand their contributions, excel in their positions, and receive the compensation that aligns with their responsibilities.'
        st.write(X + Y)

    with st.expander("Word cloud: How former employees see Apple"):

        apple_cloud_data = 'place work, smart people, environment people, work life, company work, big company, work smart, lot perk, well manage, pay phone, team work, work environment, life balance, people work, company culture, work apple, salary benefit, work culture, worklife balance, get work, work lot, excite work, really enjoy, culture people, fast pace, benefit pay, environment work, interest project, talented people, perk benefit, growth opportunities, lot opportunities, experience work, learn lot, opportunities grow, nice place, work people, depend team, interest work, want work, work benefit, work big, nice work, love work, work products, products impact, impact world, health insurance'
    
        wordcloud_apple = WordCloud(width=800, height=400, background_color='white', contour_width=3, contour_color='steelblue', random_state=42).generate(apple_cloud_data)

        fig, ax = plt.subplots()
        ax.imshow(wordcloud_apple, interpolation='bilinear')
        ax.axis("off")
        fig.set_facecolor('white')
        fig.patch.set_alpha(0.7)
    
        st.pyplot(fig)

    with st.expander("How former Employees have rated Apple?"):
        ratings_data_apple = pd.DataFrame({
            "Ratings": ["5","4","3","2","1"],
            "RatingsbyAppleEmployees": [052.8,029.1,012.2,002.0,003.9]  
        })

        ratings_data_apple['Ratings'] = ratings_data_apple['Ratings'].astype(int)

        ratings_data_apple = ratings_data_apple.sort_values('Ratings', ascending=False)

        ratings_bar_chart_apple = alt.Chart(ratings_data_apple).mark_bar().encode(
            x='sum(RatingsbyAppleEmployees)',
            y=alt.Y('Ratings:N', sort='-x'), 
            color='Ratings:N'
        )

        st.altair_chart(ratings_bar_chart_apple, use_container_width=True)

    with st.expander("Reviews most people found helpful"):
        st.write("1. **Pros**: There is a certain recognition you receive when others hear you work for Apple with it being the high flyer in the industry. There is some flexibility in the hours as long as you get your work done.")
        st.write("**Cons**: Ivory tower management that tends to be in the way more than helping. They often make decisions that the people who do the work don't understand and hurts productivity. After cutting down benefits quite a bit during the lean years (mid 90's), has done nothing to bring any of them back now that we are making a killing.")
        st.write("2. **Pros**: Salary, Food and Free shuttle bus from MRT-station.")
        st.write("**Cons**: Too much micro-management Always monitored by management. Can barely go to toilet without getting message from boss about being inactive. Too high expectations from Management to hit KPI - they care more about quantity than quality. No team morale. Management don't even introduce you to your colleagues when you start. No communication with management except for when you do something *wrong* like taking too long to get your coffee.")
        st.write("3. **Pros**: At the beginning you can learn a lot and see how a big company works. Depending on teams, data scientists have a lot of freedom.") 
        st.write("**Cons**: Unstructured. Infra structure is not as great as some other big companies. Growth is slow which is natural for big companies.")
    
    with st.expander("Top Interview Questions Frequently Asked at Apple"):
        st.write("General Questions:")
        st.write("- Internship Experiences")
        st.write("- How to Approach Problems")
        st.write("- Tell Current Responsibilities")
        st.write("- Projects on Resume")
        st.write(" ")
        st.write("Technical Questions:")
        st.write("- SQL Basic Questions")
        st.write("- Metrics Used to Evaluate a Model")
        st.write("- Conduct AB Testing")
        st.write("- KNN Nearest Neighbor")

    with st.expander("Insights into the Interview Process and Job Offer Rates"):
        st.write("- 34% of candidates describe the interview process as difficult for Apple")
        st.write("- 56% of candidates describe the interview process as average for Apple")
        st.write("- 24% of candidates receive job offers for Apple")
    
if company == 'Meta':
    st.write('Meta Platforms, Inc., formerly named Facebook, Inc., and TheFacebook, Inc., is an American multinational technology conglomerate based in Menlo Park, California. The company owns Facebook, Instagram, and WhatsApp, among other products and services.')

    with st.expander("Your compatibility analysis"):
        for i in range(1):
            if list(sorted_variable_dict)[i][0] == keyword1:
                X = f'{company_name} is exceptional when it comes to career growth, as they provide a wide variety of training programs, mentoring opportunities, and resources to help employees develop their professional skills and expand their knowledge. The company is deeply committed to recognizing and promoting talent, ensuring that individuals have clear paths for advancement and can successfully achieve their career goals.'
            if list(sorted_variable_dict)[i][0] == keyword2:
                X = f'{company_name} shines in creating a positive work environment that promotes employee well-being and satisfaction. They prioritize fostering a supportive atmosphere where individuals feel valued and motivated to thrive. By offering various perks, work-life balance initiatives, and opportunities for professional development, they ensure that employees can flourish in a fulfilling work environment.'
            if list(sorted_variable_dict)[i][0] == keyword3:
                X = f'{company_name} values work-life balance as a crucial aspect of their company culture. They understand the importance of maintaining a healthy equilibrium between work and personal life. By offering flexible work arrangements, wellness programs, and supportive policies, they empower employees to manage their professional responsibilities while tending to their personal well-being.'
            if list(sorted_variable_dict)[i][0] == keyword4:
                X = f'{company_name} demonstrates a strong commitment to diversity and inclusion within their organization. They actively promote an inclusive work environment that values and respects individuals from all backgrounds and identities. By fostering diversity, they create a space where employees feel empowered to contribute their unique perspectives and experiences, leading to innovation and growth.'
            if list(sorted_variable_dict)[i][0] == keyword5:
                X = f'{company_name} is at the forefront of utilizing technology to drive innovation and enhance productivity. They embrace the latest technological advancements to streamline processes and empower their employees with efficient tools and resources. By leveraging technology, they create a dynamic work environment that promotes collaboration, creativity, and efficiency.'
            if list(sorted_variable_dict)[i][0] == keyword6:
                X = f'{company_name} stands out when it comes to compensation. They offer a wide array of benefits and rewards to recognize and appreciate their employees efforts. With competitive salaries, bonuses based on performance, and attractive incentives, they make sure employees are fairly rewarded. Additionally, they prioritize recognizing talent and supporting career growth, giving individuals opportunities to advance and earn the compensation they deserve.'
            if list(sorted_variable_dict)[i][0] == keyword7:
                X = f'{company_name} distinguishes itself with its people-centric culture that places employees at the heart of the organization. They prioritize creating a supportive and inclusive work environment where individuals feel valued, respected, and empowered. Through their comprehensive compensation packages, professional development opportunities, and recognition programs, they demonstrate their commitment to nurturing a culture that values and invests in their people.'
            if list(sorted_variable_dict)[i][0] == keyword8:
                X = f'{company_name} places a strong emphasis on teamwork and collaboration within their organization. They foster a culture that values the power of collective effort and encourages employees to work together towards shared goals. By promoting effective communication, cross-functional projects, and a supportive team environment, they enable employees to maximize their potential and achieve success collectively.'
            if list(sorted_variable_dict)[i][0] == keyword9:
                X = f'{company_name} excels in providing exceptional learning and development opportunities for their employees. They understand the significance of continuous growth and offer a range of training programs, workshops, and resources to enhance professional skills. By prioritizing learning and development, they empower individuals to reach their full potential and succeed in their careers, complementing their competitive compensation structure.'
            if list(sorted_variable_dict)[i][0] == keyword10:
                X = f'{company_name} distinguishes itself through its attention to role scope, ensuring that employees have well-defined responsibilities and opportunities for growth. They prioritize providing clear job descriptions, outlining the expectations and parameters of each role within the organization. By offering clarity in role scope, employees can understand their contributions, excel in their positions, and receive the compensation that aligns with their responsibilities.'
          
        for i in range(1,2):
            if list(sorted_variable_dict)[i][0] == keyword1:
                Y = f'In addition to this {company_name}  is exceptional when it comes to career growth, as they provide a wide variety of training programs, mentoring opportunities, and resources to help employees develop their professional skills and expand their knowledge. The company is deeply committed to recognizing and promoting talent, ensuring that individuals have clear paths for advancement and can successfully achieve their career goals.'
            if list(sorted_variable_dict)[i][0] == keyword2:
                Y = f'In addition to this {company_name} shines in creating a positive work environment that promotes employee well-being and satisfaction. They prioritize fostering a supportive atmosphere where individuals feel valued and motivated to thrive. By offering various perks, work-life balance initiatives, and opportunities for professional development, they ensure that employees can flourish in a fulfilling work environment.'
            if list(sorted_variable_dict)[i][0] == keyword3:
                Y = f'In addition to this {company_name} values work-life balance as a crucial aspect of their company culture. They understand the importance of maintaining a healthy equilibrium between work and personal life. By offering flexible work arrangements, wellness programs, and supportive policies, they empower employees to manage their professional responsibilities while tending to their personal well-being.'
            if list(sorted_variable_dict)[i][0] == keyword4:
                Y = f'In addition to this {company_name} demonstrates a strong commitment to diversity and inclusion within their organization. They actively promote an inclusive work environment that values and respects individuals from all backgrounds and identities. By fostering diversity, they create a space where employees feel empowered to contribute their unique perspectives and experiences, leading to innovation and growth.'
            if list(sorted_variable_dict)[i][0] == keyword5:
                Y = f'In addition to this {company_name} is at the forefront of utilizing technology to drive innovation and enhance productivity. They embrace the latest technological advancements to streamline processes and empower their employees with efficient tools and resources. By leveraging technology, they create a dynamic work environment that promotes collaboration, creativity, and efficiency.'
            if list(sorted_variable_dict)[i][0] == keyword6:
                Y = f'In addition to this {company_name} stands out when it comes to compensation. They offer a wide array of benefits and rewards to recognize and appreciate their employees efforts. With competitive salaries, bonuses based on performance, and attractive incentives, they make sure employees are fairly rewarded. Additionally, they prioritize recognizing talent and supporting career growth, giving individuals opportunities to advance and earn the compensation they deserve.'
            if list(sorted_variable_dict)[i][0] == keyword7:
                Y = f'In addition to this {company_name} distinguishes itself with its people-centric culture that places employees at the heart of the organization. They prioritize creating a supportive and inclusive work environment where individuals feel valued, respected, and empowered. Through their comprehensive compensation packages, professional development opportunities, and recognition programs, they demonstrate their commitment to nurturing a culture that values and invests in their people.'
            if list(sorted_variable_dict)[i][0] == keyword8:
                Y = f'In addition to this {company_name} places a strong emphasis on teamwork and collaboration within their organization. They foster a culture that values the power of collective effort and encourages employees to work together towards shared goals. By promoting effective communication, cross-functional projects, and a supportive team environment, they enable employees to maximize their potential and achieve success collectively.'
            if list(sorted_variable_dict)[i][0] == keyword9:
                Y = f'In addition to this {company_name} excels in providing exceptional learning and development opportunities for their employees. They understand the significance of continuous growth and offer a range of training programs, workshops, and resources to enhance professional skills. By prioritizing learning and development, they empower individuals to reach their full potential and succeed in their careers, complementing their competitive compensation structure.'
            if list(sorted_variable_dict)[i][0] == keyword10:
                Y = f'In addition to this {company_name} distinguishes itself through its attention to role scope, ensuring that employees have well-defined responsibilities and opportunities for growth. They prioritize providing clear job descriptions, outlining the expectations and parameters of each role within the organization. By offering clarity in role scope, employees can understand their contributions, excel in their positions, and receive the compensation that aligns with their responsibilities.'
        st.write(X + Y)

    with st.expander("Word cloud: How former employees see Meta"):
    
        meta_cloud_data = 'smart people, interest problems, work environment, learn lot, worklife balance, pay benefit, move fast, place work, people work, career growth, take care, work life, open culture, company culture, nice people, people nice, fast pace, people benefit, really smart, talented coworkers, pay smart, challenge work, smart colleagues, nice smart, challenge problems, culture people, life balance, free food, wellness benefit, benefit nice, love work, work smart, benefit pay, every day, benefit smart, learn new'

        wordcloud_meta = WordCloud(width=800, height=400, background_color='white', contour_width=3, contour_color='steelblue', random_state=42).generate(meta_cloud_data)
    
        fig, ax = plt.subplots()
        ax.imshow(wordcloud_meta, interpolation='bilinear')
        ax.axis("off")
        fig.set_facecolor('white')
        fig.patch.set_alpha(0.7)
    
        st.pyplot(fig)

    with st.expander("How former Employees have rated Meta?"):
  
        ratings_data_meta = pd.DataFrame({
            "Ratings": ["5","4","3","2","1"],
            "RatingsbyMetaEmployees": [045.7,030.1,016.4,005.0,002.7]  
          })

        ratings_data_meta['Ratings'] = ratings_data_meta['Ratings'].astype(int)
        ratings_data_meta = ratings_data_meta.sort_values('Ratings', ascending=False)

        ratings_bar_chart_meta = alt.Chart(ratings_data_meta).mark_bar().encode(
            x='sum(RatingsbyMetaEmployees)',
            y=alt.Y('Ratings:N', sort='-x'), 
            color='Ratings:N'
        )

        st.altair_chart(ratings_bar_chart_meta, use_container_width=True)

    with st.expander("Reviews most people found helpful"):
        st.write("1. **Pros**: Good perks and comp, coworkers are nice and fun.") 
        st.write("**Cons**: Very competitive environment. No possible to succeed if you don’t work 60+ hours. Focus on short term impact due to performance cycle every 6 months. No clarity on expectations of roles. Mix signals from leadership about culture.")
        st.write("2. **Pros**: Great opportunity to work with the smartest people from the world - most products have billions of users so your work have a big scope - beautiful campus, good snacks, foods, and benefits.")
        st.write("**Cons**: If you are a data scientist, you need to really care about two things: - Impact. Unlike SWE, who can prove their impacts by finishing pre-planned coding projects and rolling out pre-planned features, data scientist does not automatically get credit if you only finish beautiful analyses. You have to suggest eng team to apply your suggestion from analysis, and prove how much of the product growth are from your analysis. So sometimes your impact can be subjective. - Skillset. You may be asked to do a lot of ad-hoc analyses from eng team, which I am sure are very important and can guide engineers whether to implement certain features, but that will prevent you from doing some deep dive analyses and learning some new techniques in data analysis. Maybe after a year or two, you will find that you did not build any statistical models or haven't touched any machine learning. But that's the skillset what other companies will ask for when you apply new job. Who cares you did how many ad-hoc analyses or AB test or wrote how many data pipelines. It's the fancy machine learning model that will earn you respect. Also, total pay is lower than SWE for the same level.")
        st.write("3. **Pros**: Food - Health care benefits - Fringe benefits - Nice campus - Corporate shuttles - State of the art tech stack - Extremely smart coworkers - Visionary and bold top management.") 
        st.write("**Cons**: Work/life balance can get hurt as a lot of folks at the office are single and do not understand the needs of having a family. The company is getting bigger. This means more room for backroom politics and aligning people without ruffling people's feathers. Very talented individual contributors (and/or good at politics) are being promoted. As a result, instead of having well rounded managers, you end up having either extremely career driven or super awkward managers. Some of those middle managers are very green, making it even more painful. Some women feel like they have to be extra tough at work because of the Leanin coolaid, making them very hard to work with.")

    with st.expander("Top Interview Questions Frequently Asked at Meta"):
        st.write("General Questions:")
        st.write("- Tell Technical Background")
        st.write("- How Would You Measure Success of a Product")
        st.write("- Tell About a Time When...")
        st.write("- Previous Experience")
      
        st.write("Technical Questions:")
        st.write("- SQL")
        st.write("- Questions on Case Studies, e.g. Determine Spam Friend Requests")
        st.write("- Questions on AB Testing")
        st.write("- Machine Learning")

    with st.expander("Insights into the Interview Process and Job Offer Rates"):
        st.write("- 26% of candidates describe the interview process as difficult for Meta")
        st.write("- 70% of candidates describe the interview process as average for Meta")
        st.write("- 21% of candidates receive job offers for Meta")

if company == 'Microsoft':
    st.write('Microsoft Corporation is an American multinational technology corporation headquartered in Redmond, Washington. Microsofts best-known software products are the Windows line of operating systems, the Microsoft Office suite, and the Internet Explorer and Edge web browsers.')

    with st.expander("Your compatibility analysis"):
        for i in range(1):
            if list(sorted_variable_dict)[i][0] == keyword1:
                X = f'{company_name} is exceptional when it comes to career growth, as they provide a wide variety of training programs, mentoring opportunities, and resources to help employees develop their professional skills and expand their knowledge. The company is deeply committed to recognizing and promoting talent, ensuring that individuals have clear paths for advancement and can successfully achieve their career goals.'
            if list(sorted_variable_dict)[i][0] == keyword2:
                X = f'{company_name} shines in creating a positive work environment that promotes employee well-being and satisfaction. They prioritize fostering a supportive atmosphere where individuals feel valued and motivated to thrive. By offering various perks, work-life balance initiatives, and opportunities for professional development, they ensure that employees can flourish in a fulfilling work environment.'
            if list(sorted_variable_dict)[i][0] == keyword3:
                X = f'{company_name} values work-life balance as a crucial aspect of their company culture. They understand the importance of maintaining a healthy equilibrium between work and personal life. By offering flexible work arrangements, wellness programs, and supportive policies, they empower employees to manage their professional responsibilities while tending to their personal well-being.'
            if list(sorted_variable_dict)[i][0] == keyword4:
                X = f'{company_name} demonstrates a strong commitment to diversity and inclusion within their organization. They actively promote an inclusive work environment that values and respects individuals from all backgrounds and identities. By fostering diversity, they create a space where employees feel empowered to contribute their unique perspectives and experiences, leading to innovation and growth.'
            if list(sorted_variable_dict)[i][0] == keyword5:
                X = f'{company_name} is at the forefront of utilizing technology to drive innovation and enhance productivity. They embrace the latest technological advancements to streamline processes and empower their employees with efficient tools and resources. By leveraging technology, they create a dynamic work environment that promotes collaboration, creativity, and efficiency.'
            if list(sorted_variable_dict)[i][0] == keyword6:
                X = f'{company_name} stands out when it comes to compensation. They offer a wide array of benefits and rewards to recognize and appreciate their employees efforts. With competitive salaries, bonuses based on performance, and attractive incentives, they make sure employees are fairly rewarded. Additionally, they prioritize recognizing talent and supporting career growth, giving individuals opportunities to advance and earn the compensation they deserve.'
            if list(sorted_variable_dict)[i][0] == keyword7:
                X = f'{company_name} distinguishes itself with its people-centric culture that places employees at the heart of the organization. They prioritize creating a supportive and inclusive work environment where individuals feel valued, respected, and empowered. Through their comprehensive compensation packages, professional development opportunities, and recognition programs, they demonstrate their commitment to nurturing a culture that values and invests in their people.'
            if list(sorted_variable_dict)[i][0] == keyword8:
                X = f'{company_name} places a strong emphasis on teamwork and collaboration within their organization. They foster a culture that values the power of collective effort and encourages employees to work together towards shared goals. By promoting effective communication, cross-functional projects, and a supportive team environment, they enable employees to maximize their potential and achieve success collectively.'
            if list(sorted_variable_dict)[i][0] == keyword9:
                X = f'{company_name} excels in providing exceptional learning and development opportunities for their employees. They understand the significance of continuous growth and offer a range of training programs, workshops, and resources to enhance professional skills. By prioritizing learning and development, they empower individuals to reach their full potential and succeed in their careers, complementing their competitive compensation structure.'
            if list(sorted_variable_dict)[i][0] == keyword10:
                X = f'{company_name} distinguishes itself through its attention to role scope, ensuring that employees have well-defined responsibilities and opportunities for growth. They prioritize providing clear job descriptions, outlining the expectations and parameters of each role within the organization. By offering clarity in role scope, employees can understand their contributions, excel in their positions, and receive the compensation that aligns with their responsibilities.'
        for i in range(1,2):
            if list(sorted_variable_dict)[i][0] == keyword1:
                Y = f'In addition to this {company_name} is exceptional when it comes to career growth, as they provide a wide variety of training programs, mentoring opportunities, and resources to help employees develop their professional skills and expand their knowledge. The company is deeply committed to recognizing and promoting talent, ensuring that individuals have clear paths for advancement and can successfully achieve their career goals.'
            if list(sorted_variable_dict)[i][0] == keyword2:
                Y = f'In addition to this {company_name} shines in creating a positive work environment that promotes employee well-being and satisfaction. They prioritize fostering a supportive atmosphere where individuals feel valued and motivated to thrive. By offering various perks, work-life balance initiatives, and opportunities for professional development, they ensure that employees can flourish in a fulfilling work environment.'
            if list(sorted_variable_dict)[i][0] == keyword3:
                Y = f'In addition to this {company_name} values work-life balance as a crucial aspect of their company culture. They understand the importance of maintaining a healthy equilibrium between work and personal life. By offering flexible work arrangements, wellness programs, and supportive policies, they empower employees to manage their professional responsibilities while tending to their personal well-being.'
            if list(sorted_variable_dict)[i][0] == keyword4:
                Y = f'In addition to this {company_name} demonstrates a strong commitment to diversity and inclusion within their organization. They actively promote an inclusive work environment that values and respects individuals from all backgrounds and identities. By fostering diversity, they create a space where employees feel empowered to contribute their unique perspectives and experiences, leading to innovation and growth.'
            if list(sorted_variable_dict)[i][0] == keyword5:
                Y = f'In addition to this {company_name} is at the forefront of utilizing technology to drive innovation and enhance productivity. They embrace the latest technological advancements to streamline processes and empower their employees with efficient tools and resources. By leveraging technology, they create a dynamic work environment that promotes collaboration, creativity, and efficiency.'
            if list(sorted_variable_dict)[i][0] == keyword6:
                Y = f'In addition to this {company_name} stands out when it comes to compensation. They offer a wide array of benefits and rewards to recognize and appreciate their employees efforts. With competitive salaries, bonuses based on performance, and attractive incentives, they make sure employees are fairly rewarded. Additionally, they prioritize recognizing talent and supporting career growth, giving individuals opportunities to advance and earn the compensation they deserve.'
            if list(sorted_variable_dict)[i][0] == keyword7:
                Y = f'In addition to this {company_name} distinguishes itself with its people-centric culture that places employees at the heart of the organization. They prioritize creating a supportive and inclusive work environment where individuals feel valued, respected, and empowered. Through their comprehensive compensation packages, professional development opportunities, and recognition programs, they demonstrate their commitment to nurturing a culture that values and invests in their people.'
            if list(sorted_variable_dict)[i][0] == keyword8:
                Y = f'In addition to this {company_name} places a strong emphasis on teamwork and collaboration within their organization. They foster a culture that values the power of collective effort and encourages employees to work together towards shared goals. By promoting effective communication, cross-functional projects, and a supportive team environment, they enable employees to maximize their potential and achieve success collectively.'
            if list(sorted_variable_dict)[i][0] == keyword9:
                Y = f'In addition to this {company_name} excels in providing exceptional learning and development opportunities for their employees. They understand the significance of continuous growth and offer a range of training programs, workshops, and resources to enhance professional skills. By prioritizing learning and development, they empower individuals to reach their full potential and succeed in their careers, complementing their competitive compensation structure.'
            if list(sorted_variable_dict)[i][0] == keyword10:
                Y = f'In addition to this {company_name} distinguishes itself through its attention to role scope, ensuring that employees have well-defined responsibilities and opportunities for growth. They prioritize providing clear job descriptions, outlining the expectations and parameters of each role within the organization. By offering clarity in role scope, employees can understand their contributions, excel in their positions, and receive the compensation that aligns with their responsibilities.'
        st.write(X + Y)

    with st.expander("Word cloud: How former employees see Microsoft"):

        microsoft_cloud_data = 'work life, life balance, worklife balance, work culture, work environment, smart people, company culture, people work, place work, talented people, diversity inclusion, company work, interest work, nice work, flexible work, growth mindset, opportunity work, work project, culture work, team members, benefit work, interest problems, company lot, work atmosphere, balance work, work hours, people around, work talented, culture people, lot opportunities, balance lot, stable company, balance smart'

        wordcloud_microsoft = WordCloud(width=800, height=400, background_color='white', contour_width=3, contour_color='steelblue', random_state=42).generate(microsoft_cloud_data)
    
        fig, ax = plt.subplots()
        ax.imshow(wordcloud_microsoft, interpolation='bilinear')
        ax.axis("off")
        fig.set_facecolor('white')
        fig.patch.set_alpha(0.7)
    
        st.pyplot(fig)

    with st.expander("How former Employees have rated Microsoft?"):
  
        ratings_data_microsoft = pd.DataFrame({
            "Ratings": ["5","4","3","2","1"],
            "RatingsbyMicrosoftEmployees": [055.0,030.1,012.0,001.3,001.6]  
        })

        ratings_data_microsoft['Ratings'] = ratings_data_microsoft['Ratings'].astype(int)
        ratings_data_microsoft = ratings_data_microsoft.sort_values('Ratings', ascending=False)

        ratings_bar_chart_microsoft = alt.Chart(ratings_data_microsoft).mark_bar().encode(
            x='sum(RatingsbyMicrosoftEmployees)',
            y=alt.Y('Ratings:N', sort='-x'), 
            color='Ratings:N'
        )

        st.altair_chart(ratings_bar_chart_microsoft, use_container_width=True)

    with st.expander("Reviews most people found helpful"):
        st.write("1. **Pros**: Brand; serves as a launchpad + Scope of work is broad + Lots of learnings- both technical and management skills.") 
        st.write("**Cons**: There are islands of talents, some are good but mostly average Must 'kiss-ass' to get visibility, promotion, and bonus Very slow pace of work and career growth.")
        st.write("2. **Pros**: Decent pay, good benefits, great co-workers.")
        st.write("**Cons**: Satya does regular layoffs, while talking a big game about caring for employees. This fiscal year, Microsoft acquired companies worth a 100B, invested 10B+ in OpenAI, but laid off 5% of the workforce to save $1-2B over the next few years.")
        st.write("3. **Pros**: Working with truly big datasets and ability to use advanced techniques Cutting edge database/stats tools Relaxed environment with no deadlines and pressure.") 
        st.write("**Cons**: slow-paced, no clear objectives and not goal-oriented - may feel more like a uni environment than a real work multiple teams doing the same tasks - which leads to internal competition and politics rather than focusing on external clients too many layers of management most project don't lead to any noticeable impact and don't align with company strategy - the emphasis is on *PR* aspect to make the manager/team look good (you spend far more time on presenting/ improving the power point slides than actual analysis or work).")
    
    with st.expander("Top Interview Questions Frequently Asked at Microsoft"):
        st.write("General Questions:")
        st.write("- Discuss Experience in Data Science")
        st.write("- Tell About a Time When...")
        st.write("- Difficulties Faced")
        st.write("- Prior Experience")
      
        st.write("Technical Questions:")
        st.write("- Underfitting and Overfitting")
        st.write("- Recommendation System Design")
        st.write("- Probability Statistics")
        st.write("- Machine Learning")

    with st.expander("Insights into the Interview Process and Job Offer Rates"):
        st.write("- 26% of candidates describe the interview process as difficult for Microsoft")
        st.write("- 57% of candidates describe the interview process as average for Microsoft")
        st.write("- 35% of candidates receive job offers for Microsoft")
    
if company == 'Amazon':
    st.write('Amazon.com, Inc. is an American multinational technology company focusing on e-commerce, cloud computing, online advertising, digital streaming, and artificial intelligence.')

    with st.expander("Your compatibility analysis"):
        for i in range(1):
            if list(sorted_variable_dict)[i][0] == keyword1:
                X = f'{company_name}  is exceptional when it comes to career growth, as they provide a wide variety of training programs, mentoring opportunities, and resources to help employees develop their professional skills and expand their knowledge. The company is deeply committed to recognizing and promoting talent, ensuring that individuals have clear paths for advancement and can successfully achieve their career goals.'
            if list(sorted_variable_dict)[i][0] == keyword2:
                X = f'{company_name} shines in creating a positive work environment that promotes employee well-being and satisfaction. They prioritize fostering a supportive atmosphere where individuals feel valued and motivated to thrive. By offering various perks, work-life balance initiatives, and opportunities for professional development, they ensure that employees can flourish in a fulfilling work environment.'
            if list(sorted_variable_dict)[i][0] == keyword3:
                X = f'{company_name} values work-life balance as a crucial aspect of their company culture. They understand the importance of maintaining a healthy equilibrium between work and personal life. By offering flexible work arrangements, wellness programs, and supportive policies, they empower employees to manage their professional responsibilities while tending to their personal well-being.'
            if list(sorted_variable_dict)[i][0] == keyword4:
                X = f'{company_name} demonstrates a strong commitment to diversity and inclusion within their organization. They actively promote an inclusive work environment that values and respects individuals from all backgrounds and identities. By fostering diversity, they create a space where employees feel empowered to contribute their unique perspectives and experiences, leading to innovation and growth.'
            if list(sorted_variable_dict)[i][0] == keyword5:
                X = f'{company_name} is at the forefront of utilizing technology to drive innovation and enhance productivity. They embrace the latest technological advancements to streamline processes and empower their employees with efficient tools and resources. By leveraging technology, they create a dynamic work environment that promotes collaboration, creativity, and efficiency.'
            if list(sorted_variable_dict)[i][0] == keyword6:
                X = f'{company_name} stands out when it comes to compensation. They offer a wide array of benefits and rewards to recognize and appreciate their employees efforts. With competitive salaries, bonuses based on performance, and attractive incentives, they make sure employees are fairly rewarded. Additionally, they prioritize recognizing talent and supporting career growth, giving individuals opportunities to advance and earn the compensation they deserve.'
            if list(sorted_variable_dict)[i][0] == keyword7:
                X = f'{company_name} distinguishes itself with its people-centric culture that places employees at the heart of the organization. They prioritize creating a supportive and inclusive work environment where individuals feel valued, respected, and empowered. Through their comprehensive compensation packages, professional development opportunities, and recognition programs, they demonstrate their commitment to nurturing a culture that values and invests in their people.'
            if list(sorted_variable_dict)[i][0] == keyword8:
                X = f'{company_name} places a strong emphasis on teamwork and collaboration within their organization. They foster a culture that values the power of collective effort and encourages employees to work together towards shared goals. By promoting effective communication, cross-functional projects, and a supportive team environment, they enable employees to maximize their potential and achieve success collectively.'
            if list(sorted_variable_dict)[i][0] == keyword9:
                X = f'{company_name} excels in providing exceptional learning and development opportunities for their employees. They understand the significance of continuous growth and offer a range of training programs, workshops, and resources to enhance professional skills. By prioritizing learning and development, they empower individuals to reach their full potential and succeed in their careers, complementing their competitive compensation structure.'
            if list(sorted_variable_dict)[i][0] == keyword10:
                X = f'{company_name} distinguishes itself through its attention to role scope, ensuring that employees have well-defined responsibilities and opportunities for growth. They prioritize providing clear job descriptions, outlining the expectations and parameters of each role within the organization. By offering clarity in role scope, employees can understand their contributions, excel in their positions, and receive the compensation that aligns with their responsibilities.'
        for i in range(1,2):
            if list(sorted_variable_dict)[i][0] == keyword1:
                Y = f'In addition to this {company_name} is exceptional when it comes to career growth, as they provide a wide variety of training programs, mentoring opportunities, and resources to help employees develop their professional skills and expand their knowledge. The company is deeply committed to recognizing and promoting talent, ensuring that individuals have clear paths for advancement and can successfully achieve their career goals.'
            if list(sorted_variable_dict)[i][0] == keyword2:
                Y = f'In addition to this {company_name} shines in creating a positive work environment that promotes employee well-being and satisfaction. They prioritize fostering a supportive atmosphere where individuals feel valued and motivated to thrive. By offering various perks, work-life balance initiatives, and opportunities for professional development, they ensure that employees can flourish in a fulfilling work environment.'
            if list(sorted_variable_dict)[i][0] == keyword3:
                Y = f'In addition to this {company_name} values work-life balance as a crucial aspect of their company culture. They understand the importance of maintaining a healthy equilibrium between work and personal life. By offering flexible work arrangements, wellness programs, and supportive policies, they empower employees to manage their professional responsibilities while tending to their personal well-being.'
            if list(sorted_variable_dict)[i][0] == keyword4:
                Y = f'In addition to this {company_name} demonstrates a strong commitment to diversity and inclusion within their organization. They actively promote an inclusive work environment that values and respects individuals from all backgrounds and identities. By fostering diversity, they create a space where employees feel empowered to contribute their unique perspectives and experiences, leading to innovation and growth.'
            if list(sorted_variable_dict)[i][0] == keyword5:
                Y = f'In addition to this {company_name} is at the forefront of utilizing technology to drive innovation and enhance productivity. They embrace the latest technological advancements to streamline processes and empower their employees with efficient tools and resources. By leveraging technology, they create a dynamic work environment that promotes collaboration, creativity, and efficiency.'
            if list(sorted_variable_dict)[i][0] == keyword6:
                Y = f'In addition to this {company_name} stands out when it comes to compensation. They offer a wide array of benefits and rewards to recognize and appreciate their employees efforts. With competitive salaries, bonuses based on performance, and attractive incentives, they make sure employees are fairly rewarded. Additionally, they prioritize recognizing talent and supporting career growth, giving individuals opportunities to advance and earn the compensation they deserve.'
            if list(sorted_variable_dict)[i][0] == keyword7:
                Y = f'In addition to this {company_name} distinguishes itself with its people-centric culture that places employees at the heart of the organization. They prioritize creating a supportive and inclusive work environment where individuals feel valued, respected, and empowered. Through their comprehensive compensation packages, professional development opportunities, and recognition programs, they demonstrate their commitment to nurturing a culture that values and invests in their people.is best know for having a great management...'
            if list(sorted_variable_dict)[i][0] == keyword8:
                Y = f'In addition to this {company_name} places a strong emphasis on teamwork and collaboration within their organization. They foster a culture that values the power of collective effort and encourages employees to work together towards shared goals. By promoting effective communication, cross-functional projects, and a supportive team environment, they enable employees to maximize their potential and achieve success collectively.'
            if list(sorted_variable_dict)[i][0] == keyword9:
                Y = f'In addition to this {company_name} excels in providing exceptional learning and development opportunities for their employees. They understand the significance of continuous growth and offer a range of training programs, workshops, and resources to enhance professional skills. By prioritizing learning and development, they empower individuals to reach their full potential and succeed in their careers, complementing their competitive compensation structure.'
            if list(sorted_variable_dict)[i][0] == keyword10:
                Y = f'In addition to this {company_name} distinguishes itself through its attention to role scope, ensuring that employees have well-defined responsibilities and opportunities for growth. They prioritize providing clear job descriptions, outlining the expectations and parameters of each role within the organization. By offering clarity in role scope, employees can understand their contributions, excel in their positions, and receive the compensation that aligns with their responsibilities.is best know for having a great management...'
        st.write(X + Y)

    with st.expander("Word cloud: How former employees see Amazon"):
  
        amazon_cloud_data = 'smart people, place work, lot learn, work life, life balance, interest problems, people work, work environment, work culture, learn lot, worklife balance, work amazon, company culture, best place, career growth, new things, interest work, learn new, opportunities learn, company work, work experience, challenge problems, compensation package, flexible work, get work, leadership principles, learn curve, many opportunities, career development, work home, work hours, growth opportunities, talented people, challenge work, opportunity learn, nice work, high salary, learn work, interest project, nice people, grow fast, place learn, love work, opportunity work, work high, people around, new ideas, work potential, try new, work project, machine learn, things learn, team work'

        wordcloud_amazon = WordCloud(width=800, height=400, background_color='white', contour_width=3, contour_color='steelblue', random_state=42).generate(amazon_cloud_data)
    
        fig, ax = plt.subplots()
        ax.imshow(wordcloud_amazon, interpolation='bilinear')
        ax.axis("off")
        fig.set_facecolor('white')
        fig.patch.set_alpha(0.7)
    
        st.pyplot(fig)

    with st.expander("How former Employees have rated Amazon?"):
  
        ratings_data_amazon = pd.DataFrame({
            "Ratings": ["5","4","3","2","1"],
            "RatingsbyAmazonEmployees": [043.7,034.8,010.4,004.8,006.3]  
        })

        ratings_data_amazon['Ratings'] = ratings_data_amazon['Ratings'].astype(int)
        ratings_data_amazon = ratings_data_amazon.sort_values('Ratings', ascending=False)

        ratings_bar_chart_amazon = alt.Chart(ratings_data_amazon).mark_bar().encode(
            x='sum(RatingsbyAmazonEmployees)',
            y=alt.Y('Ratings:N', sort='-x'), 
            color='Ratings:N'
        )

        st.altair_chart(ratings_bar_chart_amazon, use_container_width=True)

    with st.expander("Reviews most people found helpful"):
        st.write("1. **Pros**: I hear this is certainly not true for every team, but I think my team is great and I’m very happy at Amazon. - My work life balance is great. I hardly ever have to work more than 40 hours/week. The few times that I do, I don’t particularly mind since I rarely have to. - My team and manager are really chill. Nobody cares when I get to the office, when I leave, or exactly how many hours I was there. I’m certainly expected to get my work done, but I feel like I have a lot of freedom to work on my projects however I’d like. I also work from home about once a week. - This is especially true for Amazon Web Services (where I work) but I feel fortunate that I can learn how to use all the services on AWS for free. My field uses AWS pretty extensively, but it’s normally pretty expensive if you want to use it a lot. We get it all for free and we use it a lot in our everyday work, so I feel pretty lucky to be able to learn it.")
        st.write("**Cons**: Compared to other tech companies Amazon is undoubtedly very cheap. We have to pay for all of our own food, the food is expensive, and it’s also mediocre. Parking isn’t even free. Our benefits are okay but not as good as other tech companies. Our office space looks fine but pretty minimalist. I find this to be minor in the grand scheme of things but it’s definitely noticeable. I dislike being on-call. I’m on call for a week at a time about once every two months. During that time you’re handed a pager and you have to be available 24/7 for issues. This could potentially be on a random weekend afternoon, 8 am in the morning, or worst of all, the dreaded 3 am pager ringing. Fortunately I’m not on-call all that often so I just suck it up and deal with it whenever it rolls around.")
        st.write("2. **Pros**: I worked for AWS Professional Services, the consulting arm of Amazon Web Services. * AWS invests a LOT in your education. 6 weeks of just onboarding, including AWS paying for certification training classes and certification exames * Access to internal AWS accounts makes it easy to experiment and learn * My coworkers were brilliant, and I learned a lot from them * Access to unique customer challenges and datasets * Pay was great, 30% higher than what I was making in my previous job * For a while, some of the travel is great. I got to visit a few cities around the U.S. and even travel internationally * Work-life balanced is manageable. Could be a lot better if there weren't so many time-sucking unnecessary internal processes, but it's not nearly as bad as Amazon's reputation if you google *Amazon work-life balance*.")
        st.write("**Cons**: Amazon is enormous, and as bureaucratic as you'd guess based on that size. I probably bookmarked 200 well-meaning internal sites / tools my first week. Gender diversity was awful on my team. I think it was something like 80 employees, 3 women. Travel in AWS Professional Services is a lot more manageable than at management consultancies, but it can still wear you down. I'd say on average I got about 10 days notice before traveling * Internal communication tools are awful. You have to use Amazon-created, kind-of-ok alternatives to the stack you'd use at a modern company. e.g. Amazon Chime instead of Slack, Microsoft Outlook instead of Google Calendar, etc.")
        st.write("3. **Pros**: Flexible working hours work from home there are many smart people around you who are more than willing to share their knowledge.") 
        st.write("**Cons**: work-life balance not so good highly political flying economy on inter-continental flights no matter your level very rigid HR compensation could be better no perks such as a car on leasing no food provided on campus no tech courses (such as Machine Learning University) in Europe.")

    with st.expander("Top Interview Questions Frequently Asked at Amazon"):
        st.write("General Questions:")
        st.write("- Tell About a Time When...")
        st.write("- Explain One Project on Resume")
        st.write("- Behavioral Questions")
        st.write("- Tell About a Time When You Failed")
      
        st.write("Technical Questions:")
        st.write("- Difference Between Bagging and Boosting")
        st.write("- SQL")
        st.write("- Machine Learning Questions")
        st.write("- Visualize Multidimensional Data")

    with st.expander("Insights into the Interview Process and Job Offer Rates"):
        st.write("- 18% of candidates describe the interview process as difficult for Amazon")
        st.write("- 71% of candidates describe the interview process as average for Amazon")
        st.write("- 22% of candidates receive job offers for Amazon")

if company == 'Google':
    st.write('Google LLC is an American multinational technology company focusing on artificial intelligence, online advertising, search engine technology, cloud computing, computer software, quantum computing, e-commerce, and consumer electronics.')

    with st.expander("Your compatibility analysis"):
        for i in range(1):
            if list(sorted_variable_dict)[i][0] == keyword1:
                X = f'{company_name} is exceptional when it comes to career growth, as they provide a wide variety of training programs, mentoring opportunities, and resources to help employees develop their professional skills and expand their knowledge. The company is deeply committed to recognizing and promoting talent, ensuring that individuals have clear paths for advancement and can successfully achieve their career goals.'
            if list(sorted_variable_dict)[i][0] == keyword2:
                X = f'{company_name} shines in creating a positive work environment that promotes employee well-being and satisfaction. They prioritize fostering a supportive atmosphere where individuals feel valued and motivated to thrive. By offering various perks, work-life balance initiatives, and opportunities for professional development, they ensure that employees can flourish in a fulfilling work environment.'
            if list(sorted_variable_dict)[i][0] == keyword3:
                X = f'{company_name} values work-life balance as a crucial aspect of their company culture. They understand the importance of maintaining a healthy equilibrium between work and personal life. By offering flexible work arrangements, wellness programs, and supportive policies, they empower employees to manage their professional responsibilities while tending to their personal well-being.'
            if list(sorted_variable_dict)[i][0] == keyword4:
                X = f'{company_name} demonstrates a strong commitment to diversity and inclusion within their organization. They actively promote an inclusive work environment that values and respects individuals from all backgrounds and identities. By fostering diversity, they create a space where employees feel empowered to contribute their unique perspectives and experiences, leading to innovation and growth.'
            if list(sorted_variable_dict)[i][0] == keyword5:
                X = f'{company_name} is at the forefront of utilizing technology to drive innovation and enhance productivity. They embrace the latest technological advancements to streamline processes and empower their employees with efficient tools and resources. By leveraging technology, they create a dynamic work environment that promotes collaboration, creativity, and efficiency.'
            if list(sorted_variable_dict)[i][0] == keyword6:
                X = f'{company_name} stands out when it comes to compensation. They offer a wide array of benefits and rewards to recognize and appreciate their employees efforts. With competitive salaries, bonuses based on performance, and attractive incentives, they make sure employees are fairly rewarded. Additionally, they prioritize recognizing talent and supporting career growth, giving individuals opportunities to advance and earn the compensation they deserve.'
            if list(sorted_variable_dict)[i][0] == keyword7:
                X = f'{company_name} distinguishes itself with its people-centric culture that places employees at the heart of the organization. They prioritize creating a supportive and inclusive work environment where individuals feel valued, respected, and empowered. Through their comprehensive compensation packages, professional development opportunities, and recognition programs, they demonstrate their commitment to nurturing a culture that values and invests in their people.'
            if list(sorted_variable_dict)[i][0] == keyword8:
                X = f'{company_name} places a strong emphasis on teamwork and collaboration within their organization. They foster a culture that values the power of collective effort and encourages employees to work together towards shared goals. By promoting effective communication, cross-functional projects, and a supportive team environment, they enable employees to maximize their potential and achieve success collectively.'
            if list(sorted_variable_dict)[i][0] == keyword9:
                X = f'{company_name} excels in providing exceptional learning and development opportunities for their employees. They understand the significance of continuous growth and offer a range of training programs, workshops, and resources to enhance professional skills. By prioritizing learning and development, they empower individuals to reach their full potential and succeed in their careers, complementing their competitive compensation structure.'
            if list(sorted_variable_dict)[i][0] == keyword10:
                X = f'{company_name} distinguishes itself through its attention to role scope, ensuring that employees have well-defined responsibilities and opportunities for growth. They prioritize providing clear job descriptions, outlining the expectations and parameters of each role within the organization. By offering clarity in role scope, employees can understand their contributions, excel in their positions, and receive the compensation that aligns with their responsibilities.'
        for i in range(1,2):
            if list(sorted_variable_dict)[i][0] == keyword1:
                Y = f'In addition to this {company_name} is exceptional when it comes to career growth, as they provide a wide variety of training programs, mentoring opportunities, and resources to help employees develop their professional skills and expand their knowledge. The company is deeply committed to recognizing and promoting talent, ensuring that individuals have clear paths for advancement and can successfully achieve their career goals.'
            if list(sorted_variable_dict)[i][0] == keyword2:
                Y = f'In addition to this {company_name} shines in creating a positive work environment that promotes employee well-being and satisfaction. They prioritize fostering a supportive atmosphere where individuals feel valued and motivated to thrive. By offering various perks, work-life balance initiatives, and opportunities for professional development, they ensure that employees can flourish in a fulfilling work environment.'
            if list(sorted_variable_dict)[i][0] == keyword3:
                Y = f'In addition to this {company_name} values work-life balance as a crucial aspect of their company culture. They understand the importance of maintaining a healthy equilibrium between work and personal life. By offering flexible work arrangements, wellness programs, and supportive policies, they empower employees to manage their professional responsibilities while tending to their personal well-being.'
            if list(sorted_variable_dict)[i][0] == keyword4:
                Y = f'In addition to this {company_name} demonstrates a strong commitment to diversity and inclusion within their organization. They actively promote an inclusive work environment that values and respects individuals from all backgrounds and identities. By fostering diversity, they create a space where employees feel empowered to contribute their unique perspectives and experiences, leading to innovation and growth.'
            if list(sorted_variable_dict)[i][0] == keyword5:
                Y = f'In addition to this {company_name} is at the forefront of utilizing technology to drive innovation and enhance productivity. They embrace the latest technological advancements to streamline processes and empower their employees with efficient tools and resources. By leveraging technology, they create a dynamic work environment that promotes collaboration, creativity, and efficiency.'
            if list(sorted_variable_dict)[i][0] == keyword6:
                Y = f'In addition to this {company_name} stands out when it comes to compensation. They offer a wide array of benefits and rewards to recognize and appreciate their employees efforts. With competitive salaries, bonuses based on performance, and attractive incentives, they make sure employees are fairly rewarded. Additionally, they prioritize recognizing talent and supporting career growth, giving individuals opportunities to advance and earn the compensation they deserve.'
            if list(sorted_variable_dict)[i][0] == keyword7:
                Y = f'In addition to this {company_name} distinguishes itself with its people-centric culture that places employees at the heart of the organization. They prioritize creating a supportive and inclusive work environment where individuals feel valued, respected, and empowered. Through their comprehensive compensation packages, professional development opportunities, and recognition programs, they demonstrate their commitment to nurturing a culture that values and invests in their people.'
            if list(sorted_variable_dict)[i][0] == keyword8:
                Y = f'In addition to this {company_name} places a strong emphasis on teamwork and collaboration within their organization. They foster a culture that values the power of collective effort and encourages employees to work together towards shared goals. By promoting effective communication, cross-functional projects, and a supportive team environment, they enable employees to maximize their potential and achieve success collectively.'
            if list(sorted_variable_dict)[i][0] == keyword9:
                Y = f'In addition to this {company_name} excels in providing exceptional learning and development opportunities for their employees. They understand the significance of continuous growth and offer a range of training programs, workshops, and resources to enhance professional skills. By prioritizing learning and development, they empower individuals to reach their full potential and succeed in their careers, complementing their competitive compensation structure.'
            if list(sorted_variable_dict)[i][0] == keyword10:
                Y = f'In addition to this {company_name} distinguishes itself through its attention to role scope, ensuring that employees have well-defined responsibilities and opportunities for growth. They prioritize providing clear job descriptions, outlining the expectations and parameters of each role within the organization. By offering clarity in role scope, employees can understand their contributions, excel in their positions, and receive the compensation that aligns with their responsibilities.'
        st.write(X + Y)

    with st.expander("Word cloud: How former employees see Google"):
  
        google_cloud_data = 'smart people, work life, life balance, best company, free food, work environment, place work, worklife balance, work culture, work google, nice people, learn lot, people work, company work, every day, benefit work, nice work'

        wordcloud_google = WordCloud(width=800, height=400, background_color='white', contour_width=3, contour_color='steelblue', random_state=42).generate(google_cloud_data)
    
        fig, ax = plt.subplots()
        ax.imshow(wordcloud_google, interpolation='bilinear')
        ax.axis("off")
        fig.set_facecolor('white')
        fig.patch.set_alpha(0.7)
    
        st.pyplot(fig)

    with st.expander("How former Employees have rated Google?"):
  
        ratings_data_google = pd.DataFrame({
            "Ratings": ["5","4","3","2","1"],
            "RatingsbyGoogleEmployees": [066.7,027.1,004.3,001.4,000.5]  
        })

        ratings_data_google['Ratings'] = ratings_data_google['Ratings'].astype(int)
        ratings_data_google = ratings_data_google.sort_values('Ratings', ascending=False)

        ratings_bar_chart_google = alt.Chart(ratings_data_google).mark_bar().encode(
            x='sum(RatingsbyGoogleEmployees)',
            y=alt.Y('Ratings:N', sort='-x'), 
            color='Ratings:N'
        )

        st.altair_chart(ratings_bar_chart_google, use_container_width=True)

    with st.expander("Reviews most people found helpful"):
        st.write("1. **Pros**: Great tech infrastructure systems, but it's hard to know which ones to use. This is usually served by having senior team members who know what they're doing, but teams in Finance generally don't have that (employee churn).")
        st.write("**Cons**: Innovation is nonexistent: too many in the company are from non-tech / corporate backgrounds. This is especially true for those in management positions. As a result, decisions made are often too conservative. There are lots of talking points about how the org is innovating what a finance department can do but most of the people who do the innovating leave as soon as they can. Not a gateway to Google: I joined thinking that the I could work in Finance for a while learning new skills and working on cool projects on my way to moving into the eng org. This is generally not the case. What I didn't realize when I joined is that I was on a Finance ladder. As a result, transferring to the eng org involves a full interview process. These interviews are (from many people I've talked to) more stringent than the external ones. Ask which ladder you'll be placed on before accepting the offer! (This is also why the offer was FAR lower than what I expected).")
        st.write("2. **Pros**: The money’s great! The free gourmet food and snacks are never-ending Working at Google, you're exposed to amazing people and great thinkers Googlers feel like they are really living in the future Dogs are welcome!") 
        st.write("**Cons**: Learning is self-driven The competition is brutal Supervision is minimal.")
        st.write("3. **Pros**: Great job security Clear path to promotion Smart colleagues Excellent career development resources Diverse workplace Creative freedom and autonomy Effective feedback processes.") 
        st.write("**Cons**: Can be quite political Multiple teams working on the same project Some loud and disrespectful employees Sexual and racial harassment/discrimination happens more often than it should given their external messaging/image they project Not true to their stated ethics.")

    with st.expander("Top Interview Questions Frequently Asked at Google"):
        st.write("General Questions:")
        st.write("- Prior Projects Worked")
        st.write("- Responsibilities")
        st.write("- Questions on Setting Priorities and Multitasking")
        st.write("- Describe Previous Experience")
      
        st.write("Technical Questions:")
        st.write("- Machine Learning and Statstics Questions")
        st.write("- Standard Mean Error")
        st.write("- SQL and Window Functions")
        st.write("- Describe How Principal Component Analysis Works")

    with st.expander("Insights into the Interview Process and Job Offer Rates"):
        st.write("- 34% of candidates describe the interview process as difficult for Google")
        st.write("- 60% of candidates describe the interview process as average for Google")
        st.write("- 14% of candidates receive job offers for Google")

