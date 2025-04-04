from data_handler import save_candidate_data, log_interaction

test_user = {
    "name": "John Doe",
    "email": "john@example.com",
    "tech_stack": "Python, React"
}

save_candidate_data(test_user)
log_interaction("Test log from user")
print("✅ Data saved and log written.")
