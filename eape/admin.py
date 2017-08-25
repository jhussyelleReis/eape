from django.contrib import admin
from .models import Aluno, Curso, Turma, Pagamento

# Register your models here

class CursoAdmin(admin.ModelAdmin):
    model = Curso
    list_display = ('nome','descricao')

class TurmaAdmin(admin.ModelAdmin):
    model = Turma
    list_display = ('nome','diasDaSemana','horario','curso')

class AlunoAdmin(admin.ModelAdmin):
    model = Aluno
    list_display = ('nome','matricula','turma')

class PagamentoAdmin(admin.ModelAdmin):
    model = Pagamento
    list_display = ('aluno','turma','data_realizacao','valor')


admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Pagamento, PagamentoAdmin)

