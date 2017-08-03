# -*- coding: utf-8 -*-
# This file is part of pygal
#
# A python svg graph plotting library
# Copyright © 2012-2014 Kozea
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pygal. If not, see <http://www.gnu.org/licenses/>.
"""
Spanish departments and regions maps

"""

from __future__ import division
from collections import defaultdict
from pygal.graph.map import BaseMap
from pygal._compat import u
from numbers import Number
import os


DEPARTMENTS = {
    '01': u("Andalucía"),
    '02': u("Cataluña"),
    '03': u("Comunidad de Madrid"),
    '04': u("Comunidad Valenciana"),
    '05': u("Galicia"),
    '06': u("Castilla y León"),
    '07': u("País Vasco"),
    '08': u("Canarias"),
    '09': u("Castilla-La Mancha"),
    '10': u("Región de Murcia"),
    '11': u("Aragón"),
    '12': u("Islas Baleares"),
    '13': u("Extremadura"),
    '14': u("Asturias"),
    '15': u("Navarra"),
    '16': u("Cantabria"),
    '17': u("La Rioja"),
    '18': u("Ceuta"),
    '19': u("Melilla"),
}


REGIONS = {
    '01': u("Álava"),
    '02': u("Albacete"),
    '03': u("Alicante"),
    '04': u("Almería"),
    '05': u("Ávila"),
    '06': u("Badajoz"),
    '07': u("Islas Baleares"),
    '08': u("Barcelona"),
    '09': u("Burgos"),
    '10': u("Cáceres"),
    '11': u("Cádiz"),
    '12': u("Castellón"),
    '13': u("Ciudad Real"),
    '14': u("Córdoba"),
    '15': u("A Coruña"),
    '16': u("Cuenca"),
    '17': u("Girona"),
    '18': u("Granada"),
    '19': u("Guadalajara"),
    '20': u("Gipuzkoa"),
    '21': u("Huelva"),
    '22': u("Huesca"),
    '23': u("Jaén"),
    '24': u("León"),
    '25': u("Lleida"),
    '26': u("La Rioja"),
    '27': u("Lugo"),
    '28': u("Madrid"),
    '29': u("Málaga"),
    '30': u("Murcia"),
    '31': u("Navarra"),
    '32': u("Ourense"),
    '33': u("Asturias"),
    '34': u("Palencia"),
    '35': u("Las Palmas"),
    '36': u("Pontevedra"),
    '37': u("Salamanca"),
    '38': u("Santa Cruz de Tenerife"),
    '39': u("Cantabria"),
    '40': u("Segovia"),
    '41': u("Sevilla"),
    '42': u("Soria"),
    '43': u("Tarragona"),
    '44': u("Teruel"),
    '45': u("Toledo"),
    '46': u("Valencia"),
    '47': u("Valladolid"),
    '48': u("Bizkaia"),
    '49': u("Zamora"),
    '50': u("Zaragoza"),
    '51': u("Ceuta"),
    '52': u("Melilla"),
}


with open(os.path.join(
        os.path.dirname(__file__),
        'es.departments.svg')) as file:
    DPT_MAP = file.read()


class IntCodeMixin(object):
    def adapt_code(self, area_code):
        if isinstance(area_code, Number):
            return '%02d' % area_code
        return super(IntCodeMixin, self).adapt_code(area_code)


class Departments(IntCodeMixin, BaseMap):
    """French department map"""
    x_labels = list(DEPARTMENTS.keys())
    area_names = DEPARTMENTS
    area_prefix = 'c'
    kind = 'departement'
    svg_map = DPT_MAP


with open(os.path.join(
        os.path.dirname(__file__),
        'es.regions.svg')) as file:
    REG_MAP = file.read()


class Regions(IntCodeMixin, BaseMap):
    """French regions map"""
    x_labels = list(REGIONS.keys())
    area_names = REGIONS
    area_prefix = 'r'
    svg_map = REG_MAP
    kind = 'region'


DEPARTMENTS_REGIONS = {
    '01': "07",
    '02': "09",
    '03': "04",
    '04': "01",
    '05': "06",
    '06': "13",
    '07': "12",
    '08': "02",
    '09': "06",
    '10': "13",
    '11': "01",
    '12': "04",
    '13': "09",
    '14': "01",
    '15': "05",
    '16': "09",
    '17': "02",
    '18': "01",
    '19': "09",
    '20': "07",
    '21': "01",
    '22': "11",
    '23': "01",
    '24': "06",
    '25': "02",
    '26': "17",
    '27': "05",
    '28': "03",
    '29': "01",
    '30': "10",
    '31': "15",
    '32': "05",
    '33': "14",
    '34': "06",
    '35': "08",
    '36': "05",
    '37': "06",
    '38': "08",
    '39': "16",
    '40': "06",
    '41': "01",
    '42': "06",
    '43': "02",
    '44': "11",
    '45': "09",
    '46': "04",
    '47': "06",
    '48': "07",
    '49': "06",
    '50': "11",
    '51': "18",
    '52': "19",
}


def aggregate_regions(values):
    if isinstance(values, dict):
        values = values.items()
    regions = defaultdict(int)
    for department, value in values:
        regions[DEPARTMENTS_REGIONS[department]] += value
    return list(regions.items())