import { DataGrid, GridRowsProp, GridColDef } from "@mui/x-data-grid";
import INFY from "./INFY.json";
import { INFY_dataType } from "./INFY.tsx";

function App() {
  const json_arr = INFY as INFY_dataType[];
  const length_json_arr = json_arr.length;
  const keys_json = Object.keys(INFY[0]);
  const length_keys_json = keys_json.length;

  let column_data: GridColDef[] = [];
  for (let i = 0; i < length_keys_json; i++) {
    column_data = column_data.concat([{ field: keys_json[i], width: 100 }]);
  }
  let row_data: GridRowsProp = [];
  for (let i = 0; i < length_json_arr; i++) {
    row_data = row_data.concat({
      id: json_arr[i].TIMESTAMP,
      SYMBOL: json_arr[i].SYMBOL,
      SERIES: json_arr[i].SERIES,
      OPEN: json_arr[i].OPEN,
      HIGH: json_arr[i].HIGH,
      LOW: json_arr[i].LOW,
      CLOSE: json_arr[i].CLOSE,
      LAST: json_arr[i].LAST,
      PREVCLOSE: json_arr[i].PREVCLOSE,
      TOTTRDQTY: json_arr[i].TOTTRDQTY,
      TOTTRDVAL: json_arr[i].TOTTRDVAL,
      TIMESTAMP: json_arr[i].TIMESTAMP,
      TOTALTRADES: json_arr[i].TOTALTRADES,
      ISIN: json_arr[i].ISIN,
      GAIN_LOSS: json_arr[i].GAIN_LOSS,
    });
  }
  return (
    <div>
      <DataGrid rows={row_data} columns={column_data} />
    </div>
  );
}
export default App;
