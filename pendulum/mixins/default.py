# -*- coding: utf-8 -*-

import re
from ..translator import Translator


class TranslatableMixin(object):

    _translator = None

    @classmethod
    def translator(cls):
        """
        Initialize the translator instance if necessary.

        :rtype: Translator
        """
        if cls._translator is None:
            cls._translator = Translator('en')
            cls.set_locale('en')

        return cls._translator

    @classmethod
    def set_translator(cls, translator):
        """
        Set the translator instance to use.

        :param translator: The translator
        :type translator: Translator
        """
        cls._translator = translator

    @classmethod
    def get_locale(cls):
        """
        Get the current translator locale.

        :rtype: str
        """
        return cls.translator().locale

    @classmethod
    def set_locale(cls, locale):
        """
        Set the current translator locale and
        indicate if the source locale file exists.

        :type locale: str

        :rtype: bool
        """
        locale = cls.format_locale(locale)

        if not cls.translator().register_resource(locale):
            return False

        cls.translator().locale = locale

        return True

    @classmethod
    def format_locale(cls, locale):
        """
        Properly format locale.

        :param locale: The locale
        :type locale: str

        :rtype: str
        """
        m = re.match('([a-z]{2})[-_]([a-z]{2})', locale, re.I)
        if m:
            return '{}_{}'.format(m.group(1).lower(), m.group(2).lower())
        else:
            return locale.lower()
