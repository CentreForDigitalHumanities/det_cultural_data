from IPython.core.display import HTML
from pathlib import Path

def code_block(code_block_rows):
    html = '<pre  style="display: inline-block; float: left; margin-right: 10px"><code>' 
    for i,row in enumerate(code_block_rows):
        if i != len(code_block_rows)-1 :
            html += row + '\n'
        else:
            html += row
    html += '</code></pre>'

    return html

def list_to_html(items,opt='ul',code=False):

    if not opt in ['ol','ul']:
        raise ValueError('opt must be either up or ol')

    html = f'<{opt}>'
    for item in items:
        if code:
            html_line = f'<li><code>{item.strip()}</code></li>'
        else:
            html_line = f'<li>{item.strip()}</li>'
        html += html_line
        
    html += f'</{opt}>'  

    return html
    
def question_box(question='',task='',process='',tools='',code='',warning='',wiz='',solution='',
                 code_block = False,
                 css_style_file='myutils/css/boxes.css'):
    '''
    It takes text and html text to put into pre-defined boxes:
    - Research question (text);
    - Process, described into tasks (html list or text);
    - (programming) Tools to be used (html list or text);
    - Code used to implement the process (html list or text);

    PARAMETERS
    ----------
    question: str
        Question to implement
    task: str
        Same as question but with a different string
    process: str
        String containing text or html to describe the general process
        to answer the question
    tools: str
        String containing text or html to list the programming tools
        to be used in the implementation (python packages, functions,
        etc)
    code: str
        String containing text or html to describe step by step the
        programming implementation
    guru: str:
        Same as code, intended to contain expert level coding
    css_style_file: str
        String with the relative path containing the css file

    RETURNS
    -------
    display object, when this object is returned by an expression or 
    passed to the display function, it will result in the data being 
    displayed in the frontend.
    '''

    if type(css_style_file) == str:
        css_style_file = Path(css_style_file)

    # Load the CSS file and create a link tag
    css = ''
    if css_style_file.exists():
        with open(css_style_file, 'r') as css_file:
            css_content = css_file.read()
        css = f'<style>{css_content}</style>'

    sub_box1 = ''
    if question:
        sub_box1 = f''' 
            <div class="box type1">
                    <div class="sub-box">
                        <img src="myutils/icons/question.png" alt="Icon" class="picture"/>
                        <div class="ctitle">
                            <u><h4><strong>Question(s)</strong></h4></u>
                        </div>
                    </div>
                    <div class="sub-box">
                        {question}
                    </div>
            </div>
        '''

    sub_box1b = ''
    if task:
        sub_box1b = f''' 
            <div class="box type1">
                    <div class="sub-box">
                        <img src="myutils/icons/task.png" alt="Icon" class="picture"/>
                        <div class="ctitle">
                            <u><h4><strong>Task(s)</strong></h4></u>
                        </div>
                    </div>
                    <div class="sub-box">
                        {task}
                    </div>
            </div>
        '''

    sub_box2 = ''
    if process:
        sub_box2 = f'''
            <div class="box type2">
                <div class="sub-box">
                    <img src="myutils/icons/thinking.png" alt="Icon" class="picture"/>
                    <div class="ctitle">
                        <u><h4><strong>What to do?</strong></h4></u>
                    </div>
                </div>
                <div class="sub-box">
                    {process}
                </div>
            </div>    
        '''

    sub_box2b = ''
    if solution:
        sub_box2b = f'''
            <div class="box type6">
                <div class="sub-box">
                    <img src="myutils/icons/solution.png" alt="Icon" class="picture"/>
                    <div class="ctitle">
                        <u><h4><strong>Answer</strong></h4></u>
                    </div>
                </div>
                <div class="sub-box">
                    {solution}
                </div>
            </div>    
        '''

    sub_box2c = ''
    if warning:
        sub_box2c = f'''
            <div class="box">
                <div class="sub-box">
                    <img src="myutils/icons/warning.png" alt="Icon" class="picture"/>
                    <div class="ctitle">
                        <u><h4><strong>!!! Warning !!!</strong></h4></u>
                    </div>
                </div>
                <div class="sub-box">
                    {warning}
                </div>
            </div>    
        '''

    sub_box3 = ''
    if tools:
        sub_box3 = f'''
            <div class="box type3">
                <div class="sub-box">
                    <img src="myutils/icons/tools.png" alt="Icon" class="picture"/>
                    <div class="ctitle">
                        <u><h4><strong>(Python) Tools</strong></h4></u>
                    </div>
                </div>
                <div class="sub-box">
                    {tools}
                </div>            
            </div>    
        '''

    sub_box = 'class="sub-box"' if code_block else ''
    sub_box4 = ''
    if code:
        sub_box4 = f'''
            <div class="box type4">
                <div class="sub-box">
                    <img src="myutils/icons/code_expl.png" alt="Icon" class="picture"/>
                    <div class="ctitle">
                        <u><h4><strong>Coding</strong></h4></u>
                    </div>
                </div>
                <div class="sub-box">
                    <div>
                        {code}
                    </div>       
                </div>
            </div>    
        '''

    sub_box4b = ''
    if wiz:
        sub_box4b = f'''
            <div class="box type5">
                <div class="sub-box">
                    <img src="myutils/icons/wiz.png" alt="Icon" class="picture"/>
                    <div class="ctitle">
                        <u><h4><strong>Expert Coding</strong></h4></u>
                    </div>
                </div>
                <div class="sub-box">
                    <div>
                        {wiz}
                    </div>  
                </div>
            </div>    
        '''    
    
    html_code = f'{css}{sub_box1}{sub_box1b}{sub_box2}{sub_box3}{sub_box4}{sub_box2c}{sub_box4b}{sub_box2b}'
    return HTML(html_code)