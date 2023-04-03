import graphene
import api.apps.projects.gql.schema as project 
import api.microapps.stickynotes.gql.schema as note




class Query(project.Query, note.Query):
    pass

class Mutation(project.Mutation, note.Mutation):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)