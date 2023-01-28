from flask import Blueprint, render_template, request, url_for

from pybo.models import Question

bp = Blueprint('tt', __name__, url_prefix='/t')


@bp.route('/aa')
def _list1():
    return render_template('question/test2.html')

# from flask import send_file

# @bp.route('/wav_file')
# def _list():
#      path_to_file = "/question/wav_file"

#      return send_file(
#          path_to_file, 
#          mimetype="audio/wav", 
#          as_attachment=True, 
#          attachment_filename="test.mp3")



@bp.route('/list/text', methods=['GET', 'POST'])
def _list2():
    if request.method == 'POST' :
        print(request.form['textarea'])
        from ..ai_model.TTS import tts_test
        

        return render_template('question/test2.html')
    else :
        return render_template('question/test.html')


# if request.method == 'POST':
#         date = request.form['date']
#         title = request.form['blog_title']
#         post = request.form['blog_main']
#         post_entry = models.BlogPost(date = date, title = title, post = post)
#         db.session.add(post_entry)
#         db.session.commit()
#         return redirect(url_for('database'))
#     else:
#         return render_template('entry.html')