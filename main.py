import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open(r"C:\Users\RupesH\Desktop\AIRLINEPASSENGER\build1.pkl", "rb"))

st.title(" Airline Passenger Satisfaction ")
st.subheader("Welcome to the Airline Passenger Prediction Web App!" )
st.markdown("An airline passenger satisfaction web app is a tool that can be used to collect and analyze feedback from airline passengers. This feedback can be used to identify areas where the airline can improve its services and provide a better passenger experience.")
st.image("image.jpg")
def prediction(Online_Boarding,
    Class,
    Type_of_Travel,
    In_flight_Entertainment,
    Seat_Comfort,
    On_board_Service,
    Leg_Room_Service,
    Cleanliness,
    In_flight_Wifi_Service,
    Flight_Distance,
    Baggage_Handling,
    In_flight_Service,
    Check_in_Service,
    Food_and_Drink,
    Ease_of_Online_Booking,
    Age,
    Departure_Delay,
    Departure_and_Arrival_Time_Convenience,
    Arrival_Delay):
      
        if Type_of_Travel == "Personal":
            Type_of_Travel = 0
        else:
            Type_of_Travel = 1
    
        if Class == "Economy":
            Class = 0
        elif Class == "Economy Plus":
            Class = 1
        else :
            Class = 2

        input = np.array([[Online_Boarding,Class,Type_of_Travel,In_flight_Entertainment,Seat_Comfort,On_board_Service,Leg_Room_Service,Cleanliness,
                In_flight_Wifi_Service,Flight_Distance,Baggage_Handling,In_flight_Service,Check_in_Service,Food_and_Drink,Ease_of_Online_Booking,Age,
                Departure_Delay,Departure_and_Arrival_Time_Convenience,Arrival_Delay]])
        prediction = model.predict(input)
        pred = 'Passenger is Satisfied' if prediction == 1 else 'Passenger is Unsatisfied'
        return pred

def main():
        Age = st.number_input("Age (years)",1)
        Class = st.selectbox("Class", ["Economy", "Economy Plus", "Business"])
        Type_of_Travel = st.selectbox("Type of Travel", ["Personal", "Business"])
        Departure_Delay = st.number_input("Departure Delay")
        Arrival_Delay = st.number_input("Arrival Delay Time")
        Flight_Distance = st.number_input("Flight Distance (Miles)")
        Online_Boarding = st.slider("Online Boarding", 0, 5, 5)
        In_flight_Entertainment = st.slider("In-flight Entertainment", 0, 5, 5)
        Seat_Comfort = st.slider("Seat Comfort", 0, 5, 5)
        On_board_Service = st.slider("On-board Service", 0, 5, 5)
        Leg_Room_Service = st.slider("Leg Room Service", 0, 5, 5)
        Cleanliness = st.slider("Cleanliness", 0, 5, 5)
        In_flight_Wifi_Service = st.slider("In-flight Wifi Service", 0, 5, 5)
        Baggage_Handling = st.slider("Baggage Handling", 0, 5, 5)
        In_flight_Service = st.slider("In-flight Service", 0, 5, 5)
        Check_in_Service = st.slider("Check-in Service", 0, 5, 5)
        Food_and_Drink = st.slider("Food and Drink", 0, 5, 5)
        Ease_of_Online_Booking = st.slider("Ease of Online Booking", 0, 5, 5)
        Departure_and_Arrival_Time_Convenience = st.slider("Convenience Time", 0,5,5)
        
       

        if st.button("Predict"):
            result = prediction( Online_Boarding,Class,Type_of_Travel,In_flight_Entertainment,Seat_Comfort,On_board_Service,Leg_Room_Service,Cleanliness,
                In_flight_Wifi_Service,Flight_Distance,Baggage_Handling,In_flight_Service,Check_in_Service,Food_and_Drink,Ease_of_Online_Booking,Age,
                Departure_Delay,Departure_and_Arrival_Time_Convenience,Arrival_Delay)
            
            st.write("Prediction:", result)

if __name__ == "__main__":
        main()