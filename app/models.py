from django.db import models


class CadDistritos(models.Model):
    iddistrito = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=45)
    sigla = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'cad_distritos'


class CadEscolas(models.Model):
    idescola = models.CharField(primary_key=True, max_length=8)
    nome = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=14, blank=True, null=True)
    idmunicipio = models.ForeignKey('CadMunicipios', models.DO_NOTHING, db_column='idmunicipio')
    restricao = models.IntegerField()
    local = models.IntegerField()
    categoria = models.IntegerField()
    dependencia = models.IntegerField()
    conveniada = models.BooleanField()
    regular = models.BooleanField(blank=True, null=True)
    ativo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cad_escolas'
        
class EscolaView(models.Model):
    idescola = models.CharField(primary_key=True, max_length=8)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=14, null=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=10)
    local = models.CharField(max_length=45)
    categoria = models.CharField(max_length=45)
    ideb23 = models.FloatField(null=True)
    ativo = models.BooleanField()
    idestado = models.IntegerField()
    idcidade = models.CharField(max_length=7)
    idlocal = models.IntegerField()
    idcategoria = models.IntegerField()

    class Meta:
        managed = False
        db_table = "vw_escolas"


class CadEscolasIdeb(models.Model):
    idescola = models.ForeignKey(CadEscolas, models.DO_NOTHING, db_column='idescola')
    a2017 = models.DecimalField(max_digits=10, decimal_places=2)
    a2019 = models.DecimalField(max_digits=10, decimal_places=2)
    a2021 = models.DecimalField(max_digits=10, decimal_places=2)
    a2023 = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'cad_escolas_ideb'


class CadEscolasIndicadores(models.Model):
    idescola = models.ForeignKey(CadEscolas, models.DO_NOTHING, db_column='idescola')
    ano = models.SmallIntegerField()
    tipo = models.IntegerField(db_comment='0 = Abandono, 1 = Aprovação')
    fundamental = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, db_comment='Taxa Média')
    medio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, db_comment='Taxa Média')

    class Meta:
        managed = False
        db_table = 'cad_escolas_indicadores'


class CadEscolasIndicadoresAnalitico(models.Model):
    idescola = models.ForeignKey(CadEscolas, models.DO_NOTHING, db_column='idescola')
    ano = models.SmallIntegerField()
    tipo = models.IntegerField()
    f1 = models.DecimalField(max_digits=10, decimal_places=2)
    f2 = models.DecimalField(max_digits=10, decimal_places=2)
    f3 = models.DecimalField(max_digits=10, decimal_places=2)
    f4 = models.DecimalField(max_digits=10, decimal_places=2)
    f5 = models.DecimalField(max_digits=10, decimal_places=2)
    f6 = models.DecimalField(max_digits=10, decimal_places=2)
    f7 = models.DecimalField(max_digits=10, decimal_places=2)
    f8 = models.DecimalField(max_digits=10, decimal_places=2)
    f9 = models.DecimalField(max_digits=10, decimal_places=2)
    m1 = models.DecimalField(max_digits=10, decimal_places=2)
    m2 = models.DecimalField(max_digits=10, decimal_places=2)
    m3 = models.DecimalField(max_digits=10, decimal_places=2)
    idmunicipio = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_escolas_indicadores_analitico'


class CadEscolasInfraestrutura(models.Model):
    idescola = models.ForeignKey(CadEscolas, models.DO_NOTHING, db_column='idescola')
    ano = models.SmallIntegerField()
    idlayout = models.ForeignKey('CadLayouts', models.DO_NOTHING, db_column='idlayout')
    cols = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_escolas_infraestrutura'


class CadEscolasModalidades(models.Model):
    idescola = models.ForeignKey(CadEscolas, models.DO_NOTHING, db_column='idescola')
    infantil = models.BooleanField(blank=True, null=True)
    fundamental = models.BooleanField(blank=True, null=True)
    medio = models.BooleanField(blank=True, null=True)
    adultos = models.BooleanField(blank=True, null=True)
    profissional = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_escolas_modalidades'


