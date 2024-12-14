from django.contrib.auth.forms import UserCreationForm as CreationForm
from django.contrib.auth.forms import UserChangeForm as ChangeForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User


class UserCreationForm(CreationForm):
    """
    This form extends the default UserCreationForm
    to include custom fields and logic. It is designed
    to handle the creation of new user accounts, ensuring that the
    username and email are properly set and that the user's display name is
    initialized with the username. This setup is ideal for user registration
    forms where additional customization is required.
    """

    class Meta:
        model = User
        fields = [
            "username",
            "email"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({
                "placeholder": field.label,
                "class": "p-2 placeholder-primary border-[2px] border-accent bg-background text-accent rounded-[1px] transition-all duration-300 focus:outline-none focus:ring-0 focus:border-accent focus:shadow-retro"
            })

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.display_username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user


class UserAuthenticationForm(AuthenticationForm):
    """
    This form extends the default UserCreationForm
    to include custom fields and logic. It is designed
    to handle the creation of new user accounts, ensuring that the
    username and email are properly set and that the user's display name is
    initialized with the username. This setup is ideal for user registration
    forms where additional customization is required.
    """
    
    class Meta:
        model = User
        fields = [
            "username",
            "email"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({
                "placeholder": field.label,
                "class": "p-2 placeholder-primary border-[2px] border-accent bg-background text-accent rounded-[1px] transition-all duration-300 focus:outline-none focus:ring-0 focus:border-accent focus:shadow-retro"
            })


class UserChangeForm(ChangeForm):
    """
    This form extends the default UserChangeForm
    to include custom fields and logic. It is designed to
    handle the modification of existing user accounts, allowing
    changes to the username, display name, email, and password.
    This setup is ideal for admin panels or user profile management
    interfaces where comprehensive user information editing is required.
    """

    class Meta:
        model = User
        fields = [
          "username",
          "display_username",
          "email",
          "password"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({
                "placeholder": field.label,
                "class": "p-2 placeholder-primary border-[2px] border-accent bg-background text-accent rounded-[1px] transition-all duration-300 focus:outline-none focus:ring-0 focus:border-accent focus:shadow-retro"
            })