from inspect import isclass
import os, re, django
from django.db.models.fields.related import ForeignKey, ManyToOneRel, ManyToManyRel
from django.db.models.fields import IntegerField, CharField, FloatField, TextField, DecimalField, DateField, DateTimeField, BooleanField, TimeField
from django.db.models.fields.json import JSONField
import graphql_relay
import random
import string
import datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
django.setup()

from lebedoo import models

exceptions = ["Users"]
insert_values = {}
insert_items = []
update_values = {}
update_items = []
exceptions_insert_fields = ['is_active', 'is_deleted', 'created_at', 'updated_at', 'deleted_at', 'created_date', 'updated_date']
exceptions_update_fields = ['created_at', 'updated_at', 'deleted_at', 'deleted_at', 'created_date', 'updated_date']
folder_name = 'rent'

tables = [(model, getattr(models, model)) for model in dir(models) if isclass(getattr(models, model))]

for table in tables:
    print("********************************************************************************")
    if table[0] not in exceptions:
        pass
    else:
        table_name = table[0]
        table_instance = table[1]
        print(f"""processing {table_name}...""")
        alter = re.findall('[A-Z][^A-Z]*', table[0])
        final_word = ''
        for index, word in enumerate(alter):
            if index+1 != len(alter):
                final_word = final_word + word.lower() + '_'
            else:
                final_word = final_word + word.lower()
        
        dir_name = folder_name+"//"+final_word
            # file_name = current_time + ".log"
        try:
        # Create target Directory
            os.makedirs(dir_name)
        except FileExistsError:
            pass
        
        # Create types.py files *************************************** CREATE A "types.py" FILE *******************************************************************************
        open(folder_name+"//"+final_word + "//" + "types.py", "w").close()
        types = open(folder_name+"//"+final_word + "//" + "types.py", "a")

        open(folder_name+"//"+final_word + "//" +"mutations.py", "w").close()
        mutations = open(folder_name+"//"+final_word + "//" + "mutations.py", "a")

        queries = open(folder_name+"//"+final_word + "//" + "queries.py", "w+")

        open(folder_name+"//"+final_word + "//" + "tests.py", "w")
        tests = open(folder_name+"//"+final_word + "//" + "tests.py", "a")

        tests = open(folder_name + "//" + final_word + "//" + "tests.py", "r+")
        





        # ****************************** Generate types.py ************************************************

        print(f"""Create types.py and {table_name}Type class...""")
        types.write(f"""from .. import models as models
from graphene_django.types import DjangoObjectType
import graphene
import django_filters

""")    
        

        types.write(f"""
# use it in your type.py file like following :
# from .{final_word}.types import {table_name}Type, {table_name}Filter

class {table_name}Filter(django_filters.FilterSet):
    # order_by = django_filters.OrderingFilter(
    #     fields=(
    #         ('expirydate', "created_at"),
    #     )
    # )  
    class Meta:
        model = models.{table_name}
        fields = {{field.name:['exact'] for field in models.{table_name}._meta.fields}}
    
        """)
        exclude = []
        for field in table_instance._meta.get_fields():
            if isinstance(field, JSONField):
                exclude.append(field.name)

        if exclude != []:
            types.write(f"""exclude = {exclude}
            """)

        types.write(f"""
class {table_name}Type(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = models.{table_name}
        filterset_class = {table_name}Filter
        interfaces = (graphene.relay.Node,)
            """)


        print(f"""types.py and {table_name}Type class created successfully...""")




















        # ****************************** Generate mutations.py -- InsertMutation ************************************************
        print(f"""Create mutations.py and Insert{table_name}...""")
        mutations.write(f"""import graphene
from .. import models as models
from .. import types as types
from graphql_relay import from_global_id
        """
        )

        mutations.write(f"""
# use it in your schema like following:
# from .{final_word}.types import {table_name}Type, {table_name}Filter 
# from .{final_word} import queries as {final_word}_queries, mutations as {final_word}_mutations       
#    create_{final_word} = {final_word}_mutations.Insert{table_name}.Field()
#    update_{final_word} = {final_word}_mutations.Update{table_name}.Field()
#    {final_word}_queries.{table_name}Query,


# 
# ********************* insertion class *********************
class Insert{table_name}(graphene.Mutation):
    success = graphene.Boolean()
    {final_word} = graphene.Field(types.{table_name}Type)
    errors = graphene.String()

    class Arguments:
""")
        for field in table_instance._meta.get_fields():
            print(field)
            try:
                name = field.name.split('_')[0]
                for item in field.name.split('_')[1:]:
                    name += item.capitalize()
            except:
                name = field.name
            if field.name not in exceptions_insert_fields:
                if isinstance(field, ManyToManyRel):
                    mutations.write(f"""
        {field.name} = graphene.ID(required=True)
                    """)

                elif isinstance(field, ManyToOneRel):
                    pass

                elif field.primary_key:   
                    if table_name == 'Users':
                        insert_items.append(name+":"+'""')
                        mutations.write(f"""
        {field.name} = graphene.ID(required=True)
                    """)

                elif isinstance(field, ForeignKey):
                    try:
                        print("random",random.choice(field.related_model.objects.all()).id)
                        insert_values[name] = str(random.choice(field.related_model.objects.all()).id)
                        # insert_values[name] = str(graphql_relay.to_global_id(type_=f'{table_name}Type', id_=random.choice(field.related_model.objects.all()).id))
                        insert_items.append(name+":"+'"'+insert_values[name]+'"')
                    except:
                        insert_items.append(name+":"+"")
                    mutations.write(f"""
        {field.name} = graphene.ID(required=True)
                    """)
                elif isinstance(field, JSONField):
                    if field.name == 'privileges':
                        print("json")
                        insert_values[name] = '""{"role":"state"}""'
                        insert_items.append(name+":"+'"'+insert_values[name]+'"')
                    else:
                        insert_values[name] = '""{"key":"value"}""'
                        insert_items.append(name+":"+insert_values[name])
                    mutations.write(f"""
        {field.name} = graphene.JSONString(required=True)
                    """)
                elif type(field) in [CharField, TextField]:
                    insert_values[name] = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
                    insert_items.append(name+":"+'"'+insert_values[name]+'"')
                    mutations.write(f"""
        {field.name} = graphene.String()
                    """)
                elif isinstance(field, IntegerField):
                    insert_values[name] = str(random.randint(0, 100000))
                    insert_items.append(name+":"+insert_values[name])
                    mutations.write(f"""
        {field.name} = graphene.Int()
                    """)
                elif isinstance(field, FloatField):
                    insert_values[name] = str(random.random())
                    insert_items.append(name+":"+insert_values[name])
                    
                    mutations.write(f"""
        {field.name} = graphene.Float()
                    """)
                elif isinstance(field, DecimalField):
                    insert_values[name] = str(random.random())
                    insert_items.append(name+":"+insert_values[name])
                    mutations.write(f"""
        {field.name} = graphene.Decimal()
                    """)
                elif isinstance(field, DateField):
                    start_date = datetime.date(2022, 1, 1)
                    end_date = datetime.date(2024, 1, 1)
                    time_between_dates = end_date - start_date
                    days_between_dates = time_between_dates.days
                    random_number_of_days = random.randrange(days_between_dates)
                    random_date = start_date + datetime.timedelta(days=random_number_of_days)
                    insert_values[name] = str(random_date)
                    insert_items.append(name+":"+'"'+insert_values[name]+'"')
                    mutations.write(f"""
        {field.name} = graphene.Date()
                    """)
                elif isinstance(field, DateTimeField):
                    insert_values[name] = str(datetime.datetime.now())
                    insert_items.append(name+":"+insert_values[name])
                    mutations.write(f"""
        {field.name} = graphene.DateTime()
                    """)
                elif isinstance(field, BooleanField):
                    insert_values[name] = str(random.choice(['true', 'false']))
                    insert_items.append(name+":"+insert_values[name])
                    mutations.write(f"""
        {field.name} = graphene.Boolean()
                    """)
                elif isinstance(field, TimeField):
                    insert_values[name] = str(datetime.datetime.now().time())
                    insert_items.append(name+":"+'"'+insert_values[name]+'"')
                    mutations.write(f"""
        {field.name} = graphene.Time()
                    """)
        description = """'''        
> mutation{
        """
        tests.write(f"""#Mutation test request
        
        """)
        tests.write("""        
'''        
mutation{
        """)

        # ********************* Mutation insert request
        arguments=f"""> create{table_name}{tuple(insert_items)}
        """
        description += arguments.replace("'","")
        description += "> {"
        tests.write(f"""{arguments.replace("'","")}
            """)
        tests.write("{")
        try:
            name = final_word.split('_')[0]
            for item in final_word.split('_')[1:]:
                name += item.capitalize()
        except:
            name = final_word
        description += f"""
>                success
>                errors
>                {name}   
        """ 
        tests.write(f"""
                success
                errors
                {name}   
        """)
        tests.write("                {")
        description += ">             {"
        for field in table_instance._meta.get_fields():
            try:
                name = field.name.split('_')[0]
                for item in field.name.split('_')[1:]:
                    name += item.capitalize()
            except:
                name = field.name
            if isinstance(field, ForeignKey):
                tests.write(f""" 
                            {name} 
                                {{
                                    id
                                }}
                            """)

                description += f""" 
>                            {name} 
>                                {{
>                                    id
>                                }}"""
            else:
                if isinstance(field, ManyToOneRel) == False:
                    tests.write(f""" 
                                {name}""")
                    description += f""" 
>                                {name}"""
        tests.write("""
        }
    }
}
        """)
        description += """
>       }
>    }
> }
''' 
        """

        tests.write("""
'''        
        """)

        mutations.write(f"""
    class Meta:
        description = {description}
        """)
        mutations.write(f"""
    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
        """)
        pk = ''
        for field in table_instance._meta.get_fields():
            if field.name not in exceptions_insert_fields:
                if isinstance(field, ManyToManyRel):
                    mutations.write(f"""
        {field.name} = graphene.ID(required=True)
                    """)
                elif isinstance(field, ManyToOneRel):
                    pass
                elif field.primary_key:
                    pk = field
                elif isinstance(field, ForeignKey):
                    print("************************************************")
                    id = field.related_model._meta.pk.name
                    model_name = field.related_model._meta.object_name
                    
                    mutations.write(f"""
            kwargs['{field.name}'] = models.{model_name}.objects.get({id}=kwargs['{field.name}'])
                    """)
        mutations.write(f"""
            models.{table_name}.objects.create(**kwargs)
            return Insert{table_name}({final_word}=models.{table_name}.objects.filter(**kwargs).all().latest('{pk.name}'), success=True)
                    """)
        mutations.write(f"""
        except Exception as error:
            return Insert{table_name}(errors=error, success=False)
        """)

