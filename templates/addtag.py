#
#
#
# <!--
# <div class="jumbotron">
# 	<h1 align='center'>{% if tag %} Изменение метки {% else %} Создание новой метки {% endif %}</h1>
# </div>
#
#
#
# <div class='col-md-12'>
# 	<form action="" method="post">{% csrf_token %}
# 	{{form.as_p}}
#
# 	<input type='submit' value=
#                 {% if tag %}
#                     'Изменить метку'
#                 {% else %}
#                     'Создать метку'
#                 {% endif %}
#         class='btn btn-primary btn-lg btn-block' />
# 	</form>
# </div>
#
# {% if tag %}
# <div class="col-md-12" style="padding-top:15px">
#     <form action="" method="POST">{% csrf_token %}
#     <input type="hidden" name="control" value="delete" />
#     <input type="submit" value="Удалить заметку" class="btn btn-lg btn-block btn-danger" />
#     </form>
# </div>
# {% endif %}
#
# -->
