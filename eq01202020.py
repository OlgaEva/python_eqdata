# JSON with Python
import json

features_string = '''
{
    "type": "FeatureCollection",
    "metadata": {
        "generated": 1579704324000,
        "url": "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2020-01-19&latitude=17.949&longitude=-66.851&maxradiuskm=50",
        "title": "USGS Earthquakes",
        "status": 200,
        "api": "1.8.1",
        "count": 58
    },
    "features": [
        {
            "type": "Feature",
            "properties": {
                "mag": 3.5,
                "place": "12km SSE of Guanica, Puerto Rico",
                "time": 1579578837840,
                "updated": 1579585561628,
                "tz": -240,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2020021002",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=pr2020021002&format=geojson",
                "felt": 3,
                "cdi": 3.3999999999999999,
                "mmi": null,
                "alert": null,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 189,
                "net": "pr",
                "code": "2020021002",
                "ids": ",us60007bv1,pr2020021002,",
                "sources": ",us,pr,",
                "types": ",dyfi,geoserve,origin,phase-data,",
                "nst": 13,
                "dmin": 0.094,
                "rms": 0.19,
                "gap": 229,
                "magType": "md",
                "type": "earthquake",
                "title": "M 3.5 - 12km SSE of Guanica, Puerto Rico"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -66.876099999999994,
                    17.8811,
                    13
                ]
            },
            "id": "pr2020021002"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 3.6000000000000001,
                "place": "2km NNW of Penuelas, Puerto Rico",
                "time": 1579573044690,
                "updated": 1579624474220,
                "tz": -240,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2020021001",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=pr2020021001&format=geojson",
                "felt": 9,
                "cdi": 3.7999999999999998,
                "mmi": null,
                "alert": null,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 203,
                "net": "pr",
                "code": "2020021001",
                "ids": ",us60007bti,pr2020021001,",
                "sources": ",us,pr,",
                "types": ",dyfi,geoserve,origin,phase-data,",
                "nst": 12,
                "dmin": 0.12540000000000001,
                "rms": 0.10000000000000001,
                "gap": 177,
                "magType": "md",
                "type": "earthquake",
                "title": "M 3.6 - 2km NNW of Penuelas, Puerto Rico"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -66.727999999999994,
                    18.012799999999999,
                    16
                ]
            },
            "id": "pr2020021001"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 3.8999999999999999,
                "place": "1km NW of Penuelas, Puerto Rico",
                "time": 1579572479210,
                "updated": 1579631898040,
                "tz": -240,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2020021000",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=pr2020021000&format=geojson",
                "felt": 17,
                "cdi": 5.9000000000000004,
                "mmi": null,
                "alert": null,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 244,
                "net": "pr",
                "code": "2020021000",
                "ids": ",us60007btb,pr2020021000,",
                "sources": ",us,pr,",
                "types": ",dyfi,geoserve,moment-tensor,origin,phase-data,",
                "nst": 15,
                "dmin": 0.1326,
                "rms": 0.17000000000000001,
                "gap": 180,
                "magType": "ml",
                "type": "earthquake",
                "title": "M 3.9 - 1km NW of Penuelas, Puerto Rico"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -66.732299999999995,
                    18.001799999999999,
                    16
                ]
            },
            "id": "pr2020021000"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 3.1499999999999999,
                "place": "15km SSE of Guanica, Puerto Rico",
                "time": 1579564205770,
                "updated": 1579676979483,
                "tz": -240,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2020020017",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=pr2020020017&format=geojson",
                "felt": null,
                "cdi": null,
                "mmi": null,
                "alert": null,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 153,
                "net": "pr",
                "code": "2020020017",
                "ids": ",us60007bqw,pr2020020017,",
                "sources": ",us,pr,",
                "types": ",geoserve,origin,phase-data,",
                "nst": 13,
                "dmin": 0.13819999999999999,
                "rms": 0.11,
                "gap": 256,
                "magType": "md",
                "type": "earthquake",
                "title": "M 3.2 - 15km SSE of Guanica, Puerto Rico"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -66.852599999999995,
                    17.839500000000001,
                    6
                ]
            },
            "id": "pr2020020017"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 3.6099999999999999,
                "place": "16km SSE of Guanica, Puerto Rico",
                "time": 1579563301240,
                "updated": 1579577870539,
                "tz": -240,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2020020015",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=pr2020020015&format=geojson",
                "felt": 2,
                "cdi": 2.2000000000000002,
                "mmi": null,
                "alert": null,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 201,
                "net": "pr",
                "code": "2020020015",
                "ids": ",us60007bqn,pr2020020015,",
                "sources": ",us,pr,",
                "types": ",dyfi,geoserve,origin,phase-data,",
                "nst": 13,
                "dmin": 0.082100000000000006,
                "rms": 0.16,
                "gap": 223,
                "magType": "md",
                "type": "earthquake",
                "title": "M 3.6 - 16km SSE of Guanica, Puerto Rico"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -66.853800000000007,
                    17.896999999999998,
                    14
                ]
            },
            "id": "pr2020020015"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 3.2999999999999998,
                "place": "1km W of Tallaboa, Puerto Rico",
                "time": 1579552787457,
                "updated": 1579651306535,
                "tz": -240,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us60007bkl",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us60007bkl&format=geojson",
                "felt": null,
                "cdi": null,
                "mmi": null,
                "alert": null,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 168,
                "net": "us",
                "code": "60007bkl",
                "ids": ",us60007bkl,",
                "sources": ",us,",
                "types": ",geoserve,origin,phase-data,",
                "nst": null,
                "dmin": 0.042000000000000003,
                "rms": 0.31,
                "gap": 164,
                "magType": "ml",
                "type": "earthquake",
                "title": "M 3.3 - 1km W of Tallaboa, Puerto Rico"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -66.728800000000007,
                    17.996200000000002,
                    10
                ]
            },
            "id": "us60007bkl"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 3.2599999999999998,
                "place": "10km S of Tallaboa, Puerto Rico",
                "time": 1579550447270,
                "updated": 1579650976040,
                "tz": -240,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2020020014",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=pr2020020014&format=geojson",
                "felt": 1,
                "cdi": 2,
                "mmi": null,
                "alert": null,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 164,
                "net": "pr",
                "code": "2020020014",
                "ids": ",us60007bki,pr2020020014,",
                "sources": ",us,pr,",
                "types": ",dyfi,geoserve,origin,phase-data,",
                "nst": 10,
                "dmin": 0.16059999999999999,
                "rms": 0.16,
                "gap": 225,
                "magType": "md",
                "type": "earthquake",
                "title": "M 3.3 - 10km S of Tallaboa, Puerto Rico"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -66.719999999999999,
                    17.929500000000001,
                    6
                ]
            },
            "id": "pr2020020014"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 3.73,
                "place": "7km S of Tallaboa, Puerto Rico",
                "time": 1579550405770,
                "updated": 1579650852040,
                "tz": -240,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2020020013",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=pr2020020013&format=geojson",
                "felt": 27,
                "cdi": 3.7999999999999998,
                "mmi": null,
                "alert": null,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 224,
                "net": "pr",
                "code": "2020020013",
                "ids": ",us60007bjq,pr2020020013,",
                "sources": ",us,pr,",
                "types": ",dyfi,geoserve,origin,phase-data,",
                "nst": 13,
                "dmin": 0.1542,
                "rms": 0.28000000000000003,
                "gap": 204,
                "magType": "ml",
                "type": "earthquake",
                "title": "M 3.7 - 7km S of Tallaboa, Puerto Rico"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -66.723299999999995,
                    17.942499999999999,
                    7
                ]
            },
            "id": "pr2020020013"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 3.6200000000000001,
                "place": "8km S of Tallaboa, Puerto Rico",
                "time": 1579550366300,
                "updated": 1579650760040,
                "tz": -240,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2020020012",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=pr2020020012&format=geojson",
                "felt": null,
                "cdi": null,
                "mmi": null,
                "alert": null,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 202,
                "net": "pr",
                "code": "2020020012",
                "ids": ",us60007bjn,pr2020020012,",
                "sources": ",us,pr,",
                "types": ",geoserve,origin,phase-data,",
                "nst": 13,
                "dmin": 0.15629999999999999,
                "rms": 0.14000000000000001,
                "gap": 205,
                "magType": "ml",
                "type": "earthquake",
                "title": "M 3.6 - 8km S of Tallaboa, Puerto Rico"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -66.7273,
                    17.938099999999999,
                    7
                ]
            },
            "id": "pr2020020012"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 3.2999999999999998,
                "place": "14km S of Indios, Puerto Rico",
                "time": 1579550215979,
                "updated": 1579650259040,
                "tz": -240,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us60007bjl",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us60007bjl&format=geojson",
                "felt": null,
                "cdi": null,
                "mmi": null,
                "alert": null,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 168,
                "net": "us",
                "code": "60007bjl",
                "ids": ",us60007bjl,",
                "sources": ",us,",
                "types": ",geoserve,origin,phase-data,",
                "nst": null,
                "dmin": 0.14499999999999999,
                "rms": 0.56999999999999995,
                "gap": 222,
                "magType": "ml",
                "type": "earthquake",
                "title": "M 3.3 - 14km S of Indios, Puerto Rico"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -66.796400000000006,
                    17.8687,
                    10
                ]
            },
            "id": "us60007bjl"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 4.5,
                "place": "4km SW of Tallaboa, Puerto Rico",
                "time": 1579533294150,
                "updated": 1579660528225,
                "tz": -240,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2020020010",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=pr2020020010&format=geojson",
                "felt": 234,
                "cdi": 5.5,
                "mmi": 4.9420000000000002,
                "alert": "green",
                "status": "reviewed",
                "tsunami": 0,
                "sig": 440,
                "net": "pr",
                "code": "2020020010",
                "ids": ",pt20020007,us60007bcp,pr2020020010,",
                "sources": ",pt,us,pr,",
                "types": ",dyfi,geoserve,losspager,moment-tensor,origin,phase-data,shakemap,",
                "nst": 12,
                "dmin": 0.13730000000000001,
                "rms": 0.11,
                "gap": 215,
                "magType": "ml",
                "type": "earthquake",
                "title": "M 4.5 - 4km SW of Tallaboa, Puerto Rico"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -66.742500000000007,
                    17.9618,
                    14
                ]
            },
            "id": "pr2020020010"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 3.1600000000000001,
                "place": "6km SSW of Tallaboa, Puerto Rico",
                "time": 1579532980110,
                "updated": 1579548003040,
                "tz": -240,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2020020011",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=pr2020020011&format=geojson",
                "felt": 1,
                "cdi": 1,
                "mmi": null,
                "alert": null,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 154,
                "net": "pr",
                "code": "2020020011",
                "ids": ",pr2020020011,us60007bcn,",
                "sources": ",pr,us,",
                "types": ",dyfi,geoserve,origin,phase-data,",
                "nst": 13,
                "dmin": 0.13059999999999999,
                "rms": 0.13,
                "gap": 200,
                "magType": "md",
                "type": "earthquake",
                "title": "M 3.2 - 6km SSW of Tallaboa, Puerto Rico"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -66.748999999999995,
                    17.965299999999999,
                    13
                ]
            },
            "id": "pr2020020011"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 3.4500000000000002,
                "place": "8km SSE of Indios, Puerto Rico",
                "time": 1579532383640,
                "updated": 1579561605040,
                "tz": -240,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2020020009",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=pr2020020009&format=geojson",
                "felt": 2,
                "cdi": 3.1000000000000001,
                "mmi": null,
                "alert": null,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 184,
                "net": "pr",
                "code": "2020020009",
                "ids": ",pr2020020009,us60007bcm,",
                "sources": ",pr,us,",
                "types": ",dyfi,geoserve,origin,phase-data,",
                "nst": 12,
                "dmin": 0.066699999999999995,
                "rms": 0.32000000000000001,
                "gap": 187,
                "magType": "ml",
                "type": "earthquake",
                "title": "M 3.5 - 8km SSE of Indios, Puerto Rico"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -66.812799999999996,
                    17.981000000000002,
                    11
                ]
            },
            "id": "pr2020020009"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 3.2999999999999998,
                "place": "6km SSW of Tallaboa, Puerto Rico",
                "time": 1579529764730,
                "updated": 1579560403040,
                "tz": -240,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us60007bc9",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us60007bc9&format=geojson",
                "felt": null,
                "cdi": null,
                "mmi": null,
                "alert": null,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 168,
                "net": "us",
                "code": "60007bc9",
                "ids": ",us60007bc9,",
                "sources": ",us,",
                "types": ",geoserve,origin,phase-data,",
                "nst": null,
                "dmin": 0.069000000000000006,
                "rms": 0.29999999999999999,
                "gap": 198,
                "magType": "ml",
                "type": "earthquake",
                "title": "M 3.3 - 6km SSW of Tallaboa, Puerto Rico"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -66.7303,
                    17.937999999999999,
                    10
                ]
            },
            "id": "us60007bc9"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 3.1200000000000001,
                "place": "6km SW of Liborio Negron Torres, Puerto Rico",
                "time": 1579526084670,
                "updated": 1579534432421,
                "tz": -240,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2020020008",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=pr2020020008&format=geojson",
                "felt": 2,
                "cdi": 2,
                "mmi": null,
                "alert": null,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 150,
                "net": "pr",
                "code": "2020020008",
                "ids": ",pr2020020008,us60007bbw,",
                "sources": ",pr,us,",
                "types": ",dyfi,geoserve,origin,phase-data,",
                "nst": 13,
                "dmin": 0.113,
                "rms": 0.14999999999999999,
                "gap": 218,
                "magType": "md",
                "type": "earthquake",
                "title": "M 3.1 - 6km SW of Liborio Negron Torres, Puerto Rico"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -66.989999999999995,
                    17.9528,
                    13
                ]
            },
            "id": "pr2020020008"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 4.2000000000000002,
                "place": "2km E of Magas Arriba, Puerto Rico",
                "time": 1579514181230,
                "updated": 1579577647842,
                "tz": -240,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2020020006",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=pr2020020006&format=geojson",
                "felt": 27,
                "cdi": 5.7000000000000002,
                "mmi": null,
                "alert": null,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 287,
                "net": "pr",
                "code": "2020020006",
                "ids": ",us60007b9l,pr2020020006,",
                "sources": ",us,pr,",
                "types": ",dyfi,geoserve,moment-tensor,origin,phase-data,",
                "nst": 12,
                "dmin": 0.12509999999999999,
                "rms": 0.20000000000000001,
                "gap": 194,
                "magType": "ml",
                "type": "earthquake",
                "title": "M 4.2 - 2km E of Magas Arriba, Puerto Rico"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -66.754099999999994,
                    17.971499999999999,
                    6
                ]
            },
            "id": "pr2020020006"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 4.5999999999999996,
                "place": "7km SSE of Tallaboa, Puerto Rico",
                "time": 1579512996270,
                "updated": 1579644630533,
                "tz": -240,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2020020005",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=pr2020020005&format=geojson",
                "felt": 78,
                "cdi": 5.7999999999999998,
                "mmi": 5.9050000000000002,
                "alert": "green",
                "status": "reviewed",
                "tsunami": 0,
                "sig": 371,
                "net": "pr",
                "code": "2020020005",
                "ids": ",pt20020005,us60007b9a,pr2020020005,",
                "sources": ",pt,us,pr,",
                "types": ",dyfi,geoserve,losspager,moment-tensor,origin,phase-data,shakemap,",
                "nst": 12,
                "dmin": 0.12640000000000001,
                "rms": 0.14999999999999999,
                "gap": 195,
                "magType": "ml",
                "type": "earthquake",
                "title": "M 4.6 - 7km SSE of Tallaboa, Puerto Rico"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -66.752799999999993,
                    17.974799999999998,
                    7
                ]
            },
            "id": "pr2020020005"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 3.5699999999999998,
                "place": "3km WSW of Tallaboa, Puerto Rico",
                "time": 1579512833370,
                "updated": 1579522111641,
                "tz": -240,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2020020007",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=pr2020020007&format=geojson",
                "felt": 4,
                "cdi": 3.7999999999999998,
                "mmi": null,
                "alert": null,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 198,
                "net": "pr",
                "code": "2020020007",
                "ids": ",us60007b99,pr2020020007,",
                "sources": ",us,pr,",
                "types": ",dyfi,geoserve,origin,phase-data,",
                "nst": 13,
                "dmin": 0.13270000000000001,
                "rms": 0.080000000000000002,
                "gap": 194,
                "magType": "md",
                "type": "earthquake",
                "title": "M 3.6 - 3km WSW of Tallaboa, Puerto Rico"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -66.746499999999997,
                    17.9756,
                    6
                ]
            },
            "id": "pr2020020007"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 3.7200000000000002,
                "place": "4km SSW of Tallaboa, Puerto Rico",
                "time": 1579504264470,
                "updated": 1579529823583,
                "tz": -240,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2020020004",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=pr2020020004&format=geojson",
                "felt": 25,
                "cdi": 5.5999999999999996,
                "mmi": null,
                "alert": null,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 227,
                "net": "pr",
                "code": "2020020004",
                "ids": ",us60007b6f,pr2020020004,",
                "sources": ",us,pr,",
                "types": ",dyfi,geoserve,origin,phase-data,",
                "nst": 12,
                "dmin": 0.14829999999999999,
                "rms": 0.14000000000000001,
                "gap": 204,
                "magType": "md",
                "type": "earthquake",
                "title": "M 3.7 - 4km SSW of Tallaboa, Puerto Rico"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -66.730599999999995,
                    17.962,
                    6
                ]
            },
            "id": "pr2020020004"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 4.5,
                "place": "0km WSW of Tallaboa, Puerto Rico",
                "time": 1579497979710,
                "updated": 1579644373433,
                "tz": -240,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2020020003",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=pr2020020003&format=geojson",
                "felt": 140,
                "cdi": 5.5999999999999996,
                "mmi": 5.444,
                "alert": "green",
                "status": "reviewed",
                "tsunami": 0,
                "sig": 390,
                "net": "pr",
                "code": "2020020003",
                "ids": ",pt20020002,us60007b4l,pr2020020003,",
                "sources": ",pt,us,pr,",
                "types": ",dyfi,geoserve,losspager,moment-tensor,origin,phase-data,shakemap,",
                "nst": 16,
                "dmin": 0.1384,
                "rms": 0.22,
                "gap": 192,
                "magType": "ml",
                "type": "earthquake",
                "title": "M 4.5 - 0km WSW of Tallaboa, Puerto Rico"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -66.740799999999993,
                    17.977,
                    7
                ]
            },
            "id": "pr2020020003"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 3.46,
                "place": "5km SE of La Parguera, Puerto Rico",
                "time": 1579496941830,
                "updated": 1579534053239,
                "tz": -240,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2020020002",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=pr2020020002&format=geojson",
                "felt": 4,
                "cdi": 3.1000000000000001,
                "mmi": null,
                "alert": null,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 185,
                "net": "pr",
                "code": "2020020002",
                "ids": ",us60007b4h,pr2020020002,",
                "sources": ",us,pr,",
                "types": ",dyfi,geoserve,origin,phase-data,",
                "nst": 13,
                "dmin": 0.11509999999999999,
                "rms": 0.089999999999999997,
                "gap": 219,
                "magType": "md",
                "type": "earthquake",
                "title": "M 3.5 - 5km SE of La Parguera, Puerto Rico"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -66.991600000000005,
                    17.950500000000002,
                    9
                ]
            },
            "id": "pr2020020002"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 3.2999999999999998,
                "place": "12km SW of Guanica, Puerto Rico",
                "time": 1579493539540,
                "updated": 1579501569162,
                "tz": -240,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/pr2020020001",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=pr2020020001&format=geojson",
                "felt": 3,
                "cdi": 3.7999999999999998,
                "mmi": null,
                "alert": null,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 169,
                "net": "pr",
                "code": "2020020001",
                "ids": ",us60007b3g,pr2020020001,",
                "sources": ",us,pr,",
                "types": ",dyfi,geoserve,origin,phase-data,",
                "nst": 13,
                "dmin": 0.1221,
                "rms": 0.13,
                "gap": 234,
                "magType": "ml",
                "type": "earthquake",
                "title": "M 3.3 - 12km SW of Guanica, Puerto Rico"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -66.979600000000005,
                    17.9056,
                    4
                ]
            },
            "id": "pr2020020001"
        }
    ],
    "bbox": [
        -67.0036,
        17.7841,
        3,
        -66.6676,
        18.0463,
        16
    ]
}
'''

import datetime
x = []
y = []
data = json.loads(features_string)

for eq in data['features']:
    props = eq['properties']
    if props['mag'] >= 3.5:
        y.append(props['mag'])
        x.append(datetime.datetime.fromtimestamp(props['time']/1000.0))

# print(x, y)

x.reverse()
y.reverse()

import matplotlib.pyplot as plt
newx = []
for i in x:
    newx.append(i.strftime("%H:%M"))
    
plt.bar(newx, y)
plt.xlabel("Time")
plt.ylabel("Magnitude")
plt.ylim(3,7)
plt.title("Puerto Rico Seismic Activity on January 20, 2020")
plt.xticks(rotation=90)
fig = plt.gcf()
fig.set_size_inches(25.5, 5.5)