#         tests.write(f"""#Mutation test request
        
#         """)
#         tests.write("""
# '''        
# mutation{
#         """)

#         # ********************* Mutation insert request

#         arguments=f"""
#     insert{table_name}{tuple(insert_items)}
#         """
#         tests.write(f"""{arguments.replace("'","")}
#             """)
#         tests.write("{")
#         try:
#             name = final_word.split('_')[0]
#             for item in final_word.split('_')[1:]:
#                 name += item.capitalize()
#         except:
#             name = final_word
#         tests.write(f"""
#                 success
#                 errors
#                 {name}   
#         """)
#         tests.write("                {")
#         for field in table_instance._meta.get_fields():
#             try:
#                 name = field.name.split('_')[0]
#                 for item in field.name.split('_')[1:]:
#                     name += item.capitalize()
#             except:
#                 name = field.name
#             if isinstance(field, ForeignKey):
#                 tests.write(f""" 
#                             {name} 
#                                 {{
#                                     id
#                                 }}
#                             """)
#             else:
#                 if isinstance(field, ManyToOneRel) == False:
#                     tests.write(f""" 
#                                 {name}""")


#         tests.write("""
#         }
#     }
# }
#         """)

#         tests.write("""
# '''        
#         """)
        





        # ****************************** Generate mutations.py -- UpdateMutation ************************************************
        mutations.write(f"""


        """)
        mutations.write(f"""
# ********************* update class *********************
class Update{table_name}(graphene.Mutation):
    success = graphene.Boolean()
    {final_word} = graphene.Field(types.{table_name}Type)
    errors = graphene.String()

    class Arguments:
""")
        for field in table_instance._meta.get_fields():
            try:
                name = field.name.split('_')[0]
                for item in field.name.split('_')[1:]:
                    name += item.capitalize()
            except:
                name = field.name

            if field.name not in exceptions_update_fields:
                if isinstance(field, ManyToManyRel):
                    mutations.write(f"""
        {field.name} = graphene.ID(required=True)
                    """)
                elif isinstance(field, ManyToOneRel):
                    pass
                elif field.primary_key:
                    print(name, "pkkkkkkkkkkkk", field.model.objects.all())
                    try:
                        update_values[name] = str(graphql_relay.to_global_id(type_=f'{table_name}Type', id_=random.choice(field.model.objects.all()).id))
                    except:
                        update_values[name] = ""

                    update_items.append(name+":"+'"'+update_values[name]+'"')
                    mutations.write(f"""
        {field.name} = graphene.ID(required=True)
                    """)
                elif isinstance(field, ForeignKey):
                    try:
                        update_values[name] = str(graphql_relay.to_global_id(type_=f'{table_name}Type', id_=random.choice(field.related_model.objects.all()).id))
                        update_items.append(name+":"+'"'+update_items[name]+'"')
                    except:
                        update_items.append(name+":"+"")
                    mutations.write(f"""
        {field.name} = graphene.ID(required=True)
                    """)
                elif isinstance(field, JSONField):
                    if field.name == 'privileges':
                        update_values[name] = """{"role":"state"}"""
                        update_items.append(name+":"+update_values[name])
                        mutations.write(f"""
        {field.name} = graphene.JSONString(required=True)
                    """)
                    else:
                        update_values[name] = """{"key":"value"}"""
                        update_items.append(name+":"+update_values[name])
                        mutations.write(f"""
        {field.name} = graphene.JSONString()
                    """)
                elif type(field) in [CharField, TextField]:
                    update_values[name] = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
                    update_items.append(name+":"+'"'+update_values[name]+'"')
                    mutations.write(f"""
        {field.name} = graphene.String()
                    """)
                elif isinstance(field, IntegerField):
                    update_values[name] = str(random.randint(0, 100000))
                    update_items.append(name+":"+update_values[name])
                    mutations.write(f"""
        {field.name} = graphene.Int()
                    """)
                elif isinstance(field, FloatField):
                    update_values[name] = str(random.random())
                    update_items.append(name+":"+update_values[name])
                    
                    mutations.write(f"""
        {field.name} = graphene.Float()
                    """)
                elif isinstance(field, DecimalField):
                    update_values[name] = str(random.random())
                    update_items.append(name+":"+update_values[name])
                    mutations.write(f"""
        {field.name} = graphene.Decimal()
                    """)
                elif isinstance(field, DateField):
                    start_date = datetime.date(2022, 1, 1)
                    end_date = datetime.date(2024, 1, 1)
                    time_between_dates = end_date - start_date
                    days_between_dates = time_between_dates.days
                    random_number_of_days = random.randrange(days_between_dates)
                    random_date = start_date + datetime.timedelta(days=random_number_of_days)
                    update_values[name] = str(random_date)
                    update_items.append(name+":"+'"'+update_values[name]+'"')
                    mutations.write(f"""
        {field.name} = graphene.Date()
                    """)
                elif isinstance(field, DateTimeField):
                    update_values[name] = str(datetime.datetime.now() )
                    update_items.append(name+":"+update_values[name])
                    mutations.write(f"""
        {field.name} = graphene.DateTime()
                    """)
                elif isinstance(field, BooleanField):
                    update_values[name] = str(random.choice(['true', 'false']))
                    update_items.append(name+":"+update_values[name])
                    mutations.write(f"""
        {field.name} = graphene.Boolean()
                    """)
                elif isinstance(field, TimeField):
                    update_values[name] = str(datetime.datetime.now().time())
                    update_items.append(name+":"+'"'+update_values[name]+'"')
                    mutations.write(f"""
        {field.name} = graphene.Time()
                    """)

        description = """'''        
> mutation{
        """
        tests.write(f"""#Mutation test request
        
        """)
        tests.write(f"""
#*****************************************************Mutation test request************************************************        
        """)
        tests.write("""
'''        
mutation{
        """)
        
        arguments=f"""
>    update{table_name}{tuple(update_items)}"""
        description += arguments.replace("'","")
        tests.write(f"""{arguments.replace("'","")}
            """)
        try:
            name1 = final_word.split('_')[0]
            for item in final_word.split('_')[1:]:
                name1 += item.capitalize()
        except:
            name1 = final_word
        tests.write("{")
        tests.write(f"""
                success
                errors
                {name1}   
        """)
        description += "{"
        description += f"""
>                success
>                errors
>                {name1}   
        """
        description += ">            {"
        tests.write("                {")
        for field in table_instance._meta.get_fields():
            try:
                name = field.name.split('_')[0]
                for item in field.name.split('_')[1:]:
                    name += item.capitalize()
            except:
                name = field.name
            if isinstance(field, ForeignKey):
                tests.write(f""" 
                            {name} 
                                {{
>                                    id
                                }}
                            """)
                description += f""" 
                            {name} 
                                {{
>                                    id
                                }}"""
            else:
                 if isinstance(field, ManyToOneRel) == False:
                    tests.write(f""" 
                                {name}""")
                    description += f""" 
                            >    {name}"""

        tests.write("""
        }
    }
}
        """)
        description+= """
>        }
>    }
> }''' """

        tests.write("""
'''        
        """)


        mutations.write(f"""
    class Meta:
        description = {description}
        """)
        mutations.write(f"""
    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
        """)
        pk = ''
        for field in table_instance._meta.get_fields():
            if field.name not in exceptions_insert_fields:
                if isinstance(field, ManyToManyRel):
                    mutations.write(f"""
        {field.name} = graphene.ID(required=True)
                    """)
                elif isinstance(field, ManyToOneRel):
   
                    pass
                elif field.primary_key:
                    pk = field
                    mutations.write(f"""
            kwargs['{field.name}'] = models.{table_name}.objects.get({pk.name}=kwargs['{field.name}']).id
                    """)
                if isinstance(field, ForeignKey):
                    id = field.related_model._meta.pk.name
                    model_name = field.related_model._meta.object_name
                    
                    mutations.write(f"""
            kwargs['{field.name}'] = models.{model_name}.objects.get({id}=kwargs['{field.name}']).id
                    """)
        mutations.write(f"""
            models.{table_name}.objects.filter({pk.name}=kwargs['{pk.name}']).update(**kwargs)
            return Update{table_name}({final_word}=models.{table_name}.objects.filter(**kwargs).all().latest('{pk.name}'), success=True)
                    """)
        mutations.write(f"""
        except Exception as error:
            return Update{table_name}(errors=error, success=False)
        """)