class CadGrupos(models.Model):
    idgrupo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    tipo = models.IntegerField()
    descricao = models.CharField(max_length=100, blank=True, null=True)
    ativo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cad_grupos'


class CadGruposPermissoes(models.Model):
    idgrupo = models.ForeignKey(CadGrupos, models.DO_NOTHING, db_column='idgrupo')
    idpermissao = models.ForeignKey('CadPermissoes', models.DO_NOTHING, db_column='idpermissao')

    class Meta:
        managed = False
        db_table = 'cad_grupos_permissoes'


class CadLayouts(models.Model):
    idlayout = models.AutoField(primary_key=True)
    grupo = models.IntegerField()
    caminho = models.CharField(max_length=100)
    descricao = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_layouts'


class CadMunicipios(models.Model):
    idmunicipio = models.CharField(primary_key=True, max_length=7)
    nome = models.CharField(max_length=45)
    iddistrito = models.ForeignKey(CadDistritos, models.DO_NOTHING, db_column='iddistrito')

    class Meta:
        managed = False
        db_table = 'cad_municipios'


class CadMunicipiosIndicadores(models.Model):
    idmunicipio = models.ForeignKey(CadMunicipios, models.DO_NOTHING, db_column='idmunicipio')
    ano = models.SmallIntegerField()
    qtdmatriculas = models.IntegerField(blank=True, null=True)
    qtdescolas = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_municipios_indicadores'


class CadMunicipiosIndicadoresAnalitico(models.Model):
    idmunicipio = models.ForeignKey(CadMunicipios, models.DO_NOTHING, db_column='idmunicipio')
    ano = models.SmallIntegerField()
    tipo = models.CharField(max_length=1)
    local = models.IntegerField()
    modalidade = models.IntegerField()
    federal = models.IntegerField(blank=True, null=True)
    estadual = models.IntegerField(blank=True, null=True)
    municipal = models.IntegerField(blank=True, null=True)
    privada = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_municipios_indicadores_analitico'


class CadPermissoes(models.Model):
    idpermissao = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    caminho = models.TextField(blank=True, null=True)
    tipo = models.IntegerField()
    rota = models.CharField(max_length=255, blank=True, null=True)
    idpai = models.IntegerField(blank=True, null=True)
    icone = models.CharField(max_length=45, blank=True, null=True)
    ordem = models.IntegerField(blank=True, null=True)
    ativo = models.BooleanField()
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_permissoes'


class CadTipos(models.Model):
    categoria = models.IntegerField()
    cod = models.IntegerField(blank=True, null=True)
    descricao = models.CharField(max_length=45)
    campo = models.CharField(max_length=45, blank=True, null=True)
    ordem = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cad_tipos'


class CadUsuarios(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=60)
    cpf = models.CharField(max_length=11)
    datanascimento = models.DateField()
    email = models.CharField(max_length=255)
    idmunicipio = models.ForeignKey(CadMunicipios, models.DO_NOTHING, db_column='idmunicipio')
    tokensenha = models.CharField(max_length=50, blank=True, null=True)
    ativo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cad_usuarios'


class CadUsuariosGrupos(models.Model):
    idusuario = models.ForeignKey(CadUsuarios, models.DO_NOTHING, db_column='idusuario')
    idgrupo = models.ForeignKey(CadGrupos, models.DO_NOTHING, db_column='idgrupo')

    class Meta:
        managed = False
        db_table = 'cad_usuarios_grupos'


class CadUsuariosPermissoes(models.Model):
    cad_usuarios_idusuario = models.ForeignKey(CadUsuarios, models.DO_NOTHING, db_column='cad_usuarios_idusuario')
    idpermissao = models.ForeignKey(CadPermissoes, models.DO_NOTHING, db_column='idpermissao')
    ativo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cad_usuarios_permissoes'
