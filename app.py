import sys
import io
from flask import Flask, render_template, request, jsonify
from curriculum import lessons_data

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('index.html', lessons=lessons_data)

@app.route('/lesson/<int:lesson_id>')
def lesson(lesson_id):
    # Find the specific lesson
    lesson = next((l for l in lessons_data if l['id'] == lesson_id), None)
    return render_template('lesson.html', lesson=lesson)

@app.route('/run_code', methods=['POST'])
def run_code():
    data = request.json
    user_code = data.get('code')
    lesson_id = data.get('lesson_id')
    
    # Get expected answer for this lesson
    target_lesson = next((l for l in lessons_data if l['id'] == lesson_id), None)
    
    # SECURITY WARNING: exec() is dangerous in public websites. 
    # Since this is for your LOCAL learning only, it is safe.
    
    # Capture standard output (what print() sends)
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    
    result = "Error"
    passed = False
    
    try:
        # Dictionary to store local variables defined in user's code
        local_scope = {}
        exec(user_code, {}, local_scope)
        result = redirected_output.getvalue().strip()
        
        # Check against expected output
        if str(result) == str(target_lesson['expected_output']):
            passed = True
            
    except Exception as e:
        result = f"Error: {e}"
    finally:
        sys.stdout = old_stdout # Reset output

    return jsonify({"output": result, "passed": passed})

if __name__ == '__main__':
    app.run(debug=True)