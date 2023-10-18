from constants import RWIDTH, RHEIGHT

class HTML_Renderer:

    def __init__(self):
        """
        Instantiates a new instance of HTML_Renderer.
        """

    def get_body_text(self, body):
        """
        Gets all the text (exludes the tags) of an HTML body.

        Returns:
            str: All the text of an HTML body.
        """
        in_angle = False
        text = ""
        for c in body:
            if c == '<':
                in_angle = True
            elif c == '>':
                in_angle = False
            if not in_angle:
                text += c
        return text
    
    def layout_text(self, text):
        """
        Builds a display list where an entry looks like: (x, y, c). 'x' is the x position of the character, 'y' is the y position of the character, and 'c' is the character itself.
        
        Returns:
            list: A display list.
        """
        x_step = 10
        y_step = 15
        x = x_step
        y = y_step
        display_list = []
        for c in text:
            display_list.append((x, y, c))
            x += x_step
            if x > RWIDTH - x_step:
                x = x_step
                y += y_step
        
        return display_list

