from django import forms
from sfv.models import Story
from django.template.defaultfilters import slugify



class StoryForm(forms.ModelForm):
    '''
    Very straightforward form for creating new Story from Vilnius.
    Request instance is passed in order to bind the story to currently logged in User.
    Unique Story title is required to generate unique slugs (for URLs)
    '''
    class Meta:
        model = Story
        fields = ('title', 'content', 'picture' , 'city', 'location')



    def __init__(self, request, *args, **kwargs):
       super(StoryForm, self).__init__(*args, **kwargs)
       self.request = request
       self.user = request.user
       self.fields['title'].widget.attrs['class'] = 'title'
       self.fields['content'].widget.attrs['class'] = 'content'
       self.fields['picture'].widget.attrs['class'] = 'picture'
       self.fields['location'].widget.attrs['class'] = 'coords'


    def clean(self):
    	super(StoryForm, self).clean()
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        slug = slugify(title)
        if Story.objects.filter(user=self.user, slug = slug).exists():
            self._errors['title'] = 'Such title already exists'
        return cleaned_data

    def save(self):
        story = super(StoryForm, self).save(commit=False)
        story.user = self.user
        story.save()
        return story
