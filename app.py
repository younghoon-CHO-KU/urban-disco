
from flask import Flask, render_template, request, Response
import os
import random
import glob
import shutil

app = Flask(__name__)

@app.route("/")
def init(chk = None):
	return render_template('new_post.html', chk = chk)

@app.route('/redirect', methods=['POST', 'GET'])
def redirect(chk = None):
    if request.method == 'GET':
        # story_prompt
        prompt = request.args.get('story_prompt')
        if 'story_prompt.txt' in os.listdir():
            os.remove('story_prompt.txt')
        file = open('story_prompt.txt', 'w')
        file.write(prompt)
        file.close()
        num_scenes = request.args.get('num_scenes')
        if 'num_scenes.txt' in os.listdir():
            os.remove('num_scenes.txt')
        file = open('num_scenes.txt', 'w')
        file.write(num_scenes)
        file.close()
        return render_template('new_post.html', chk = chk)
    elif request.method == 'POST':
        # title
        title_file_path = 'static/title/title.txt'
        f = open(title_file_path, 'r')
        title = f.readline()
        f.close()
        # question
        question_file_path_list = sorted(os.path.join('static/question', file_name) for file_name in os.listdir('static/question'))
        question_list = list()
        for question_file_path, i in zip(question_file_path_list, range(len(question_file_path_list))):
            f = open(question_file_path, 'r')
            question_list.append(str(i+1)+ '. ' + f.readline())
            f.close()
        # prompt
        prompt_file_path_list = sorted(os.path.join('static/prompt', file_name) for file_name in os.listdir('static/prompt'))
        prompt_list = list()
        for prompt_file_path, i in zip(prompt_file_path_list, range(len(prompt_file_path_list))):
            f = open(prompt_file_path, 'r')
            prompt_list.append(str(i+1)+ '. ' + f.readline())
            f.close()
        # subtitle
        subtitle_file_path_list = sorted(os.path.join('static/subtitle', file_name) for file_name in os.listdir('static/subtitle'))
        subtitle_list = list()
        for subtitle_file_path, i in zip(subtitle_file_path_list, range(len(subtitle_file_path_list))):
            f = open(subtitle_file_path, 'r')
            subtitle_list.append('< '+f.readline()+' >')
            f.close()    

        
        
        return render_template('new_post.html', chk = 'show', prompts = prompt_list, questions = question_list, subtitles = subtitle_list, num_prompt = len(prompt_list), num_question = len(question_list)) 
    
@app.route('/storygen', methods=['GET', 'POST'])
def storygen():
    if request.method == 'GET':
        if 'story_prompt.txt' in os.listdir():
            f = open('story_prompt.txt', 'r')
            story_prompt = f.readline()
            f.close()
            os.remove('story_prompt.txt')
            f = open('num_scenes.txt', 'r')
            num_scenes = f.readline()
            f.close()
            os.remove('num_scenes.txt')
            folder_list = ['prompt', 'question', 'subtitle', 'title']
            for folder in folder_list:
                if os.path.exists(os.path.join('static', folder)):
                    shutil.rmtree(os.path.join('static', folder))
                os.mkdir(os.path.join('static', folder))
            return Response(story_prompt + ',' + num_scenes, status=200)
        else:
            return  Response(status=404)
    elif request.method == 'POST':
        # img-text
        # print('request.form: ', request.form)
        # title
        post_type = int(request.form['type'])
        if post_type == 0:
            print('type_0')
            title_filename = 'title/title.txt'
            title_file = open('static/' + title_filename, 'w')
            title_file.write(request.form['title'])
            title_file.close()
        elif post_type == 1:
            # save image
            print('type_1')
            img = request.files['file']
            print(img.filename)
            img.save('static/image/' + img.filename)
            # save prompt
            prompt_filename = 'prompt/prompt' + request.form['num'] + '.txt'
            print(prompt_filename)
            prompt_file = open('static/' + prompt_filename, 'w')
            prompt_file.write(request.form['prompt'])
            prompt_file.close()
            # save subtitle
            subtitle_filename = 'subtitle/subtitle' + request.form['num'] + '.txt'
            subtitle_file = open('static/' + subtitle_filename, 'w')
            subtitle_file.write(request.form['subtitle'])
            subtitle_file.close()
        # question
        elif post_type == 2:
            print('type_2')
            question_filename = 'question/question' + request.form['num'] + '.txt'
            question_file= open('static/' + question_filename, 'w')
            question_file.write(request.form['question'])
            question_file.close()

        return 'clear'

if __name__ == "__main__":
    # app.run(host = '192.168.25.112', port='17864') 
    app.run(host = '192.168.25.112', port = '17864')