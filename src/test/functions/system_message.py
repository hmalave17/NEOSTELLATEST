from pathlib import Path
import sys
BASE_DIR = Path(__file__).resolve().parent.parent  
sys.path.append(str(BASE_DIR / "functions"))

class SystemMessage:

    FORM_SENDING = "📝 Sending form {num} - Data: {data}"       
    FORM_SUCCESS = "📤 Form {num} successfully submitted"
    AUTOMATION_START = "🚀 Starting automation..."
    AUTOMATION_END = "🏁 Automation completed successfully"
    LOGIN_SUCCESS = "🔑 Login successful"
    LOGIN_ATTEMPT = "🔍 Attempting login with user: {user}"
    MISSING_FIELD = "⚠️ Empty field for label '{label}', skipping."  
    FIELD_NOT_FOUND = "⚠️ No field found for label '{label}'"
    VALIDATION_SKIPPED = "⚠️ Validation skipped: {reason}"
    RECAPTCHA_DETECTED = "❗ reCAPTCHA detected, attempting to close..."
    RECAPTCHA_CLOSED = "✅ reCAPTCHA popup closed."
    NO_FOUND_RECAPCHA = "No reCAPTCHA popup detected."
    FORM_ERROR = "❌ Error submitting form {num}: {error}"      
    LOGIN_ERROR = "❌ Login error: {error}"
    SUBMIT_ERROR = "❌ Failed to submit the form correctly"
    TIMEOUT_ERROR = "❌ Challenge not completed. 'SUCCESS!' message not found."
    TIME_MESSAGE_ERROR = "Time message not found"
    MESSAGE_NOT_FOUND = "❌ Challenge not completed. 'SUCCESS!' message not found."
    LIST_EMPTY = "The data list is empty. The form cannot be filled out."
    DEBUG_INPUT_FILL = "🖋️ Filling field '{field}' with value '{value}'"  
    DEBUG_LIST_STATUS = "📋 Full list: {valueData}, Length: {length}"
    DEBUG_INDEX_VALUE = "🔢 Index: {index}, Value: {value}"              
    DEBUG_RECAPCHA = "⏱️ Timeout while checking for reCAPTCHA popup."
    CHALLENGE_COMPLETED = "✅ Challenge completed successfully!"
    TIME_VALIDATION_SUCCESS = "✅ Time validation completed!"
    FORM_SEND_SUCCESSFUL = "📤 Form send successful"

    @staticmethod
    def format(message, **kwargs):
        return message.format(**kwargs)
