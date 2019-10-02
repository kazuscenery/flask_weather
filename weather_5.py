# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 11:21:04 2019

@author: KS
"""
from flask import Flask, render_template , request#追加
#from weather_3 import weather_forecast
import requests
import json

app = Flask(__name__)# インスタンスの作成


@app.route('/')
def weather_data():
# APIキーの指定
#apikey = "{あなたのAPIKEYを入れてください}" #{}　要らないドキュメント読もう
    apikey = "4f014110bfdd5104f901ff1cd75112db"

# 天気を調べたい都市の一覧
    cities = ["Tokyo,JP"]
    weather_d = []
# APIのひな型
    api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

# 温度変換(ケルビン→摂氏)
    k2c = lambda k: k - 273.15

# 各都市の温度を取得する
    for name in cities:
    # APIのURLを得る
        url = api.format(city=name, key=apikey)
    # 実際にAPIにリクエストを送信して結果を取得する
        r = requests.get(url)
    # 結果はJSON形式なのでデコードする
        data = json.loads(r.text)
    # 結果を出力
        """
        print("+ 都市=", data["name"])
        print("| 天気=", data["weather"][0]["description"])
        print("| 最低気温=", k2c(data["main"]["temp_min"]))
        print("| 最高気温=", k2c(data["main"]["temp_max"]))
        print("| 湿度=", data["main"]["humidity"])
        print("| 気圧=", data["main"]["pressure"])
        print("| 風向き=", data["wind"]["deg"])
        print("| 風速度=", data["wind"]["speed"])
        print("")
        """
        city_name = (data["name"])#都市
        weather_d = (data["weather"][0]["description"])#天気
        min = (k2c(data["main"]["temp_min"]))#"最低気温=",
        #min = "{:.1f}".format(min_a[0])
        max = (k2c(data["main"]["temp_max"]))#"最高気温=",
        humidity = (data["main"]["humidity"])#"| 湿度=",
        pressure = ( data["main"]["pressure"])#"| 気圧=",
        #print("| 風向き=", data["wind"]["deg"])
        #print("| 風速度=", data["wind"]["speed"])
        #print("")
        #{cities:cities}name =neme ,cities =cities,

        return render_template('weather.html',cities =cities,
        title='flask test', city_name=city_name, weather_d=weather_d,
        min = min, max = max, humidity = humidity, pressure = pressure)
        #変更
@app.route('/forecast')
def weather_forecast():
# APIキーの指定
#apikey = "{あなたのAPIKEYを入れてください}" #{}　要らないドキュメント読もう
    apikey = "4f014110bfdd5104f901ff1cd75112db"

# 天気を調べたい都市の一覧
    cities = ["Tokyo,JP"]#, "London,UK", "New York,US"]
    weather_d = []
# APIのひな型
    #api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"
    api = "http://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={key}"
# 温度変換(ケルビン→摂氏)
    k2c = lambda k: k - 273.15

# 各都市の温度を取得する
    for name in cities:
    # APIのURLを得る
        url = api.format(city=name, key=apikey)
    # 実際にAPIにリクエストを送信して結果を取得する
        r = requests.get(url)
    # 結果はJSON形式なのでデコードする
        data = json.loads(r.text)
    # 結果を出力

        w=[p['weather'][0]['main'] for i, p in enumerate(data['list']) if i < 3]
        #最低気温
        temp_min_list = []

        for i, p in enumerate(data['list']):
            if i < 3:
                temp_min_list.append(k2c(p['main']['temp_min']))


        temp_max_list = []
        for i, p in enumerate(data['list']):
            if i < 3:
                temp_max_list.append(k2c(p['main']['temp_max']))


        temp_list = []
        for i, p in enumerate(data['list']):
            if i < 3:
                temp_list.append(k2c(p['main']['temp']))

        x = 0
        a = ("3hours: weather,{} / temp{:.1f} degrees".format(w[x],temp_list[x]))
        x = 1
        b = ("6hours: weather,{} / temp{:.1f} degrees".format(w[x],temp_list[x]))
        x = 2
        c = ("9hours: weather,{} / temp{:.1f} degrees".format(w[x],temp_list[x]))



        return render_template('weather_2.html',cities =cities,
        #title='flask test', city_name=city_name, weather_d=weathers_d,
        #temp_min_list = temp_min_list,
        #temp_max_list = temp_max_list,
        #temp_list = temp_list,
        a = a, b = b, c = c)#,

#weather_data()

if __name__ == "__main__":
    app.run(debug=True)
