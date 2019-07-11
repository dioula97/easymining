# -*- coding: utf-8 -*-

from odoo import models, fields, api

class site(models.Model):
    _name = 'easymining.site'

    name = fields.Char('Nom')
    description = fields.Text('Description')
    localisation = fields.Char('Localisation')
    attachment_ids = fields.Many2many('ir.attachment', 'easymining_site_ir_attachments_rel', 'easymining_site_id', 'attachment_id', 'Pièces jointes')
    longueur = fields.Integer('Longueur')
    largeur = fields.Integer('Largeur')
    profondeur = fields.Integer('Profondeur')
    # volume_estime = fields.Float()
    minerai_ids = fields.Many2many('product.template', 'easymining_site_product_template_rel', 'easymining_site_id', 'product_template_id', 'Minerais')
    # capacite_theorique_globale = fields.Float()
    # capacite_theorique_restante = fields.Float()
    # capacite_extraite = fields.Float()
    date_ouverture = fields.Date('Date d\'Ouverture')
    date_fermeture = fields.Date('Date de fermeture')

    opminage_ids = fields.One2many('easymining.opminage', 'site_id', string="Operations de minage")


class opminage(models.Model):
    _name = 'easymining.opminage'

    name = fields.Char('Nom de l\'operation')
    date = fields.Date('Date de l\'operation')
    site_id = fields.Many2one('easymining.site', string="Site")
    minerai_ids = fields.Many2many('product.template', 'easymining_opminage_product_template_rel', 'easymining_opminage_id', 'product_template_id', string="Minerais utilises")
    prestataire_id = fields.Many2one('res.partner', string="Prestataire")
    commentaire = fields.Text()
    pourcentage = fields.Integer()



