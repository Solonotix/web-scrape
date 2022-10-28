from dataclasses import dataclass
from datetime import datetime
from typing import Tuple
from urllib.parse import parse_qs, urlparse

from bs4 import Tag


@dataclass
class PrecipitationRecord(object):
    county: str
    gauge_catch: float
    is_trace: bool
    observed: datetime
    latitude: float
    longitude: float
    snowfall_depth: float
    # Water-equivalent depth
    snowfall_liquid: float
    snowfall_ratio: float
    # Percent liquid in snowpack
    snowpack_density: float
    snowpack_depth: float
    # Water-equivalent depth
    snowpack_liquid: float
    state: str
    station_name: str
    station_num: str

    @classmethod
    def from_tr(cls, tr: Tag) -> 'PrecipitationRecord':
        _date, _time, _num, _name, _gauge, _snowfall, _snowpack, state, county, _, _maps = tr.find_all('td')
        _sp_depth, _sp_liquid, _sp_density = _snowpack.find_all('span')

        is_trace, gauge = cls.derive_gauge(_gauge)
        latitude, longitude = cls.url_to_location(_maps.a['href'])
        observed = cls.derive_datetime(_date, _time)
        snowfall_depth, snowfall_liquid, snowfall_ratio = cls.derive_snowfall(_snowfall)
        snowpack_depth, snowpack_liquid, snowpack_density = cls.derive_snowpack(_snowpack)

        return cls(county, gauge, is_trace, observed, latitude, longitude, snowfall_depth, snowfall_liquid,
                   snowfall_ratio, snowpack_density, snowpack_depth, snowpack_liquid, state, _name, _num)

    @staticmethod
    def derive_datetime(_date: Tag, _time: Tag) -> datetime:
        return datetime.strptime(f'{_date.text} {_time.text}', '%m/%d/%Y %I:%M %p')

    @staticmethod
    def derive_gauge(_gauge: Tag) -> Tuple[bool, float]:
        is_trace = _gauge.text.upper() == 'T'
        return is_trace, 0.0 if is_trace else float(_gauge.text)

    @staticmethod
    def derive_snowfall(snowfall: Tag) -> Tuple[float, float, float]:
        sf_depth, sf_liquid, sf_ratio = map(lambda t: t.text.upper(), snowfall.find_all('span'))
        depth = None if sf_depth == 'NA' else float(sf_depth)
        liquid = None if sf_liquid == 'NA' else float(sf_liquid)
        ratio = round(depth / liquid, 1) if depth and liquid else None

        return depth, liquid, ratio

    @staticmethod
    def derive_snowpack(snowpack: Tag) -> Tuple[float, float, float]:
        sp_depth, sp_liquid, sp_ratio = map(lambda t: t.text.upper(), snowpack.find_all('span'))
        depth = None if sp_depth == 'NA' else float(sp_depth)
        liquid = None if sp_liquid == 'NA' else float(sp_liquid)
        density = round(liquid / depth, 2) if depth and liquid else None

        return depth, liquid, density

    @staticmethod
    def url_to_location(href: str) -> Tuple[float, float]:
        url = urlparse(href)
        query = parse_qs(url.query)
        center = query.get('center', []).pop()
        latitude, longitude = center.split(',')

        return float(latitude), float(longitude)
