@app.route("/interviewPrompt", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        job = request.form["job"]
        experience = request.form['experience']
        print(job)
        print(experience)
response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=f"Create a list of 8 questions for my interview as a {experience} {job}\n",
        temperature=0.5,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
        
        text = response.choices[0].text
        print(text)
        list = text.split('\n')[1:]
        list = filter(None, list)
        # list = ["sfsdgfsegds","sfsargsgd","sefsargsrgdsr"]
return render_template("interview.html", 
        list=list
        )
else:
     return render_template("interviewPrompt.html")
