from django.db import models


MOTIVATION_CHOISES = (
    ('6', '6'),
    ('5', '5'),
    ('4', '4'),
    ('3', '3'),
    ('2', '2'),
    ('1', '1'),
)


FREQUENCY_CHOISES = (
    ('0', 'やめたい'),
    ('1', '毎日'),
    ('2', '毎週'),
    ('3', '毎月'),
)


DIVISION_CHOISES = (
    ('朝', '朝'),
    ('昼', '昼'),
    ('夜', '夜'),
    ('月', '月'),
    ('火', '火'),
    ('水', '水'),
    ('木', '木'),
    ('金', '金'),
    ('土', '土'),
    ('日', '日'),
    ('土日', '土日'),
)


HABITGENRE1_CHOISES = (
    ('意思', '意思'),
    ('行動', '行動'),
    ('向上', '向上'),
    ('喧嘩', '喧嘩'),
    ('目標', '目標'),
    ('関係', '関係'),
    ('他', '他'),
)


PROBGENRE1_CHOISES = (
    ('生活', '生活'),
    ('心', '心'),
    ('他', '他'),
)


PROBGENRE2_CHOISES = (
    ('怒り', '怒り'),
    ('イライラ', 'イライラ'),
    ('ネガティブ', 'ネガティブ'),
    ('不調', '不調'),
    ('不安', '不安'),
    ('人生最悪', '人生最悪'),
    ('やる気', 'やる気'),
    ('睡眠', '睡眠'),
    ('他', '他'),
)


class Habit_motivation(models.Model):
    motivation = models.IntegerField(blank=True, default=4, choices=MOTIVATION_CHOISES)


class Habit_frequency(models.Model):
    frequency = models.IntegerField(blank=True, default=1, choices=FREQUENCY_CHOISES)


class Habit_division(models.Model):
    division = models.CharField(blank=True, max_length=100, choices=DIVISION_CHOISES)


class Habit_habitgenre1(models.Model):
    habitgenre1 = models.CharField(max_length=100, default='意思', choices=HABITGENRE1_CHOISES)


class Habit_probgenre1(models.Model):
    probgenre1 = models.CharField(blank=True, max_length=100, default='心', choices=PROBGENRE1_CHOISES)


class Habit_probgenre2(models.Model):
    probgenre2 = models.CharField(blank=True, max_length=100, default='不安', choices=PROBGENRE2_CHOISES)


class Habit(models.Model):
    motivation = models.IntegerField(null=True, blank=True)
    frequency = models.IntegerField(null=True, blank=True)
    division = models.CharField(blank=True, max_length=100)
    number = models.IntegerField(null=True, blank=True)
    habitgenre1 = models.CharField(blank=True, max_length=100)
    habit = models.TextField()
    habitmemo = models.TextField(blank=True)
    done1 = models.BooleanField(blank=True)
    done2 = models.BooleanField(blank=True)
    done3 = models.BooleanField(blank=True)
    done4 = models.BooleanField(blank=True)
    review = models.IntegerField(blank=True)
    completiondate = models.DateField(blank=True)

    habitflag = models.BooleanField(null=True, blank=True, default=False)

    probgenre1 = models.CharField(blank=True, max_length=100)
    probgenre2 = models.CharField(blank=True, max_length=100)
    problem = models.TextField(blank=True)
    proburl = models.TextField(blank=True)
    probmemo = models.TextField(blank=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        db_table = "habit"
