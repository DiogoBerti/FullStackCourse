from django import forms
from blog.models import Post, Comments


# Adicionando os formularios para manipulacao na page...
class PostForm(forms.ModelForm):

    # Essa classe meta é onde definimos qual model e quais campos podem ser
    # manipulados pelo formulario...
    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        # Esses Widgets são, basicamente, componentes visuais usados no formulario.
        # Atencao para as classes editable e medium pois são de bibliotecas
        # externas....
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={
                'class':'editable medium-editor-textarea postcontent'
                })
        }



class CommentForm(forms.ModelForm):

    class Meta():
        model = Comments
        fields = ('author', 'text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={
                'class':'editable medium-editor-textarea'
                })
        }
