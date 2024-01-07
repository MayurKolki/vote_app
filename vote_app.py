import streamlit as st
import psycopg2

def create_connection():
    conn = psycopg2.connect(
        database ="mayur_test",
        user = "postgres",
        password = 4212,
        host = "localhost",
        port = 5432
    )
    return conn

def main():
    st.title("APARICHIT TRUTH ELECTION 2024")

    age = st.number_input("Enter your age :",min_value=0,max_value=150,value=18)
    gender = st.selectbox("Select your gender :",["Male","Female","Other"])
    candidate = st.radio("Choose your Candidate :",["N D A","I N D I A","None"])

    if age and gender and candidate:
        st.write(f"Your age : {age}")
        st.write(f"Your gender : {gender}")
        st.write(f"Your candidate : {candidate}")
        if st.button("Vote"):
            try:
                conn = create_connection()
                cursor = conn.cursor()
                insert_query = f"INSERT INTO votes(age , gender , party) VALUES (%s, %s, %s)"
                values = (age,gender,candidate)
                cursor.execute(insert_query,values)
                conn.commit()
                st.success("Thank you for voting!")
            except Exception as e:
                st.error(f"Error inserting date : {e}")
            finally:
                cursor.close()
                conn.close()

if __name__ == "__main__":
    main()