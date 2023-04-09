package main

import (
	"fmt";
	"encoding/json";
	"net/http";
	"net/url";
	"io/ioutil"
)

func getall() interface{}{
	url := "http://127.0.0.1:5001/getall"
	resp,err := http.Get(url)
	if err != nil{
		panic(err)
	}
	defer resp.Body.Close()

	var data interface{}
	err = json.NewDecoder(resp.Body).Decode(&data)
	if err!= nil{
		panic(err)
	}
	return data
}

func adddata(){
	url_add:= "http://127.0.0.1:5001/add"
	params_add := url.Values{}
	params_add.Add("item","a chicken from america")
	params_add.Add("date","2019-01-01")
	params_add.Add("weight","1.5")
	params_add.Add("transtype","purchase")
	params_add.Add("remark","a very good chicken from america, but there are only bones,where is the meat??")

	resp, err := http.Get(url_add + "?" + params_add.Encode())
	fmt.Println(url_add + "?" + params_add.Encode())
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	bodyBytes, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}
	bodyString := string(bodyBytes)

	fmt.Println(bodyString)
}

func main(){
	//adddata()
	fmt.Println(getall())
}