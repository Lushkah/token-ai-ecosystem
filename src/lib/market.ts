export type Market={bitcoin:{usd:number,usd_24h_change:number},ethereum:{usd:number,usd_24h_change:number}};
export async function getMarket():Promise<Market>{const r=await fetch("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd&include_24hr_change=true"); if(!r.ok)throw new Error("Market data unavailable"); return r.json();}
