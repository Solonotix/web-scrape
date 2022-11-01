import { Buffer } from "https://deno.land/std@0.161.0/node/buffer.ts";


const response = await fetch('https://www.nohrsc.noaa.gov/snowfall/data/202202/sfav2_CONUS_24h_2022020100_grid184.grb2');

let data = [];
for(let reader = response.body.getReader(), done = false, value = Buffer.alloc(0); !done; ({ done, value } = await reader.read())) {
    data.push(value);
}

console.log(Buffer.byteLength(Buffer.concat(data)));
