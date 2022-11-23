import graphene
from graphene_django import DjangoObjectType
from .models import UserInfo

class UsersList(DjangoObjectType):
    class Meta:
        model = UserInfo
        fields = ('name', 'email', 'phoneno') #for querying multiple users and display the three fields alone
        # fields = ('id', 'name', 'email', 'phoneno') #used when querying a single user with id

class Query(graphene.ObjectType):

    # listing all created users' info
    list_users = graphene.List(UsersList)   
    def resolve_list_users(root, info):
        return UserInfo.objects.all()

    #listing all created users without all info(remove the email and phone fields, then displays only the names)
    


    #listing a single/particular user
    # singleuser = graphene.Field(UsersList, id=graphene.Int())
    # def resolve_singleuser(root, info, id):
    #     return UserInfo.objects.get(pk=id)
        

class UserInput(graphene.InputObjectType):
    Name = graphene.String()
    Email = graphene.String()
    Phoneno = graphene.Int()


#creating new users
class registerUser(graphene.Mutation):

    class Arguments:
        input = UserInput(required=True)
    
    user = graphene.Field(UsersList)

    @classmethod
    def mutate(cls, root, info, input):
            user = UserInfo()
            user.name = input.Name
            user.email = input.Email
            user.phoneno = input.Phoneno
            user.save()
            return registerUser(user=user)


class Mutation(graphene.ObjectType):
    newuser = registerUser.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)