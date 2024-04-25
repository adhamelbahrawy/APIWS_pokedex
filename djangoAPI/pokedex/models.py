from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EggGroups(models.Model):
    id = models.IntegerField()
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'egg_groups'


class Items(models.Model):
    id = models.IntegerField()
    identifier = models.CharField(max_length=79)
    category_id = models.IntegerField()
    cost = models.IntegerField()
    fling_power = models.IntegerField(blank=True, null=True)
    fling_effect_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'


class Locations(models.Model):
    id = models.IntegerField()
    region_id = models.IntegerField(blank=True, null=True)
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'locations'


class Moves(models.Model):
    id = models.IntegerField()
    identifier = models.CharField(max_length=79)
    generation_id = models.IntegerField()
    type_id = models.IntegerField()
    power = models.SmallIntegerField(blank=True, null=True)
    pp = models.SmallIntegerField(blank=True, null=True)
    accuracy = models.SmallIntegerField(blank=True, null=True)
    priority = models.SmallIntegerField()
    target_id = models.IntegerField()
    damage_class_id = models.IntegerField()
    effect_id = models.IntegerField()
    effect_chance = models.IntegerField(blank=True, null=True)
    contest_type_id = models.IntegerField(blank=True, null=True)
    contest_effect_id = models.IntegerField(blank=True, null=True)
    super_contest_effect_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moves'


class Pokemon(models.Model):
    id = models.IntegerField()
    identifier = models.CharField(max_length=79)
    species_id = models.IntegerField(blank=True, null=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    base_experience = models.IntegerField()
    order = models.IntegerField()
    is_default = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon'


class PokemonEggGroups(models.Model):
    species_id = models.IntegerField()
    egg_group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_egg_groups'


class PokemonFormGenerations(models.Model):
    pokemon_form_id = models.IntegerField()
    generation_id = models.IntegerField()
    game_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_form_generations'


class PokemonMoves(models.Model):
    pokemon_id = models.IntegerField()
    version_group_id = models.IntegerField()
    move_id = models.IntegerField()
    pokemon_move_method_id = models.IntegerField()
    level = models.IntegerField()
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon_moves'


class PokemonStats(models.Model):
    pokemon_id = models.IntegerField()
    stat_id = models.IntegerField()
    base_stat = models.IntegerField()
    effort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_stats'


class PokemonTypes(models.Model):
    pokemon_id = models.IntegerField()
    type_id = models.IntegerField()
    slot = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_types'


class Stats(models.Model):
    id = models.IntegerField()
    damage_class_id = models.IntegerField(blank=True, null=True)
    identifier = models.CharField(max_length=79)
    is_battle_only = models.IntegerField()
    game_index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stats'


class Types(models.Model):
    id = models.IntegerField()
    identifier = models.CharField(max_length=79)
    generation_id = models.IntegerField()
    damage_class_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'types'


class UserPokemon(models.Model):
    user_id = models.IntegerField()
    pokemon_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_pokemon'


class Users(models.Model):
    id = models.IntegerField()
    email = models.CharField(max_length=320)
    identifier = models.CharField(max_length=79)
    password = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'users'