#         tests.write(f"""#Mutation test request
        
#         """)
#         tests.write(f"""
# #*****************************************************Mutation test request************************************************        
#         """)
#         tests.write("""
# '''        
# mutation{
#         """)
#         arguments=f"""
#     update{table_name}{tuple(update_items)}
#         """
#         tests.write(f"""{arguments.replace("'","")}
#             """)
#         try:
#             name1 = final_word.split('_')[0]
#             for item in final_word.split('_')[1:]:
#                 name1 += item.capitalize()
#         except:
#             name1 = final_word
#         tests.write("{")
#         tests.write(f"""
#                 success
#                 errors
#                 {name1}   
#         """)
#         tests.write("                {")
#         for field in table_instance._meta.get_fields():
#             try:
#                 name = field.name.split('_')[0]
#                 for item in field.name.split('_')[1:]:
#                     name += item.capitalize()
#             except:
#                 name = field.name
#             if isinstance(field, ForeignKey):
#                 tests.write(f""" 
#                             {name} 
#                                 {{
#                                     id
#                                 }}
#                             """)
#             else:
#                  if isinstance(field, ManyToOneRel) == False:
#                     tests.write(f""" 
#                                 {name}""")

#         tests.write("""
#         }
#     }
# }
#         """)

#         tests.write("""
# '''        
#         """)





        ### Generate queries.py
        queries.write(f"""import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .. import types as types
from .. import models as models

""")

        queries.write(f"""
# use it in your schema like following:
# from .{final_word} import queries as {final_word}_queries
# {final_word}_queries.{table_name}Query,

class {table_name}Query(graphene.ObjectType):
        """)

        queries.write(f"""
    {table_name}Node = DjangoFilterConnectionField(types.{table_name}Type, filterset_class=types.{table_name}Filter)
    def resolve_{table_name}Node(self, info, **kwargs):
        pass
            """)

        queries.write(f"""
    {table_name}By_id = graphene.Field(types.{table_name}Type, id=graphene.ID(required=True))
    def resolve_{table_name}By_id(self, info, **kwargs):
        return models.{table_name}.objects.get(**kwargs)
            """)

