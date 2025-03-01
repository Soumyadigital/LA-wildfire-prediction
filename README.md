# LA wildfire prediction

This streamlit based application is built for predicting future wildfire probability from historical data(specifically for LA, USA)
using dataset by [NOAA](https://www.ncdc.noaa.gov/) and [Google earth engine](https://earthengine.google.com/)


## Dependencies

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install streamlit
pip install pandas
pip install numpy
pip install tensorflow==2.18.0
```
python version:3.11.11

## For Usage run:

```python
streamlit run app.py
```
Then click on the generated link to access the webapp

## Details about the dataset

Note: Details about model selection mentioned on colab notebook

Column Name	Description
- STATION:	Station ID or identifier
- NAME	Name of the weather station.
- LATITUDE	Latitude of the station.
- LONGITUDE	Longitude of the station.
- ELEVATION	Elevation of the station.
- DATE	Date of the observation.
- AWND	Average wind speed.
- PGTM	Peak gust time (time of the highest wind gust).
- PRCP	Precipitation (in inches or millimeters).
- SNOW	Snowfall (in inches or centimeters).
- SNWD	Snow depth (in inches or centimeters).
- TAVG	Average temperature.
- TMAX	Maximum temperature.
- TMIN	Minimum temperature.
- WDF2	Direction of the fastest 2-minute wind.
- WDF5	Direction of the fastest 5-minute wind.
- WSF2	Fastest 2-minute wind speed.
- WSF5	Fastest 5-minute wind speed.
- WT01 to WT08	Weather type codes (e.g., fog, rain, snow, etc.).

The wildfire in LA can happen when:
- PRCP < 0.39 (inch)
- TMAX > 21 (degree celsius)

 

## License

[MIT](https://choosealicense.com/licenses/mit/)