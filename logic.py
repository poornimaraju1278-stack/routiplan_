from js import document

def generate():
    name = document.getElementById("name").value
    m_start = document.getElementById("m_start").value
    m_end = document.getElementById("m_end").value
    n_start = document.getElementById("n_start").value
    n_end = document.getElementById("n_end").value
    goal = document.getElementById("goal").value
    category = document.getElementById("category").value
    priority = document.getElementById("priority").value

    routine = f"""
    <div class='card p-3'>
        <h4>Good day, {name}! 😊</h4>
        <p>🌅 Morning: {m_start} - {m_end}</p>
        <p>🎯 Goal: {goal} ({category})</p>
        <p>🔥 Priority: {priority}</p>
        <p>🌙 Night: {n_start} - {n_end}</p>
        <p>💡 Stay consistent. Small steps every day!</p>
    </div>
    """

    document.getElementById("output").innerHTML = routine
