import { DataGrid, GridRowsProp, GridColDef } from "@mui/x-data-grid";
import INFY from "./INFY.json"
import {INFY_dataType} from "./INFY"

function App(){
  const data_arr = INFY as INFY_dataType[]

  const column_data: GridColDef[] = [
    {field: "SYMBOL", width: 150},
    {field: "SERIES", width: 150},
    {field: "OPEN", width: 150},
    {field: "HIGH", width: 150},
    {field: "LOW", width: 150},
    {field: "CLOSE", width: 150},
    {field: "LAST", width: 150},
    {field: "PREVCLOSE", width: 150},
    {field: "TOTTRDQTY", width: 150},
    {field: "TOTTRDVAL", width: 150},
    {field: "TIMESTAMP", width: 150}, 
    {field: "TOTALTRADES", width: 150},
    {field: "ISIN", width: 150},
    {field: "GAIN_LOSS", width: 150},
  ]
  const row_data: GridRowsProp = [
    { id: data_arr[0].TIMESTAMP, SYMBOL: data_arr[0].SYMBOL, SERIES: data_arr[0].SERIES, OPEN: data_arr[0].OPEN, HIGH: data_arr[0].HIGH, LOW:data_arr[0].LOW, CLOSE: data_arr[0].CLOSE, LAST: data_arr[0].LAST, PREVCLOSE: data_arr[0].PREVCLOSE, TOTTRDQTY: data_arr[0].TOTTRDQTY, TOTTRDVAL: data_arr[0].TOTTRDVAL, TIMESTAMP: data_arr[0].TIMESTAMP, TOTALTRADES: data_arr[0].TOTALTRADES, ISIN: data_arr[0].ISIN, GAIN_LOSS: data_arr[0].GAIN_LOSS},
    { id: data_arr[1].TIMESTAMP, SYMBOL: data_arr[1].SYMBOL, SERIES: data_arr[1].SERIES, OPEN: data_arr[1].OPEN, HIGH: data_arr[1].HIGH, LOW:data_arr[1].LOW, CLOSE: data_arr[1].CLOSE, LAST: data_arr[1].LAST, PREVCLOSE: data_arr[1].PREVCLOSE, TOTTRDQTY: data_arr[1].TOTTRDQTY, TOTTRDVAL: data_arr[1].TOTTRDVAL, TIMESTAMP: data_arr[1].TIMESTAMP, TOTALTRADES: data_arr[1].TOTALTRADES, ISIN: data_arr[1].ISIN, GAIN_LOSS: data_arr[1].GAIN_LOSS},
    { id: data_arr[2].TIMESTAMP, SYMBOL: data_arr[2].SYMBOL, SERIES: data_arr[2].SERIES, OPEN: data_arr[2].OPEN, HIGH: data_arr[2].HIGH, LOW:data_arr[2].LOW, CLOSE: data_arr[2].CLOSE, LAST: data_arr[2].LAST, PREVCLOSE: data_arr[2].PREVCLOSE, TOTTRDQTY: data_arr[2].TOTTRDQTY, TOTTRDVAL: data_arr[2].TOTTRDVAL, TIMESTAMP: data_arr[2].TIMESTAMP, TOTALTRADES: data_arr[2].TOTALTRADES, ISIN: data_arr[2].ISIN, GAIN_LOSS: data_arr[2].GAIN_LOSS},
    { id: data_arr[3].TIMESTAMP, SYMBOL: data_arr[3].SYMBOL, SERIES: data_arr[3].SERIES, OPEN: data_arr[3].OPEN, HIGH: data_arr[3].HIGH, LOW:data_arr[3].LOW, CLOSE: data_arr[3].CLOSE, LAST: data_arr[3].LAST, PREVCLOSE: data_arr[3].PREVCLOSE, TOTTRDQTY: data_arr[3].TOTTRDQTY, TOTTRDVAL: data_arr[3].TOTTRDVAL, TIMESTAMP: data_arr[3].TIMESTAMP, TOTALTRADES: data_arr[3].TOTALTRADES, ISIN: data_arr[3].ISIN, GAIN_LOSS: data_arr[3].GAIN_LOSS},
    { id: data_arr[4].TIMESTAMP, SYMBOL: data_arr[4].SYMBOL, SERIES: data_arr[4].SERIES, OPEN: data_arr[4].OPEN, HIGH: data_arr[4].HIGH, LOW:data_arr[4].LOW, CLOSE: data_arr[4].CLOSE, LAST: data_arr[4].LAST, PREVCLOSE: data_arr[4].PREVCLOSE, TOTTRDQTY: data_arr[4].TOTTRDQTY, TOTTRDVAL: data_arr[4].TOTTRDVAL, TIMESTAMP: data_arr[4].TIMESTAMP, TOTALTRADES: data_arr[4].TOTALTRADES, ISIN: data_arr[4].ISIN, GAIN_LOSS: data_arr[4].GAIN_LOSS},
  ]
  return <div>
    <DataGrid rows={row_data} columns={column_data}/>
  </div>
}
export default App;