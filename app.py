import streamlit as st

def calculate_overall_rating():
    points = 0.0
    
    # Question 1
    response = st.radio("Were you sloppy or allow a TM to be sloppy during this sprint?", ["Yes", "No"], index=0)
    if response == "No":
        points += 1.0
    
    # Question 2
    response = st.radio("Did you make Every Day Count during the sprint?", ["Yes", "No"], index=1)
    if response == "Yes":
        points += 1.0
    
    # Question 3
    response = st.radio("Did you complete a Sprint goal?", ["Yes", "No"], index=1)
    if response == "Yes":
        points += 1.0
    
    # Question 4
    response = st.slider("On a scale of 1 to 5, what is your overall sprint rating for yourself?", 1, 5, step=1, value=1)
    points += response / 5.0
    
    # Question 5
    response = st.slider("On a scale of 1 to 5, what is your overall sprint rating for your team?", 1, 5, step=1, value=1)
    points += response / 5.0
    
    # Bonus question
    response = st.radio("Did you do something extraordinary during this sprint?", ["Yes", "No"], index=1)
    if response == "Yes":
        points += 1.0

    return points


# Streamlit app
def main():
    st.title("Sprint Rating")
    st.write("Answer the following questions to calculate your overall rating for the sprint.")
    overall_rating = calculate_overall_rating()

    overall_rating_rounded = round(overall_rating)
    overall_rating_rounded = max(min(overall_rating_rounded, 5), 1)  # Clamp the rating between 1 and 5

    stars = ["★☆☆☆☆", "★★☆☆☆", "★★★☆☆", "★★★★☆", "★★★★★"]
    star_rating = stars[overall_rating_rounded - 1]
    st.write(f"<span style='font-size: 24px; color: red;'>Overall rating: {overall_rating:.1f} {star_rating}</span>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
