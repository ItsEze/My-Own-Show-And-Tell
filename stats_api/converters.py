from django.urls import converters

class PlatformTypeConverter(converters.StringConverter):
    allowed_platforms = ['kbm', 'touch', 'gamepad']
    
    def to_python(self, value):
        if value.lower() not in self.allowed_platforms:
            raise ValueError('Invalid platform type')
        return value.lower()