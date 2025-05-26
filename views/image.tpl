<div class="ui segment">
    <h2 class="ui center aligned header">Cat #{{ image_id }}</h2>
    
    <div class="image-container">
        <img src="/static/{{image_id}}.jpg" alt="Cat {{ image_id }}" class="ui rounded image">
    </div>
    
    <div class="navigation">
        <a href="/image/{{ prev_id }}" class="ui labeled icon button">
            <i class="left arrow icon"></i>
            Previous
        </a>
        <a href="/image/{{ next_id }}" class="ui right labeled icon button">
            <i class="right arrow icon"></i>
            Next
        </a>
    </div>

    {% for i in numbers %}
    <div>YAY {{ i }}</div>
    {% if i == image_id %}
    <div>WOW</div>
    {% endif %}
    {% endfor %}
    
    <div class="ui tiny statistics" style="display: flex; justify-content: center; margin-top: 20px;">
    </div>
</div>
