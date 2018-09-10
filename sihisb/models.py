from django.db import models
from sihisb import domains

# Create your models here.
from django.db.models import ForeignKey


class Domain(models.Model):
    nm_domain = models.CharField(max_length=75)
    ds_domain = models.CharField(max_length=300)

    def __str__(self):
        return self.nm_domain


class DomainValue(models.Model):
    id_domain_fk = models.ForeignKey(Domain, on_delete=models.CASCADE)
    vl_domain = models.CharField(max_length=25)          # Valor do Domínio
    ds_vl_domain = models.CharField(max_length=300)         # ToolTip

    def __str__(self):
        return self.vl_domain


class Assentamento(models.Model):           # Caracterização
    id_funep = models.PositiveSmallIntegerField
    nm_area = models.CharField(max_length=100)
    id_sehab = models.PositiveSmallIntegerField
    ds_regiao_op = models.CharField(max_length=5)
    dm_tipologia = models.ForeignKey(
        DomainValue,
        limit_choices_to={'id_domain_fk': domains.TIPOLOGIA},     # Domain.id com nm_domain = tipologia...
        on_delete=models.SET_NULL
    )
    """
    @property
    def _tipologia(self):
        return DomainValue(self.dm_tipologia)

    ds_tipologia = property(_tipologia)
    """
    dm_vulnerabilidade = models.ForeignKey(
        DomainValue,
        limit_choices_to={'id_domain_fk': domains.VULNERABILIDADE},     # Domain.id com nm_domain = vulnerabilidade...
        on_delete=models.SET_NULL
    )
    ds_localizacao = models.CharField(max_length=100)
    vl_uhs_mapeadas = models.PositiveIntegerField

    @property
    def _uhs_calc(self):
        return round(self.vl_uhs_mapeadas * 1.05)

    vl_uhs_calc = property(_uhs_calc)
    vl_unid_cad = models.PositiveIntegerField
    sn_manancial = models.BooleanField
    sn_projeto = models.BooleanField
    dm_tp_assentamento = models.ForeignKey(
        DomainValue,
        limit_choices_to={'id_domain_fk': domains.ASSENTAMENTO},
        on_delete=models.SET_NULL
    )
    dm_situ_propriedade = models.ManyToManyField(
        DomainValue,
        limit_choices_to={'id_domain_fk': domains.SITUA_PROPRIEDADE}
    )
    tx_obs = models.TextField
    dm_situa_prog = models.ManyToManyField(
        DomainValue,
        limit_choices_to={'id_domain_fk': domains.SITUA_PROG}
    )
    dm_situa_estagio = models.ForeignKey(
        DomainValue,
        limit_choices_to={'id_domain_fk': domains.SITUA_ESTAGIO},
        on_delete=models.SET_NULL
    )
    vl_classifica = models.PositiveSmallIntegerField
    vl_hierarq = models.PositiveSmallIntegerField
    vl_ano_doc = models.PositiveSmallIntegerField
    vl_ano_moradores = models.PositiveSmallIntegerField
    dm_apps = models.ManyToManyField(
        DomainValue,
        limit_choices_to={'id_domain_fk': domains.APPS}
    )
    dm_zoneamento = models.ForeignKey(
        DomainValue,
        limit_choices_to={'id_domain_fk': domains.ZONEAMENTO},
        on_delete=models.SET_NULL
    )
    ds_feicao_morf = models.CharField
    ds_gravames = models.CharField
    tx_obs_jur = models.TextField
    tx_caracteriza = models.TextField
    tx_gps = models.TextField                   #tem algo melhor
    img_fotos = models.ImageField

    def __str__(self):
        return self.nm_area
